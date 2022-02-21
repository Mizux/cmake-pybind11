#!/usr/bin/env python3
'''Test APIs'''

import unittest
import cmakepybind11
from cmakepybind11.bar import pyBar
#import cmakepybind11.bar.pyBar as bar

if __debug__:
    print(f'version: {cmakepybind11.__version__}')
    print(f'cmakepybind11: ${dir(cmakepybind11)}')
    print(f'cmakepybind11.bar: ${dir(cmakepybind11.bar)}')
    print(f'pyBar: ${dir(pyBar)}')


class TestpyBar(unittest.TestCase):
    '''Test pyBar'''
    def test_free_function(self):
        pyBar.free_function(2147483647) # max int
        pyBar.free_function(2147483647+1) # max int + 1

    def test_string_vector(self):
        self.assertEqual(4, pyBar.string_vector_input(["1", "2", "3", "4"]))

        self.assertEqual(
            5, pyBar.string_vector_ref_input(["1", "2", "3", "4", "5"]))

        res = pyBar.string_vector_output(3)
        if __debug__:
            print(f"res: {res}")
        self.assertEqual(3, len(res))

    def test_string_jagged_array(self):
        self.assertEqual(
            3,
            pyBar.string_jagged_array_input([['1'], ['2', '3'],
                                             ['4', '5', '6']]))

        self.assertEqual(
            4,
            pyBar.string_jagged_array_ref_input([['1'], ['2', '3'],
                                                 ['4', '5', '6'], ['7']]))

        v = pyBar.string_jagged_array_output(5)
        self.assertEqual(5, len(v))
        for i in range(5):
            self.assertEqual(i + 1, len(v[i]))

    def test_pair_vector(self):
        self.assertEqual(3, pyBar.pair_vector_input([(1, 2), (3, 4), (5, 6)]))

        self.assertEqual(3,
                         pyBar.pair_vector_ref_input([(1, 2), (3, 4), (5, 6)]))

        res = pyBar.pair_vector_output(3)
        if __debug__:
            print(f"res: {res}")
        self.assertEqual(3, len(res))

    def test_pair_jagged_array(self):
        self.assertEqual(
            2, pyBar.pair_jagged_array_input([[(1, 1)], [(2, 2), (2, 2)]]))

        self.assertEqual(
            2, pyBar.pair_jagged_array_ref_input([[(1, 1)], [(2, 2), (2, 2)]]))

        res = pyBar.pair_jagged_array_output(5)
        if __debug__:
            print(f"res: {res}")
        self.assertEqual(5, len(res))
        for i in range(5):
            self.assertEqual(i + 1, len(res[i]))

    def test_pyBar_static_methods(self):
        f = pyBar.Bar()
        if __debug__:
            print(f'class Bar: ${dir(f)}')
        f.static_function(1)
        f.static_function(2147483647)
        f.static_function(2147483647 + 1)

    def test_pyBar_int_methods(self):
        f = pyBar.Bar()
        f.int = 13
        self.assertEqual(f.int, 13)
        f.int = 17
        self.assertEqual(f.int, 17)

    def test_pyBar_int64_methods(self):
        f = pyBar.Bar()
        f.int64 = 31
        self.assertEqual(f.int64, 31)
        f.int64 = 42
        self.assertEqual(f.int64, 42)


if __name__ == '__main__':
    unittest.main(verbosity=2)
