# CMakeLists file for src

add_library(distance_library distance.c)

target_include_directories(distance_library PUBLIC ../include/distance)

# Dependency libraries here
# The "m" is math.h
target_link_libraries(distance_library PRIVATE m)

target_compile_features(distance_library PUBLIC c_std_99)

target_compile_options(distance_library PUBLIC 
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
    )
