### Get proxy-kernel
set(PK_SRC_DIR ${PROJECT_BINARY_DIR}/pk)
set(PK_CONFIG_FLAGS --prefix=/opt/riscv/bin --host=riscv64-unknown-elf --with-arch=rv32imafdc --enable-fp-emulation)

ExternalProject_Add(pkproj
    GIT_REPOSITORY https://github.com/riscv-software-src/riscv-pk
    SOURCE_DIR ${PK_SRC_DIR}
    CONFIGURE_COMMAND "${PK_SRC_DIR}/configure" ${PK_CONFIG_FLAGS}
    BUILD_COMMAND ${MAKE}
    INSTALL_COMMAND cmake -E echo "Skipping install step."
)
ExternalProject_Get_Property(pkproj BINARY_DIR)

set(PK_BIN_DIR ${BINARY_DIR})

add_executable(pk_exe IMPORTED)
set_target_properties(pk_exe
    PROPERTIES 
    IMPORTED_LOCATION "${PK_BIN_DIR}/pk")

add_dependencies(pk_exe pkproj)
