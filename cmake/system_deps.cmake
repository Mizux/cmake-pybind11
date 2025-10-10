# Check dependencies
set(CMAKE_THREAD_PREFER_PTHREAD TRUE)
set(THREAD_PREFER_PTHREAD_FLAG TRUE)
find_package(Threads REQUIRED)

# Tell find_package() to try “Config” mode before “Module” mode if no mode was specified.
# This should avoid find_package() to first find our FindXXX.cmake modules if
# distro package already provide a CMake config file...
set(CMAKE_FIND_PACKAGE_PREFER_CONFIG TRUE)

if(NOT BUILD_pybind11)
  find_package(pybind11 REQUIRED)
endif()

# CXX Test
if(BUILD_TESTING)
  if(NOT BUILD_googletest AND NOT TARGET GTest::gtest_main)
    find_package(GTest REQUIRED)
  endif()
endif()
