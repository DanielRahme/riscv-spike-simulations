### CMakeLists.txt for external libraries
include(FetchContent)

FetchContent_Declare(   
    cmsis-dsp-lib   
    GIT_REPOSITORY https://github.com/DanielRahme/CMSIS-DSP-PULPino
    )
FetchContent_MakeAvailable(cmsis-dsp-lib)
