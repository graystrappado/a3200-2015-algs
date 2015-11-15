from lab12.Vasich.tree import UnbalancedBinarySearchTree
from random import randint
import unittest


class TestQueue(unittest.TestCase):
    def _check(self, input_arr):
        tree = UnbalancedBinarySearchTree()

        for v in input_arr:
            tree.add(v)

        input_arr.sort()
        i = 0
        for p in tree:
            if p != input_arr[i]:
                return False
            i += 1
        return True

    def test_empty(self):
        self.assertTrue(self._check([]))

    def test_ascending(self):
        size = 100
        input_arr = [0] * size
        for i in range(1, size):
            input_arr[i] = input_arr[i - 1] + randint(1, 10)
        self.assertTrue(self._check(input_arr))

    def test_repeating_ascending(self):
        size = 100
        input_arr = [0] * size
        for i in range(size):
            input_arr[i] = input_arr[i - 1] + randint(0, 4)
        self.assertTrue(self._check(input_arr))

    def test_descending(self):
        size = 100
        input_arr = [randint(0, size)] * size
        for i in range(size):
            input_arr[i] = input_arr[i - 1] - randint(1, 10)
        self.assertTrue(self._check(input_arr))

    def test_random(self):
        size = 100
        input_arr = [0] * size
        for i in range(size):
            input_arr[i] = randint(-1000, 1000)
        self.assertTrue(self._check(input_arr))

    def test_contains(self):
        size = 100
        input_arr = [0] * size
        for i in range(size):
            input_arr[i] = randint(-1000, 1000)

        tree = UnbalancedBinarySearchTree()
        for v in input_arr:
            tree.add(v)

        value = input_arr[randint(0, size)]
        self.assertTrue(tree.contains(value))

    def test_contains1(self):
        size = 100
        input_arr = [0] * size
        for i in range(size):
            input_arr[i] = randint(-1000, 1000)

        tree = UnbalancedBinarySearchTree()
        for v in input_arr:
            tree.add(v)

        value = 1001
        self.assertFalse(tree.contains(value))