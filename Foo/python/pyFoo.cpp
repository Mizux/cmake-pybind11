#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <foo/Foo.hpp>

namespace py = pybind11;

PYBIND11_MODULE(pyFoo, m) {
    m.doc() = "pyFoo module"; // optional module docstring

    // Free function
    // Vector of String
    m.def("string_vector_output", &::foo::stringVectorOutput, "A function that return a vector of string.");
    m.def("string_vector_input", &::foo::stringVectorInput, "A function that use a vector of string.");
    m.def("string_vector_ref_input", &::foo::stringVectorInput, "A function that use a vector of string const ref.");

    // Vector of Vector of String
    m.def("string_jagged_array_output", &::foo::stringJaggedArrayOutput, "A function that return a jagged array of string.");
    m.def("string_jagged_array_input", &::foo::stringJaggedArrayInput, "A function that use a jagged array of string.");
    m.def("string_jagged_array_ref_input", &::foo::stringJaggedArrayRefInput, "A function that use a jagged array of string const ref.");

    // Vector of Pair
    m.def("pair_vectorOutput", &::foo::pairVectorOutput, "A function that return a vector of pair.");
    m.def("pair_vectorInput", &::foo::pairVectorInput, "A function that use a vector of pair.");
    m.def("pair_vectorRefInput", &::foo::pairVectorRefInput, "A function that use a vector of pair const ref.");

    // Vector of Vector of Pair
    m.def("pair_jagged_array_output", &::foo::pairJaggedArrayOutput, "A function that return a jagged array of pair.");
    m.def("pair_jagged_array_input", &::foo::pairJaggedArrayInput, "A function that use a jagged array of pair.");
    m.def("pair_jagged_array_ref_input", &::foo::pairJaggedArrayRefInput, "A function that use a jagged array of pair const ref.");

    // Free Function
    m.def("free_function", &::foo::pairJaggedArrayOutput, "A function that return a jagged array of pair.");
    m.def("free_function", &::foo::pairJaggedArrayInput, "A function that use a jagged array of pair.");

    // Class Foo
    py::class_<::foo::Foo>(m, "Foo")
      .def(py::init<>())
      .def_static("static_function", py::overload_cast<int>(&::foo::Foo::staticFunction))
      .def_static("static_function", py::overload_cast<int64_t>(&::foo::Foo::staticFunction))
      .def_property("int", &::foo::Foo::getInt, &::foo::Foo::setInt, py::return_value_policy::copy)
      .def_property("int64", &::foo::Foo::getInt64, &::foo::Foo::setInt64, py::return_value_policy::copy)
      .def("__str__", &::foo::Foo::operator());
}
