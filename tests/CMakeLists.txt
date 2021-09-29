
add_executable(test_dist test_dist.c)

target_compile_features(test_dist PRIVATE c_std_99)

target_link_libraries(test_dist PRIVATE distance_library)

add_test(NAME test_dist_test COMMAND test_dist)
