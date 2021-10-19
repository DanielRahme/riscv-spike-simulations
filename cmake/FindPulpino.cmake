### CMakeLists.txt for external libraries
include(FetchContent)

FetchContent_Declare(   
    pulpino-cmsis-dsp   
    GIT_REPOSITORY https://github.com/misaleh/pulpino
    SOURCE_SUBDIR  cmake
    )
FetchContent_MakeAvailable(pulpino-cmsis-dsp)
