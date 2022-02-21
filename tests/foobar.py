#!/usr/bin/env python3
'''Test APIs'''

import unittest
import cmakepybind11
from cmakepybind11.foobar import pyFooBar
#import cmakepybind11.foobar.pyFooBar as foobar

if __debug__:
    print(f'version: {cmakepybind11.__version__}')
    print(f'cmakepybind11: ${dir(cmakepybind11)}')
    print(f'cmakepybind11.foobar: ${dir(cmakepybind11.foobar)}')
    print(f'pyFooBar: ${dir(pyFooBar)}')


class TestpyFooBar(unittest.TestCase):
    '''Test pyFooBar'''
    def test_free_function(self):
        pyFooBar.free_function(2147483647)  # max int
        pyFooBar.free_function(2147483647 + 1)  # max int + 1

    def test_string_vector(self):
        self.assertEqual(4, pyFooBar.string_vector_input(["1", "2", "3", "4"]))

        self.assertEqual(
            5, pyFooBar.string_vector_ref_input(["1", "2", "3", "4", "5"]))

        res = pyFooBar.string_vector_output(3)
        if __debug__:
            print(f"res: {res}")
        self.assertEqual(8, len(res))

    def test_string_jagged_array(self):
        self.assertEqual(
            3,
            pyFooBar.string_jagged_array_input([['1'], ['2', '3'],
                                                ['4', '5', '6']]))

        self.assertEqual(
            4,
            pyFooBar.string_jagged_array_ref_input([['1'], ['2', '3'],
                                                ['4', '5', '6'], ['7']]))

        v = pyFooBar.string_jagged_array_output(5)
        self.assertEqual(5, len(v))
        for i in range(5):
            self.assertEqual(i + 1, len(v[i]))

    def test_pair_vector(self):
        self.assertEqual(3, pyFooBar.pair_vector_input([(1, 2), (3, 4), (5, 6)]))

        self.assertEqual(3,
                         pyFooBar.pair_vector_ref_input([(1, 2), (3, 4), (5, 6)]))

        res = pyFooBar.pair_vector_output(3)
        if __debug__:
            print(f"res: {res}")
        self.assertEqual(8, len(res))

    def test_pair_jagged_array(self):
        self.assertEqual(
            2, pyFooBar.pair_jagged_array_input([[(1, 1)], [(2, 2), (2, 2)]]))

        self.assertEqual(
            2, pyFooBar.pair_jagged_array_ref_input([[(1, 1)], [(2, 2), (2, 2)]]))

        res = pyFooBar.pair_jagged_array_output(5)
        if __debug__:
            print(f"res: {res}")
        self.assertEqual(5, len(res))
        for i in range(5):
            self.assertEqual(i + 1, len(res[i]))

    def test_pyFooBar_static_methods(self):
        f = pyFooBar.FooBar()
        if __debug__:
            print(f'class FooBar: ${dir(f)}')
        f.static_function(1)
        f.static_function(2147483647)
        f.static_function(2147483647 + 1)

    def test_pyFooBar_int_methods(self):
        f = pyFooBar.FooBar()
        f.foo_int = 13
        f.bar_int = 17
        self.assertEqual(30, f.int)

    def test_pyFooBar_int64_methods(self):
        f = pyFooBar.FooBar()
        f.foo_int64 = 31
        f.bar_int64 = 37
        self.assertEqual(68, f.int64)


if __name__ == '__main__':
    unittest.main(verbosity=2)
