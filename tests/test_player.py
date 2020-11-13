import unittest
from apps.deck import Deck, DeckEmptied, Card
from apps.players import Player


class PlayerTest(unittest.TestCase):

    def test_player(self):
        player = Player("Thach")
        self.assertEqual(player.name, "Thach")

    def test_draw_card(self):
        player = Player("Thach")
        deck = Deck(3)
        player.draw(deck)
        card = player.hand[0]
        self.assertEqual(card.value, 1)
        self.assertEqual(card.color.name, "red")
        self.assertEqual(card.color.value, 3)
        self.assertEqual(player.hand_score, 1*3)

