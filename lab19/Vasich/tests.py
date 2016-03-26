from lab19.Vasich.palindrome import palindrome
import unittest
from random import choice, sample, randrange, shuffle, randint, getrandbits
from itertools import chain
import string


class TestPalindrome(unittest.TestCase):

    def test_random(self):
        base_chars = list(chain(string.ascii_letters, string.digits, string.punctuation))

        max_half_length = 3 * 10 ** 1
        number_of_tests = 10 ** 3

        for _ in range(number_of_tests):
            pal = []
            s = []
            half_length = randint(1, max_half_length)
            middle = half_length
            shuffle(base_chars)
            pal_alph, mix_alph = base_chars[:half_length], base_chars[half_length:]

            for _ in range(half_length):
                pal.append(choice(pal_alph))
            pal.extend(pal[:: -1])
            s.extend(pal)
            center = ""

            for ch in sample(mix_alph, randrange(len(mix_alph))):
                idx = randrange(len(s))
                if idx == middle:
                    center = ch
                s.insert(idx, ch)
                middle += idx < middle
            pal.insert(half_length, center)
            pal = "".join(pal)
            s = "".join(s)
            self.assertEqual(pal, palindrome(s))
