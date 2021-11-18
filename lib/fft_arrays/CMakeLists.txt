# CMakeLists.txt file for fft_arrays library

add_library(fft_arrays src/fft_input_array.c)

target_include_directories(fft_arrays PUBLIC include)

target_compile_options(fft_arrays
PUBLIC
    -fdata-sections
    
PRIVATE
    -Wall
    -Wextra
    -Wshadow
    -Wdouble-promotion
    -Wconversion
    -fno-common
)
