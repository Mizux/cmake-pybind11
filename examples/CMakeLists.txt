if(NOT BUILD_EXAMPLES)
  return()
endif()

file(GLOB CPP_SRCS "*.cpp")
foreach(FILE_NAME IN LISTS CPP_SRCS)
  get_filename_component(NAME ${FILE_NAME} NAME_WE)
  add_cxx_example(
    NAME
      ${NAME}
    SOURCES
      ${FILE_NAME}
    LINK_LIBRARIES
      ${PROJECT_NAMESPACE}::Foo
      ${PROJECT_NAMESPACE}::Bar
      ${PROJECT_NAMESPACE}::FooBar
  )
endforeach()

file(GLOB PYTHON_SRCS "*.py")
foreach(FILE_NAME IN LISTS PYTHON_SRCS)
  add_python_example(${FILE_NAME})
endforeach()
