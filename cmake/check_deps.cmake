# CXX Test
if(BUILD_TESTING)
  if(NOT TARGET GTest::gtest)
    message(FATAL_ERROR "Target GTest::gtest not available.")
  endif()
  if(NOT TARGET GTest::gtest_main)
    message(FATAL_ERROR "Target GTest::gtest_main not available.")
  endif()
endif()
