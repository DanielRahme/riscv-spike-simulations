
cmake_minimum_required(VERSION 3.20)

project(
    DistanceRiscvExample
    VERSION 0.1
    DESCRIPTION "Distance example in CMake"
    LANGUAGES C
)

if(CMAKE_PROJECT_NAME STREQUAL PROJECT_NAME) 


     set(CMAKE_CXX_EXTENSIONS OFF)   # Let's nicely support folders in IDEs   
     set_property(GLOBAL PROPERTY USE_FOLDERS ON)   
     

     # Testing only available if this is the main app   # Note this needs to be done in the main CMakeLists   # since it calls enable_testing, which must be in the   # main CMakeLists.   

     include(CTest)   # Docs only available if this is the main app   

     find_package(Doxygen)   
     if(Doxygen_FOUND)  
         add_subdirectory(docs)   
     else()     
         message(STATUS "Doxygen not found, not building docs")   
     endif() 
 endif() 
 

include(${PROJECT_SOURCE_DIR}/cmake/riscv.cmake)
include(FetchContent)
include(ExternalProject)    


add_subdirectory(src)
add_subdirectory(apps)

### Get proxy-kernel
set(PK_SRC_DIR ${PROJECT_BINARY_DIR}/pk)
set(PK_CONFIG_FLAGS --prefix=/opt/riscv/bin --host=riscv64-unknown-elf --with-arch=rv32imafdc --enable-fp-emulation)
#set(PK_CONFIG_FLAGS --prefix=/opt/riscv/bin --host=riscv64-unknown-elf --with-arch=rv32i)

ExternalProject_Add(pkproj
    GIT_REPOSITORY https://github.com/riscv-software-src/riscv-pk
    SOURCE_DIR ${PK_SRC_DIR}
    CONFIGURE_COMMAND "${PK_SRC_DIR}/configure" ${PK_CONFIG_FLAGS}
    #CMAKE_ARGS -DCMAKE_TOOLCHAIN_FILE=${PROJECT_SOURCE_DIR}/cmake/riscv.cmake
    BUILD_COMMAND ${MAKE}
    INSTALL_COMMAND cmake -E echo "Skipping install step."
)
ExternalProject_Get_Property(pkproj BINARY_DIR)

set(PK_BIN_DIR ${BINARY_DIR})

add_executable(pk_exe IMPORTED)
set_target_properties(pk_exe
    PROPERTIES 
    IMPORTED_LOCATION "${PK_BIN_DIR}/pk")

add_dependencies(pk_exe pkproj)


### Get Spike
set(SPIKE_SRC_DIR ${PROJECT_BINARY_DIR}/spike)

ExternalProject_Add(spikeproj
    GIT_REPOSITORY https://github.com/riscv-software-src/riscv-isa-sim
    SOURCE_DIR ${SPIKE_SRC_DIR}
    CONFIGURE_COMMAND "${SPIKE_SRC_DIR}/configure" --prefix=/opt/riscv-spike
    BUILD_COMMAND ${MAKE}
    INSTALL_COMMAND cmake -E echo "Skipping install step."
)
ExternalProject_Get_Property(spikeproj BINARY_DIR)


## Spike log Command
set(SPIKE_BIN_DIR ${BINARY_DIR})
set(SPIKE_LOG_FILE ${PROJECT_BINARY_DIR}/spike-log.txt)

add_executable(spike IMPORTED)
set_target_properties(spike 
    PROPERTIES 
    IMPORTED_LOCATION "${SPIKE_BIN_DIR}/spike")

add_dependencies(spike spikeproj pkproj)


#find_program(PK pk)
set(SPIKE_CMD_FILE ${PROJECT_SOURCE_DIR}/debug-cmd.txt)

add_custom_command(OUTPUT ${SPIKE_LOG_FILE}
    COMMAND spike -d -l --debug-cmd=${SPIKE_CMD_FILE} --log=${SPIKE_LOG_FILE} --isa=RV32IMAFDC
    $<TARGET_FILE:pk_exe> $<TARGET_FILE:main>
    DEPENDS main
)


add_custom_target(spike_log
    DEPENDS ${SPIKE_LOG_FILE}
)


#add_custom_command(TARGET main
#    COMMAND riscv64-unknown-elf-objdump -D main > main.dump.txt
#    COMMENT "Creat a objdump of main binary"
#    DEPENDS main
#    )






if((CMAKE_PROJECT_NAME STREQUAL PROJECT_NAME OR MODERN_CMAKE_BUILD_TESTING)    
    AND BUILD_TESTING)   
    add_subdirectory(tests) 
endif()
