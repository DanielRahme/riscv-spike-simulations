#!/bin/bash

echo "CMake configure"

#echo "cmake -S . -B build"
#cmake -S . -B build

echo "cmake -S . -DCMAKE_TOOLCHAIN_FILE=./cmake/riscv.cmake -B build"
cmake -S . -DCMAKE_TOOLCHAIN_FILE=./cmake/riscv.cmake -B build

