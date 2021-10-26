# CMakeLists file for apps/main executable

add_executable(main main.c)
target_compile_features(main PRIVATE c_std_99)

target_link_libraries(main PRIVATE distance_library riscv_cmsis_dsp_lib)
