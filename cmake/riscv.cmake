# usage
# cmake -DCMAKE_TOOLCHAIN_FILE=../cmake/riscv.cmake ../

find_program(RISCV_GCC riscv64-unknown-elf-gcc)
find_program(RISCV_AR riscv64-unknown-elf-ar)
find_program(RISCV_GPP riscv64-unknown-elf-g++)
find_program(RISCV_OBJDUMP riscv64-unknown-elf-objdump)
find_program(RISCV_OBJCOPY riscv64-unknown-elf-objcopy)
message( "RISC-V GCC found: ${RISCV_GCC}")
message( "RISC-V AR found: ${RISCV_AR}")
message( "RISC-V G++ found: ${RISCV_GPP}")
message( "RISC-V objdump found: ${RISCV_OBJDUMP}")
message( "RISC-V objcopy found: ${RISCV_OBJCOPY}")

# The Generic system name is used for embedded targets (targets without OS) in
# CMake
set( CMAKE_SYSTEM_NAME          Generic )
set( CMAKE_SYSTEM_PROCESSOR     rv32imfc )
set( CMAKE_EXECUTABLE_SUFFIX    ".elf")
set(MABI ilp32f)


set(CMAKE_ASM_COMPILER ${RISCV_GCC})
set(CMAKE_AR ${RISCV_AR})
set(CMAKE_ASM_COMPILER ${RISCV_GCC})
set(CMAKE_C_COMPILER ${RISCV_GCC})
set(CMAKE_CXX_COMPILER ${RISCV_GPP})
set(CMAKE_OBJCOPY ${RISCV_OBJCOPY})
set(CMAKE_OBJDUMP ${RISCV_OBJDUMP})

# Set the common build flags
# Set the CMAKE C flags (which should also be used by the assembler!
set( CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -g" )
set( CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -march=${CMAKE_SYSTEM_PROCESSOR}" )
set( CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -mabi=${MABI}" )

set( CMAKE_C_FLAGS "${CMAKE_C_FLAGS}" CACHE STRING "" )
set( CMAKE_CXX_FLAGS "${CMAKE_C_FLAGS}" CACHE STRING "" )
set( CMAKE_ASM_FLAGS "${CMAKE_C_FLAGS}" CACHE STRING "" )

# -nostartfiles is commented out because Spike simulator needs it to simulate.
#set( CMAKE_EXE_LINKER_FLAGS   "${CMAKE_EXE_LINKER_FLAGS}  -march=${CMAKE_SYSTEM_PROCESSOR}    -nostartfiles   " )
set( CMAKE_EXE_LINKER_FLAGS   "${CMAKE_EXE_LINKER_FLAGS}  -march=${CMAKE_SYSTEM_PROCESSOR}" )

