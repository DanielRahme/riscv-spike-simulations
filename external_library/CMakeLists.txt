cmake_minimum_required(VERSION 3.20)
project(spikesim)

include(ExternalProject)

SET(SPIKE_SRC_DIR ${CMAKE_CURRENT_SOURCE_DIR}/spike)

ExternalProject_Add(spikeproj
    GIT_REPOSITORY https://github.com/riscv-software-src/riscv-isa-sim
    SOURCE_DIR ${SPIKE_SRC_DIR}
    CONFIGURE_COMMAND "${SPIKE_SRC_DIR}/configure" --prefix=/opt/riscv-spike
    BUILD_COMMAND ${MAKE}
)

ExternalProject_Get_Property(spikeproj BINARY_DIR)
SET(SPIKE_BIN_DIR ${BINARY_DIR})

add_executable(spike IMPORTED)
set_target_properties(spike 
    PROPERTIES 
    IMPORTED_LOCATION "${SPIKE_BIN_DIR}/spike")

add_dependencies(spike spikeproj)
