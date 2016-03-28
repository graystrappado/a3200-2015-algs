from lab19.Vasich.palindrome import palindrome
import unittest
from itertools import accumulate
from random import choice
import string
import operator


class TestPalindrome(unittest.TestCase):

    def test_better(self):
        number_of_tests = 10 ** 3
        printables = list(string.printable)

        for length in accumulate(range(1, 7), operator.mul):           # PAL: [p] + P_MIDDLE + [p]
            for _ in range(number_of_tests):                           # LINE: LEFT + [p] + MIDDLE + [p] + RIGHT
                line = [choice(printables) for _ in range(length)]     # if LEFT and RIGHT intersect at y
                pal = palindrome("".join(line))                        # there is a bigger palindrome [y] + PAL + [y]
                len_p = len(pal)
                if len_p == 1:
                    self.assertTrue(len(set(line)) == len(line) and pal[0] == line[0])
                    continue
                for p in pal[0: len_p // 2 + len_p % 2]:
                    idx_left, idx_right = line.index(p), len(line) - line[::-1].index(p) - 1
                    left, line, right = line[: idx_left], line[idx_left + 1: idx_right], line[idx_right + 1:]
                    self.assertTrue(set(left).isdisjoint(set(right)))
            print("length {} passed".format(length))
