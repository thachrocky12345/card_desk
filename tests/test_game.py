import unittest
from apps.cards import Card
from apps.config import Color
from apps.game import Game
from apps.deck import Deck

class TestGame(unittest.TestCase):

    def test_game(self):
        game = Game(["Thach", "Sean"])
        self.assertEqual(game.players[0].name, "Thach")
        self.assertEqual(game.players[1].name, "Sean")

    def test_find_winner(self):
        deck = Deck(2)
        game = Game(["Thach", "Sean"])
        deck.cards = [Card(Color.red, 1),
                      Card(Color.red, 2),
                      Card(Color.green, 1),
                      Card(Color.green, 2)]

        for turn in range(2):
            for player in game.players:
                player.draw(deck)

        winner = game.find_winner()
        self.assertEqual(winner.name, "Sean")

    def test_play(self):
        game = Game(["Thach", "Sean"])
        game.play()
        self.assertEqual(1, 1)
