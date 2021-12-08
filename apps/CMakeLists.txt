# CMakeLists file for apps executables

### Add executables to SOURCE_FILES list below to compile and simulate
set(SOURCE_FILES
    cfft_f32_64.c
    cfft_f32_128.c
    cfft_f32_256.c
    cfft_f32_512.c
    cfft_f32_1024.c
    cfft_f32_2048.c
    cfft_f32_4096.c
    rfft_q15_64.c
    rfft_q15_128.c
    rfft_q15_256.c
    rfft_q15_512.c
    rfft_q15_1024.c
    rfft_q15_2048.c
    rfft_q15_4096.c
    rfft_q15_8192.c
    rfft_f32_64.c
    rfft_f32_128.c
    rfft_f32_256.c
    rfft_f32_512.c
    rfft_f32_1024.c
    rfft_f32_2048.c
    rfft_f32_4096.c
    rfft_q31_64.c
    rfft_q31_128.c
    rfft_q31_256.c
    rfft_q31_512.c
    rfft_q31_1024.c
    rfft_q31_2048.c
    rfft_q31_4096.c
    rfft_q31_8192.c
    CACHE INTERNAL ""
)

set(MY_LIBS
    riscv_cmsis_dsp_lib
    fft_arrays
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

foreach(testsourcefile ${SOURCE_FILES})
    #Simple string replace, to cut off .cpp.
    string(REPLACE ".c" "" testname ${testsourcefile})

    add_executable(${testname} ${testsourcefile})

    target_compile_features(${testname} PRIVATE c_std_99)
    target_link_options(${testname} PRIVATE -Wl,--gc-sections)
    target_link_libraries(${testname} PRIVATE ${MY_LIBS})
    target_compile_options(${testname} PRIVATE ${C_FLAGS})
endforeach(testsourcefile ${SOURCE_FILES})
