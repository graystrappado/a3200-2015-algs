from lab9.Vasich.k_max_p1 import MinHeap
from lab9.Vasich.k_max_p2 import quickselect
from random import randint
import unittest


class TestMax(unittest.TestCase):
    def _check(self, input_arr, out_arr):
        input_arr.sort()
        answer = [input_arr[i] for i in range(len(input_arr) - len(out_arr), len(input_arr))]
        result = [out_arr[i] for i in range(len(out_arr))]

        result.sort()

        for i in range(0, len(result)):
            if answer[i] != result[i]:
                return False
        return True

    def test_random(self):
        size = 1000
        k = 20
        input_arr = [0] * size
        for i in range(size):
            input_arr[i] = randint(-1000, 1000)
        mh = MinHeap(20)
        for i in range(size):
            mh.push(input_arr[i])
        output_arr1 = mh.max_list()
        output_arr2 = quickselect(input_arr, 0, len(input_arr), k)

        self.assertTrue(self._check(input_arr, output_arr1))
        self.assertTrue(self._check(input_arr, output_arr2))

    def test_max(self):
        max_val = float("-inf")
        size = 1000
        k = 1
        input_arr = [0] * size

        for i in range(size):
            input_arr[i] = randint(-1000, 1000)
            if input_arr[i] > max_val:
                max_val = input_arr[i]

        mh = MinHeap(k)
        for i in range(size):
            mh.push(input_arr[i])
        output_arr1 = mh.max_list()
        output_arr2 = quickselect(input_arr, 0, len(input_arr), k)

        self.assertEqual(max_val, output_arr1[0])
        self.assertEqual(max_val, output_arr2[0])
