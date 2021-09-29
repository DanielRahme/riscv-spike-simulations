
cmake_minimum_required(VERSION 3.20)

project(
    DistanceRiscvExample
    VERSION 0.1
    DESCRIPTION "Distance example in CMake"
    LANGUAGES C
    )

if(CMAKE_PROJECT_NAME STREQUAL PROJECT_NAME) 

     set(CMAKE_CXX_EXTENSIONS OFF)   # Let's nicely support folders in IDEs   
     set_property(GLOBAL PROPERTY USE_FOLDERS ON)   
     

     # Testing only available if this is the main app   # Note this needs to be done in the main CMakeLists   # since it calls enable_testing, which must be in the   # main CMakeLists.   

     include(CTest)   # Docs only available if this is the main app   

     find_package(Doxygen)   
     if(Doxygen_FOUND)  
         add_subdirectory(docs)   
     else()     
         message(STATUS "Doxygen not found, not building docs")   
     endif() 
 endif() 
 
 include(FetchContent)

 #if(${CMAKE_VERSION} VERSION_LESS 3.14)   
 #  include(cmake/add_FetchContent_MakeAvailable.cmake) 
 #endif()


# Fetch repo and add to build
#FetchContent_Declare(   
#   fmtlib
#   GIT_REPOSITORY https://github.com/fmtlib/fmt.git   
#   GIT_TAG 5.3.0) 
#FetchContent_MakeAvailable(fmtlib)


add_subdirectory(src)
add_subdirectory(apps)

if((CMAKE_PROJECT_NAME STREQUAL PROJECT_NAME OR MODERN_CMAKE_BUILD_TESTING)    
    AND BUILD_TESTING)   
    add_subdirectory(tests) 
endif()
