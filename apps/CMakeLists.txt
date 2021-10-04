# CMakeLists file for apps/main executable

add_executable(main main.c)
target_compile_features(main PRIVATE c_std_99)

target_link_libraries(main PRIVATE distance_library)

add_custom_command(TARGET main
    COMMAND riscv64-unknown-elf-objdump -D main > main.dump.txt
    COMMENT "Creat a objdump of main binary"
    DEPENDS main
    )
