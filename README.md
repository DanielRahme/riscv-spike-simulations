# Spike simulation of CMSIS DSP functions

>TODO: Project description....

## Getting started

This section will cover how to get started. What prerequisite tools are needed and how to build this project with CMake. 
> TODO: list of tools used

### Prerequisites
The [RISCV-V GNU toolchain](https://github.com/riscv-collab/riscv-gnu-toolchain) needs to be installed and configured with the architectures **rv32imafdc** and **rv32imfc**. The prefix is the location where the toolchain will be installed ``--prefix=/path/to/toolchain``.

    $ ./configure --prefix=/opt/riscv --enable-multilib --with-multilib-generator="rv32i-ilp32--; rv32imfc-ilp32f--; rv32imafdc-ilp32--"

Build and install after configuration. Might take some time so grab a coffee or two.

    $ make newlib -j8

> The rv32imafdc is for the proxy-kernel [riscv-pk](https://github.com/riscv-software-src/riscv-pk) and r32imfc is for the project. The architecture for the project (rv32imfc) can be changed by adding a new architecture to the toolchain and changing the cmake toolchain file ``/cmake/riscv.cmake``.

Add the toolchain to PATH. Store it in bashrc or zshrc to make it permanent.

    $ export PATH="opt/riscv/bin:$PATH"

Once exported to PATH this can be easily tested by the ``which`` command. 

    $ which riscv64-unknown-elf-gcc

### Setup

Create the build directory, configure and then build as seen below. The results will be in the ``/build/results`` folder.

    $ mkdir build
    $ cd build
    $ cmake -DCMAKE_TOOLCHAIN_FILE=../cmake/riscv.cmake ..
    $ make results VERBOSE=1 -j8

> For debugging use ``VERBOSE=1`` and to utilize n-number of cores use ``-jn``

If the required **Python libraries are missing** run the command:

    $ make python-install-libraries

