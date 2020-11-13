import unittest
from apps.cards import Card
from apps.config import Color

class CardTest(unittest.TestCase):

    def test_red_color(self):
        card = Card(Color.red, 4)
        self.assertEqual(card.value, 4)
        self.assertEqual(card.color, Color.red)
        self.assertEqual(card.color.name, "red")
        self.assertEqual(card.color.value, 3)

    def test_yellow_color(self):
        card = Card(Color.yellow, 4)
        self.assertEqual(card.value, 4)
        self.assertEqual(card.color, Color.yellow)
        self.assertEqual(card.color.name, "yellow")
        self.assertEqual(card.color.value, 2)

    def test_green_color(self):
        card = Card(Color.green, 4)
        self.assertEqual(card.value, 4)
        self.assertEqual(card.color, Color.green)
        self.assertEqual(card.color.name, "green")
        self.assertEqual(card.color.value, 1)