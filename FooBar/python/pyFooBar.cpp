#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <foobar/FooBar.hpp>

namespace py = pybind11;

PYBIND11_MODULE(pyFooBar, m) {
    m.doc() = "pyFooBar module"; // optional module docstring

    // Free function
    // Vector of String
    m.def("string_vector_output", &::foobar::stringVectorOutput, "A function that return a vector of string.");
    m.def("string_vector_input", &::foobar::stringVectorInput, "A function that use a vector of string.");
    m.def("string_vector_ref_input", &::foobar::stringVectorInput, "A function that use a vector of string const ref.");

    // Vector of Vector of String
    m.def("string_jagged_array_output", &::foobar::stringJaggedArrayOutput, "A function that return a jagged array of string.");
    m.def("string_jagged_array_input", &::foobar::stringJaggedArrayInput, "A function that use a jagged array of string.");
    m.def("string_jagged_array_ref_input", &::foobar::stringJaggedArrayRefInput, "A function that use a jagged array of string const ref.");

    // Vector of Pair
    m.def("pair_vectorOutput", &::foobar::pairVectorOutput, "A function that return a vector of pair.");
    m.def("pair_vectorInput", &::foobar::pairVectorInput, "A function that use a vector of pair.");
    m.def("pair_vectorRefInput", &::foobar::pairVectorRefInput, "A function that use a vector of pair const ref.");

    // Vector of Vector of Pair
    m.def("pair_jagged_array_output", &::foobar::pairJaggedArrayOutput, "A function that return a jagged array of pair.");
    m.def("pair_jagged_array_input", &::foobar::pairJaggedArrayInput, "A function that use a jagged array of pair.");
    m.def("pair_jagged_array_ref_input", &::foobar::pairJaggedArrayRefInput, "A function that use a jagged array of pair const ref.");

    // Free Function
    m.def("free_function", &::foobar::pairJaggedArrayOutput, "A function that return a jagged array of pair.");
    m.def("free_function", &::foobar::pairJaggedArrayInput, "A function that use a jagged array of pair.");

    // Class FooBar
    py::class_<::foobar::FooBar>(m, "FooBar")
      .def(py::init<>())
      .def_static("static_function", py::overload_cast<int>(&::foobar::FooBar::staticFunction))
      .def_static("static_function", py::overload_cast<int64_t>(&::foobar::FooBar::staticFunction))
      .def("get_int", &::foobar::FooBar::getInt)
      .def("set_bar_int", &::foobar::FooBar::setBarInt)
      .def("set_foo_int", &::foobar::FooBar::setFooInt)
      .def("get_int64", &::foobar::FooBar::getInt64)
      .def("set_bar_int64", &::foobar::FooBar::setBarInt64)
      .def("set_foo_int64", &::foobar::FooBar::setFooInt64)
      .def("__str__", &::foobar::FooBar::operator());
}
