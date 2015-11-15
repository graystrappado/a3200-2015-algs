from random import randint
from lab6.Vasich.radix_sort import radix_sort
import unittest


class TestSorting(unittest.TestCase):

    def _check(self, seq):
        if len(seq) <= 1:
            return True
        i = 1
        while i < len(seq):
            if seq[i - 1] > seq[i]:
                return False
            i += 1

        return True

    def test_trivial(self):
        seq = [1, 333, 22]
        res = radix_sort(seq)
        expected = [1, 22, 333]

        self.assertEqual(expected, res)

    def test_empty(self):
        seq = []
        res = radix_sort(seq)
        expected = []
        self.assertEqual(expected, res)

    def test_ascending(self):
        size = 100000
        seq = [0] * size
        for i in range(1, size):
            seq[i] = seq[i - 1] + randint(1, 10)
        radix_sort(seq)
        self.assertTrue(self._check(seq))

    def test_repeating_ascending(self):
        size = 100000
        seq = [0] * size
        for i in range(1, size):
            seq[i] = seq[i - 1] + randint(0, 4)
        radix_sort(seq)
        self.assertTrue(self._check(seq))

    def test_descending(self):
        size = 100000
        seq = [randint(0, size)] * size
        for i in range(size):
            seq[i] = seq[i - 1] - randint(1, 10)
        radix_sort(seq)
        self.assertTrue(self._check(seq))

    def test_positive_random(self):
        size = 100000
        seq = [0] * size
        for i in range(size):
            seq[i] = randint(0, 100000)
        radix_sort(seq)
        self.assertTrue(self._check(seq))

    def test_positive_and_negative_random(self):
        size = 100000
        seq = [0] * size
        for i in range(size):
            seq[i] = randint(-100000, 100000)
        radix_sort(seq)
        self.assertTrue(self._check(seq))
