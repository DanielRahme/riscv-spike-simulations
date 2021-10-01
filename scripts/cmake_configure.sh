#!/bin/bash

echo "CMake configure"

#echo "cmake -S . -B build"
#cmake -S . -B build

echo "cmake -S . -DCMAKE_TOOLCHAIN_FILE=./cmake/riscv.cmake -DCMAKE_BUILD_TYPE=Release -B build"

# Build type Release is for -O3 optimization
cmake -S . -DCMAKE_TOOLCHAIN_FILE=./cmake/riscv.cmake -DCMAKE_BUILD_TYPE=Release -B build

