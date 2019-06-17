#!/usr/bin/python3

import unittest
from cs_clrs.ch2.merge_sort import merge_sort

class TestInsertionSort(unittest.TestCase):

    def test_normal(self):
        unsorted_arr = [5, 3, 7, 9, 10, 1, 2]
        sorted_arr = [1, 2, 3, 5, 7, 9, 10]
        self.assertEqual(sorted_arr, merge_sort(unsorted_arr))

    def test_one(self):
        self.assertEqual([1], merge_sort([1]))

    def test_none(self):
        self.assertEqual([], merge_sort([]))

if __name__ == '__main__':
    unittest.main()
