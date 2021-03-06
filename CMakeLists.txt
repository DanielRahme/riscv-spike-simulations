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

     find_package(Doxygen)   
     if(Doxygen_FOUND)  
         add_subdirectory(docs)   
     else()     
         message(STATUS "Doxygen not found, not building docs")   
     endif() 
 endif() 
 

################################################################################
#################### PACKAGES AND FILES
################################################################################
include(FetchContent)
include(ExternalProject)    

find_package(CMSIS)
find_package(Pk)        # Proxy-kernel
find_package(Spike)     # Spike simulator

add_subdirectory(lib)
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
set(PY_REQ_FILE ${PROJECT_SOURCE_DIR}/py_requirements.txt)
set(PY_REQUIREMENTS py_req_install.stamp)

add_custom_command(OUTPUT ${PY_REQUIREMENTS}
    COMMAND python3 -m pip install --user -U -r ${PY_REQ_FILE}
    COMMAND touch ${CMAKE_BINARY_DIR}/${PY_REQUIREMENTS}
    DEPENDS ${PY_REQ_FILE}
)
add_custom_target(python-install-libraries
    DEPENDS ${PY_REQUIREMENTS}
)

### The result process: objectdump -> find address -> simulate -> print result
# SOURCE_FILES lists all target source files from apps/CMakeLists.txt file
set(TEST_RESULTS "")
set(ICOUNT_PLOTS "")
set(IGROUP_PLOTS "")

foreach(targetsourcefile ${SOURCE_FILES})
    string(REPLACE ".c" "" targetsource ${targetsourcefile})

    ### Object dump
    set(OBJDUMP_FILE ${LOG_DIR}/${targetsource}-objdump.txt)

    add_custom_command(OUTPUT ${OBJDUMP_FILE}
        COMMAND ${OBJDUMP} -d $<TARGET_FILE:${targetsource}> > ${OBJDUMP_FILE}
        DEPENDS ${targetsource}
    )

    ### Python find addresses from objdump
    set(PYTHON_OBJDUMP ${PROJECT_SOURCE_DIR}/scripts/objdump_parser.py)
    set(SPIKE_CMD_FILE ${LOG_DIR}/${targetsource}-spike-cmd.txt)

    add_custom_command(OUTPUT ${SPIKE_CMD_FILE}
        COMMAND python3 ${PYTHON_OBJDUMP} < ${OBJDUMP_FILE} > ${SPIKE_CMD_FILE}
        DEPENDS ${OBJDUMP_FILE} ${PYTHON_OBJDUMP}
    )

    ### Spike simulation
    set(SPIKE_LOG_FILE ${LOG_DIR}/${targetsource}-spike-log.txt)

    add_custom_command(OUTPUT ${SPIKE_LOG_FILE}
        COMMAND $<TARGET_FILE:spike> -d -l --debug-cmd=${SPIKE_CMD_FILE} --log=${SPIKE_LOG_FILE} --isa=RV32IMAFDC
        $<TARGET_FILE:pk_exe> $<TARGET_FILE:${targetsource}>
        DEPENDS ${targetsource} pk_exe ${SPIKE_CMD_FILE}
    )

    ### Extract instructions from Spike log
    set(PYTHON_SPIKE_PARSER ${PROJECT_SOURCE_DIR}/scripts/spike_parser.py)
    set(INSTR_COUNT_FILE ${RESULT_DIR}/${targetsource}-freq-instruct.csv)
    set(INSTR_COUNT_PATH ${RESULT_DIR}/${targetsource})

    add_custom_command(OUTPUT ${INSTR_COUNT_FILE}
        COMMAND python3 ${PYTHON_SPIKE_PARSER} ${targetsource} < ${SPIKE_LOG_FILE} > ${INSTR_COUNT_FILE}
        DEPENDS ${SPIKE_LOG_FILE} ${PY_REQUIREMENTS} ${PYTHON_SPIKE_PARSER}
    )

    ### Calculate execution time
    set(CALC_EXEC_TIME_SCRIPT ${PROJECT_SOURCE_DIR}/scripts/calc_execution_time.py)
    set(EXEC_TIME_CSV ${RESULT_DIR}/${targetsource}-results.csv)

    add_custom_command(OUTPUT ${EXEC_TIME_CSV}
        COMMAND python3 ${CALC_EXEC_TIME_SCRIPT} ${targetsource} < ${INSTR_COUNT_FILE} > ${EXEC_TIME_CSV}
        DEPENDS ${INSTR_COUNT_FILE} ${PY_REQUIREMENTS} ${CALC_EXEC_TIME_SCRIPT}
    )


    list(APPEND TEST_RESULTS ${EXEC_TIME_CSV})


    ### Generate instruction count plot
    set(GENERATE_PLOT_ICOUNT_SCRIPT ${PROJECT_SOURCE_DIR}/scripts/generate_icount_plot.py)
    set(ICOUNT_PLOT ${RESULT_DIR}/${targetsource}-icount.png)
    set(PLOT_PATH ${RESULT_DIR}/)

    add_custom_command(OUTPUT ${ICOUNT_PLOT}
        COMMAND python3 ${GENERATE_PLOT_ICOUNT_SCRIPT} ${targetsource} ${PLOT_PATH} < ${INSTR_COUNT_FILE}
        DEPENDS ${INSTR_COUNT_FILE} ${PY_REQUIREMENTS} ${GENERATE_PLOT_ICOUNT_SCRIPT}
    )

    list(APPEND ICOUNT_PLOTS ${ICOUNT_PLOT})


    ### Generate instruction count proportion by type
    set(GENERATE_PLOT_IGROUP_SCRIPT ${PROJECT_SOURCE_DIR}/scripts/generate_igroup_plot.py)
    set(IGROUP_PLOT ${RESULT_DIR}/${targetsource}-igroup-percent.png)

    add_custom_command(OUTPUT ${IGROUP_PLOT}
        COMMAND python3 ${GENERATE_PLOT_IGROUP_SCRIPT} ${targetsource} ${PLOT_PATH} < ${INSTR_COUNT_FILE}
        DEPENDS ${INSTR_COUNT_FILE} ${PY_REQUIREMENTS} ${GENERATE_PLOT_IGROUP_SCRIPT}
    )

    list(APPEND IGROUP_PLOTS ${IGROUP_PLOT})


    ### Plot execution time for each case
    set(PLOT_EXEC_TIME_SCRIPT ${PROJECT_SOURCE_DIR}/scripts/plot_exec_time.py)
    set(EXEC_TIME_PLOT ${RESULT_DIR}/${targetsource}-exec-time.png)

    add_custom_command(OUTPUT ${EXEC_TIME_PLOT}
        COMMAND python3 ${PLOT_EXEC_TIME_SCRIPT} ${targetsource} ${PLOT_PATH} < ${INSTR_COUNT_FILE}
        DEPENDS ${INSTR_COUNT_FILE} ${PY_REQUIREMENTS} ${PLOT_EXEC_TIME_SCRIPT}
    )

    list(APPEND EXEC_TIME_PLOTS ${EXEC_TIME_PLOT})


    ### DEBUG
    #add_custom_target("objdump-${targetsource}" DEPENDS ${OBJDUMP_FILE})
    #add_custom_target("python-spike-cmd-${targetsource}" DEPENDS ${SPIKE_CMD_FILE})
    #add_custom_target("spike-log-${targetsource}" DEPENDS ${SPIKE_LOG_FILE})
    #add_custom_target("python-extract-instructions-${targetsource}" DEPENDS ${INSTR_COUNT_PATH})
