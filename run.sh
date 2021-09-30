#!/bin/bash

echo "[1/2] Configure the build"
./scripts/cmake_configure.sh

echo "[2/2] Build"
./scripts/cmake_build.sh

