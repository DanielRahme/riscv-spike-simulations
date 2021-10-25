### Get Spike
set(SPIKE_SRC_DIR ${PROJECT_BINARY_DIR}/spike)

ExternalProject_Add(spikeproj
    GIT_REPOSITORY https://github.com/riscv-software-src/riscv-isa-sim
    SOURCE_DIR ${SPIKE_SRC_DIR}
    CONFIGURE_COMMAND "${SPIKE_SRC_DIR}/configure" --prefix=/opt/riscv-spike
    BUILD_COMMAND ${MAKE}
    INSTALL_COMMAND cmake -E echo "Skipping install step."
)
ExternalProject_Get_Property(spikeproj BINARY_DIR)


set(SPIKE_BIN_DIR ${BINARY_DIR})

add_executable(spike IMPORTED)
set_target_properties(spike 
    PROPERTIES 
    IMPORTED_LOCATION "${SPIKE_BIN_DIR}/spike")

add_dependencies(spike spikeproj)
