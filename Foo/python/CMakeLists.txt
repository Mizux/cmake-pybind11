pybind11_add_module(pyFoo MODULE pyFoo.cpp)
# note: macOS is APPLE and also UNIX !
if(APPLE)
  set_target_properties(pyFoo PROPERTIES
    SUFFIX ".so"
    INSTALL_RPATH "@loader_path;@loader_path/../../${PYTHON_PROJECT}/.libs"
    )
  set_property(TARGET pyFoo APPEND PROPERTY
    LINK_FLAGS "-flat_namespace -undefined suppress"
    )
elseif(UNIX)
  set_target_properties(pyFoo PROPERTIES
    INSTALL_RPATH "$ORIGIN:$ORIGIN/../../${PYTHON_PROJECT}/.libs"
    )
endif()
target_link_libraries(pyFoo PRIVATE ${PROJECT_NAMESPACE}::Foo)
add_library(${PROJECT_NAMESPACE}::pyFoo ALIAS pyFoo)
