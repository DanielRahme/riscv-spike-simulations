# CMakeLists file for apps executables

### Add executables to MY_APPS list below to compile
set(MY_APPS
    main.c
    mat_mult.c
)

set(MY_LIBS
    distance_library
    riscv_cmsis_dsp_lib
)

set(C_FLAGS
    -O3
    #Warnings
    -Wall
    -Wextra
    -Wshadow
    -Wdouble-promotion
    -Wconversion
    -fno-common
    #Debug
    -ffunction-sections
    -fdata-sections
    #Memory
    -fstack-usage
    #Compile and linker
    -nostdlib
    -ffreestanding
    -flto
)

foreach(testsourcefile ${MY_APPS})
    #Simple string replace, to cut off .cpp.
    string(REPLACE ".c" "" testname ${testsourcefile})

    add_executable(${testname} ${testsourcefile})

    target_compile_features(${testname} PRIVATE c_std_99)
    target_link_options(${testname} PRIVATE -Wl,--gc-sections)
    target_link_libraries(${testname} PRIVATE ${MY_LIBS})
    target_compile_options(${testname} PRIVATE ${C_FLAGS})
endforeach(testsourcefile ${MY_APPS})
