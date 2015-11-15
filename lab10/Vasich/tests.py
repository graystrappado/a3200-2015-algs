from lab10.Vasich.pythagorean_triples import triples
from random import randint

import unittest


class TestTriples(unittest.TestCase):
    def _check(self, input_arr, out_value):
        work_copy = [input_arr[i] ** 2 for i in range(len(input_arr))]
        work_copy.sort()
        arr = [work_copy[0]]

        j = 0
        for i in range(1, len(work_copy)):
            value = work_copy[i]
            if arr[j] != value:
                arr.append(value)
                j += 1

        count = 0
        for i in range(len(arr) - 1, -1, -1):
            for j in range(i - 1, -1, -1):
                for k in range(j - 1, -1, -1):
                    if arr[i] == arr[j] + arr[k]:
                        count += 1
        return count == out_value

    def test_egypt(self):
        input_arr = [3, 4, 5]
        self.assertEqual(1, triples(input_arr))

    def test_manual1(self):
        input_arr = [20, 21, 29, 12, 16, 3]
        self.assertEqual(2, triples(input_arr))

    def test_manual2(self):
        input_arr = [23, 247, 19, 96, 264, 265, 132, 181]
        self.assertEqual(2, triples(input_arr))

    def test_manual3(self):
        input_arr = [12, 15, 24, 27, 40, 1, 42]
        self.assertEqual(0, triples(input_arr))

    def test_random(self):
        size = 500
        input_arr = [0] * size
        for i in range(size):
            input_arr[i] = randint(0, 1000)
        self.assertTrue(self._check(input_arr, triples(input_arr)))
