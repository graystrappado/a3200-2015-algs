from lab11.Vasich.bar_chart import chart_area

import unittest


class TestBarChart(unittest.TestCase):
    def test_empty_chart(self):
        self.assertEqual(0, chart_area([]))

    def test_plane(self):
        self.assertEqual(0, chart_area([2, 2, 2, 2, 2]))

    def test_ascending(self):
        self.assertEqual(0, chart_area([2, 3, 5, 8, 11]))

    def test_descending(self):
        self.assertEqual(0, chart_area([52, 43, 35, 28, 11]))

    def test_castle_wall(self):
        self.assertEqual(1, chart_area([1, 2, 1, 2, 1, 2, 1, 2]))

    def test_mount_elbrus(self):
        self.assertEqual(25, chart_area([1, 2, 4, 8, 16, 6, 6, 8, 15, 7, 6, 7, 0]))
