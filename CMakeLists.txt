cmake_minimum_required(VERSION 3.20)

project(
    DistanceRiscvExample
    VERSION 0.1
    DESCRIPTION "Distance example in CMake"
    LANGUAGES C
)

### CMake modules path in folder cmake/
list(APPEND CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_SOURCE_DIR}/cmake/modules")

if(CMAKE_PROJECT_NAME STREQUAL PROJECT_NAME) 
     set(CMAKE_CXX_EXTENSIONS OFF)   # Let's nicely support folders in IDEs   
     set_property(GLOBAL PROPERTY USE_FOLDERS ON)   
     include(CTest)   # Docs only available if this is the main app   

     find_package(Doxygen)   
     if(Doxygen_FOUND)  
         add_subdirectory(docs)   
     else()     
         message(STATUS "Doxygen not found, not building docs")   
     endif() 
 endif() 
 
if((CMAKE_PROJECT_NAME STREQUAL PROJECT_NAME OR MODERN_CMAKE_BUILD_TESTING)    
    AND BUILD_TESTING)   
    add_subdirectory(tests) 
endif()

################################################################################
#################### PACKAGES AND FILES
################################################################################
#include(${PROJECT_SOURCE_DIR}/cmake/riscv.cmake)    # RISCV GCC toolchain
#set(CMAKE_TOOLCHAIN_FILE ${PROJECT_SOURCE_DIR}/cmake/riscv.cmake)

include(FetchContent)
include(ExternalProject)    

find_package(CMSIS)
find_package(Pk)        # Proxy-kernel
find_package(Spike)     # Spike simulator

add_subdirectory(src)
add_subdirectory(apps)

find_program(OBJDUMP riscv64-unknown-elf-objdump)
find_program(Python3 COMPONENTS Interpreter)


set(LOG_DIR ${CMAKE_CURRENT_BINARY_DIR}/log)
set(RESULT_DIR ${CMAKE_CURRENT_BINARY_DIR}/results)
file(MAKE_DIRECTORY ${LOG_DIR})
file(MAKE_DIRECTORY ${RESULT_DIR})
################################################################################
#################### COMMANDS
################################################################################

### Install Python modules used in this project
add_custom_command(OUTPUT py_req_install.stamp
    COMMAND python3 -m pip install -U -r ${PY_REQ_FILE}
    COMMAND touch ${CMAKE_BINARY_DIR}/py_req_install.stamp
)
add_custom_target(python-install-libraries
    DEPENDS py_req_install.stamp
)

### The result process: objectdump -> find address -> simulate -> print result
# SOURCE_FILES lists all target source files from apps/CMakeLists.txt file
foreach(targetsourcefile ${SOURCE_FILES})
    string(REPLACE ".c" "" targetsource ${targetsourcefile})

    ### Object dump
    set(OBJDUMP_FILE ${LOG_DIR}/${targetsource}-objdump.txt)

    add_custom_command(OUTPUT ${OBJDUMP_FILE}
        COMMAND ${OBJDUMP} -d $<TARGET_FILE:${targetsource}> > ${OBJDUMP_FILE}
        DEPENDS ${targetsource}
    )
    add_custom_target("objdump-${targetsource}"
        DEPENDS ${OBJDUMP_FILE}
    )


    ### Python find addresses from objdump
    set(PYTHON_OBJDUMP ${PROJECT_SOURCE_DIR}/scripts/objdump_parser.py)
    set(PY_REQ_FILE ${PROJECT_SOURCE_DIR}/py_requirements.txt)
    set(SPIKE_CMD_FILE ${LOG_DIR}/${targetsource}-spike-cmd.txt)

    add_custom_command(OUTPUT ${SPIKE_CMD_FILE}
        COMMAND python3 ${PYTHON_OBJDUMP} ${OBJDUMP_FILE} ${SPIKE_CMD_FILE}
        DEPENDS ${OBJDUMP_FILE}
    )
    add_custom_target("python-spike-cmd-${targetsource}"
        DEPENDS ${SPIKE_CMD_FILE}
    )


    ### Spike simulation
    set(SPIKE_LOG_FILE ${LOG_DIR}/${targetsource}-spike-log.txt)

    add_custom_command(OUTPUT ${SPIKE_LOG_FILE}
        COMMAND spike -d -l --debug-cmd=${SPIKE_CMD_FILE} --log=${SPIKE_LOG_FILE} --isa=RV32IMAFDC
        $<TARGET_FILE:pk_exe> $<TARGET_FILE:${targetsource}>
        DEPENDS ${targetsource} pk_exe ${SPIKE_CMD_FILE}
    )
    add_custom_target("spike-log-${targetsource}"
        DEPENDS ${SPIKE_LOG_FILE}
    )


    ### Extract instructions from Spike log
    set(PYTHON_SPIKE_PARSER ${PROJECT_SOURCE_DIR}/scripts/spike_parser.py)
    set(PYTHON_FREQ_FILE ${RESULT_DIR}/${targetsource}) # TODO: Change this name

    add_custom_command(OUTPUT ${PYTHON_FREQ_FILE}
        COMMAND python3 ${PYTHON_SPIKE_PARSER} ${SPIKE_LOG_FILE} ${PYTHON_FREQ_FILE}
        DEPENDS ${SPIKE_LOG_FILE}
    )
    add_custom_target("python-extract-instructions-${targetsource}"
        DEPENDS ${PYTHON_FREQ_FILE}
    )
endforeach(targetsourcefile ${SOURCE_FILES})

