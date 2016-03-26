from lab18.Vasich.damerau_levenstein import distance
import unittest


class TestDLDistance(unittest.TestCase):

    def test_manual(self):
        self.assertEqual(distance("хотели как лучще", "получилось как всегда"), 14)
        self.assertEqual(distance("apple", "google"), 4)

        self.assertEqual(distance("Торбинс", "Сумникс"), 5)
        self.assertEqual(distance("Сумникс", "Бэггинс"), 5)
        self.assertEqual(distance("Бэггинс", "Беббинс"), 3)

        self.assertEqual(distance("казнить нельзя, помиловать", "казнить, нельзя помиловать"), 2)
        self.assertEqual(distance("хлеб", "пиво"), 4)