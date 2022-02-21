#!/usr/bin/env python3
'''Test APIs'''

import unittest
import cmakepybind11
from cmakepybind11.foo import pyFoo
#import cmakepybind11.foo.pyFoo as foo

if __debug__:
    print(f'version: {cmakepybind11.__version__}')
    print(f'cmakepybind11: ${dir(cmakepybind11)}')
    print(f'cmakepybind11.foo: ${dir(cmakepybind11.foo)}')
    print(f'pyFoo: ${dir(pyFoo)}')


class TestpyFoo(unittest.TestCase):
    '''Test pyFoo'''
    def test_free_function(self):
        pyFoo.free_function(2147483647)  # max int
        pyFoo.free_function(2147483647 + 1)  # max int + 1

    def test_string_vector(self):
        self.assertEqual(4, pyFoo.string_vector_input(["1", "2", "3", "4"]))

        self.assertEqual(
            5, pyFoo.string_vector_ref_input(["1", "2", "3", "4", "5"]))

        res = pyFoo.string_vector_output(3)
        if __debug__:
            print(f"res: {res}")
        self.assertEqual(3, len(res))

    def test_string_jagged_array(self):
        self.assertEqual(
            3,
            pyFoo.string_jagged_array_input([['1'], ['2', '3'],
                                             ['4', '5', '6']]))

        self.assertEqual(
            4,
            pyFoo.string_jagged_array_ref_input([['1'], ['2', '3'],
                                                 ['4', '5', '6'], ['7']]))

        v = pyFoo.string_jagged_array_output(5)
        self.assertEqual(5, len(v))
        for i in range(5):
            self.assertEqual(i + 1, len(v[i]))

    def test_pair_vector(self):
        self.assertEqual(3, pyFoo.pair_vector_input([(1, 2), (3, 4), (5, 6)]))

        self.assertEqual(3,
                         pyFoo.pair_vector_ref_input([(1, 2), (3, 4), (5, 6)]))

        res = pyFoo.pair_vector_output(3)
        if __debug__:
            print(f"res: {res}")
        self.assertEqual(3, len(res))

    def test_pair_jagged_array(self):
        self.assertEqual(
            2, pyFoo.pair_jagged_array_input([[(1, 1)], [(2, 2), (2, 2)]]))

        self.assertEqual(
            2, pyFoo.pair_jagged_array_ref_input([[(1, 1)], [(2, 2), (2, 2)]]))

        res = pyFoo.pair_jagged_array_output(5)
        if __debug__:
            print(f"res: {res}")
        self.assertEqual(5, len(res))
        for i in range(5):
            self.assertEqual(i + 1, len(res[i]))

    def test_pyFoo_static_methods(self):
        f = pyFoo.Foo()
        if __debug__:
            print(f'class Foo: ${dir(f)}')
        f.static_function(1)
        f.static_function(2147483647)
        f.static_function(2147483647 + 1)

    def test_pyFoo_int_methods(self):
        f = pyFoo.Foo()
        f.int = 13
        self.assertEqual(13, f.int)
        f.int = 17
        self.assertEqual(17, f.int)

    def test_pyFoo_int64_methods(self):
        f = pyFoo.Foo()
        f.int64 = 31
        self.assertEqual(31, f.int64)
        f.int64 = 42
        self.assertEqual(42, f.int64)


if __name__ == '__main__':
    unittest.main(verbosity=2)
