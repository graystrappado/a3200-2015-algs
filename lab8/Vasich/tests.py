from lab8.Vasich.queue import parse_line, MaxElementQueue
from random import randint
import unittest


class TestQueue(unittest.TestCase):
    def _check(self, commands, expected_out, queue):
        size = len(commands)
        for i in range(size):
            self.assertEqual(expected_out[i], parse_line(commands[i], queue))

    def test_empty(self):
        queue = MaxElementQueue()
        strings = ["max", "max", "pop"]
        ans = ["empty", "empty", "empty"]
        self._check(strings, ans, queue)

    def test_pops(self):
        queue = MaxElementQueue()
        self.assertEqual("empty", queue.pop())

        count = 500
        first = randint(-100, 100)
        queue.push(first)
        for _ in range(count):
            queue.push(randint(-100, 100))
        self.assertEqual(first, queue.pop())

        for _ in range(count):
            queue.pop()
        self.assertEqual("empty", queue.pop())

    def test_manual(self):
        queue = MaxElementQueue()
        strings = ["push 3", "push 14", "push 15", "push 3", "push 14", "push 15", "max", "push 28", "push 18",
                   "push 7", "push 2", "pop", "pop", "pop", "max", "push 42", "max", "pop", "max", "pop", "pop", "pop",
                   "pop", "pop", "max", "pop", "pop", "max", "pop", "pop", "push 30", "max", "pop"]
        ans = ["ok", "ok", "ok", "ok", "ok", "ok", "15", "ok", "ok", "ok", "ok", "3", "14", "15", "28", "ok", "42", "3",
               "42", "14", "15", "28", "18", "7", "42", "2", "42", "empty", "empty", "empty", "ok", "30", "30"]
        self._check(strings, ans, queue)
