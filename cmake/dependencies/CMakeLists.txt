include(FetchContent)
set(FETCHCONTENT_QUIET OFF)
set(FETCHCONTENT_UPDATES_DISCONNECTED ON)
set(BUILD_SHARED_LIBS OFF)
set(CMAKE_POSITION_INDEPENDENT_CODE ON)
set(BUILD_TESTING OFF)

# ##############################################################################
# pybind11
# ##############################################################################
# Find Python 3
find_package(Python3 REQUIRED COMPONENTS Interpreter Development.Module)

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