endforeach(targetsourcefile ${SOURCE_FILES})


### Execution time results
set(RESULT_FILE ${RESULT_DIR}/result.csv)
set(ALL_PLOTS ${RESULT_DIR}/all-plots)

add_custom_command(OUTPUT ${RESULT_FILE}
    COMMAND cmake -E echo "test,count,cycles,time_us @200MHz" > ${RESULT_FILE}
    COMMAND cat ${TEST_RESULTS} >> ${RESULT_FILE}
    DEPENDS ${TEST_RESULTS}
)


### Plot execution time results
set(RISCV_EXEC_TIMES_PLOT ${RESULT_DIR}/riscv-exec-time-all.png)
set(PLOT_EXEC_TIME_ALL_SCRIPT ${PROJECT_SOURCE_DIR}/scripts/plot_all_exec_time.py)

add_custom_command(OUTPUT ${RISCV_EXEC_TIMES_PLOT}
    COMMAND python3 ${PLOT_EXEC_TIME_ALL_SCRIPT} ${RISCV_EXEC_TIMES_PLOT} < ${RESULT_FILE}
    DEPENDS ${PLOT_EXEC_TIME_ALL_SCRIPT} ${RESULT_FILE} ${PY_REQUIREMENTS}
)

### Plots
add_custom_command(OUTPUT ${ALL_PLOTS}
    DEPENDS ${ICOUNT_PLOTS} ${IGROUP_PLOTS} ${EXEC_TIME_PLOTS} ${RISCV_EXEC_TIMES_PLOT}
)


### Target which generates all results
add_custom_target(results
    DEPENDS ${RESULT_FILE} ${ALL_PLOTS}
)
