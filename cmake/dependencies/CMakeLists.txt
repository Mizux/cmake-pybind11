# ##############################################################################
# SWIG (WIN32)
# ##############################################################################
if(WIN32)
  message(CHECK_START "Fetching SWIG")
  list(APPEND CMAKE_MESSAGE_INDENT "  ")
  # Download and unpack swig at configure time
  configure_file(${CMAKE_CURRENT_LIST_DIR}/CMakeLists.txt.swig swig-download/CMakeLists.txt)
  execute_process(COMMAND ${CMAKE_COMMAND} -G "${CMAKE_GENERATOR}" .
    RESULT_VARIABLE result
    WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/swig-download )
  if(result)
    message(FATAL_ERROR "CMake step for swig failed: ${result}")
  endif()
  execute_process(COMMAND ${CMAKE_COMMAND} --build .
    RESULT_VARIABLE result
    WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/swig-download )
  if(result)
    message(FATAL_ERROR "Build step for swig failed: ${result}")
  endif()

  # Define SWIG_EXECUTABLE (used as "hint" by FindSWIG)
  set(SWIG_EXECUTABLE ${CMAKE_BINARY_DIR}/swig/swig.exe)
  list(POP_BACK CMAKE_MESSAGE_INDENT)
  message(CHECK_PASS "fetched")
endif()

include(FetchContent)
set(FETCHCONTENT_QUIET OFF)
set(FETCHCONTENT_UPDATES_DISCONNECTED ON)
set(BUILD_SHARED_LIBS OFF)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)
set(BUILD_TESTING OFF)

# ##############################################################################
# pybind11
# ##############################################################################
if(BUILD_pybind11)
  message(CHECK_START "Fetching pybind11")
  list(APPEND CMAKE_MESSAGE_INDENT "  ")
  set(PYBIND11_INSTALL ON)
  set(PYBIND11_TEST OFF)
  FetchContent_Declare(
    pybind11
    GIT_REPOSITORY "https://github.com/pybind/pybind11.git"
    GIT_TAG "v2.9.1"
    #PATCH_COMMAND git apply --ignore-whitespace "${CMAKE_CURRENT_LIST_DIR}/../../patches/pybind11-2.9.1.patch"
  )
  FetchContent_MakeAvailable(pybind11)
  list(POP_BACK CMAKE_MESSAGE_INDENT)
  message(CHECK_PASS "fetched")
endif()
