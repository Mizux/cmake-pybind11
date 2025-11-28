if(NOT BUILD_EXAMPLES)
  return()
endif()

add_cxx_example(
  NAME
    example
  SOURCES
    example.cpp
  LINK_LIBRARIES
    ${PROJECT_NAMESPACE}::Foo
    ${PROJECT_NAMESPACE}::Bar
    ${PROJECT_NAMESPACE}::FooBar
)

file(GLOB PYTHON_SRCS "*.py")
foreach(FILE_NAME IN LISTS PYTHON_SRCS)
  add_python_example(FILE_NAME ${FILE_NAME})
endforeach()
