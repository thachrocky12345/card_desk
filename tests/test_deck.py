import unittest
from apps.deck import Deck, DeckEmptied, Card
from apps.config import Color

class DeckTest(unittest.TestCase):
    def test_deck_build(self):
        deck = Deck(5)
        self.assertEqual(len(deck.cards), (5-1) * 3)

    def test_draw_card(self):
        deck = Deck(3)
        card = deck.draw_card()
        self.assertEqual(card.value, 1)
        self.assertEqual(card.color.name, "red")
        self.assertEqual(card.color.value, 3)

    def test_assert_raise_deck_emptied(self):
        deck = Deck(2)
        card = deck.draw_card()
        card = deck.draw_card()
        card = deck.draw_card()
        try:
            card = deck.draw_card()
        except DeckEmptied:
            pass
        self.assertRaises(DeckEmptied, deck.draw_card)

    def test_desk_shuffle(self):
        deck1 = Deck(3)
        deck2 = Deck(3)
        self.assertEqual(tuple([(card.color, card.value) for card in deck1.cards]),
                         tuple([(card.color, card.value) for card in deck2.cards]))
        deck2.shuffle()
        self.assertNotEqual(tuple([(card.color, card.value) for card in deck1.cards]),
                            tuple([(card.color, card.value) for card in deck2.cards]))

    def test_sorted_card(self):
        deck = Deck(2)
        # emptied the card and create modified ones
        # (red, 1), (green, 5), (red, 0), (yellow, 3), (green, 2)
        # ([yellow, green, red]) -> (yellow, 3), (green, 2), (green, 5), (red, 0), (red, 1) 
        deck.cards = [Card(Color.red, 1),
                      Card(Color.green, 5),
                      Card(Color.red, 0),
                      Card(Color.yellow, 3),
                      Card(Color.green, 2)]
        deck.sort_cards(["green", "red", "yellow"])
        self.assertEqual(tuple([(Color.green, 2), (Color.green, 5),
                                (Color.red, 0), (Color.red, 1), (Color.yellow, 3)
                                ]),
                         tuple([(card.color, card.value) for card in deck.cards]))

        deck.sort_cards(["yellow", "green", "red"])
        self.assertEqual(tuple([(Color.yellow, 3), (Color.green, 2), (Color.green, 5),
                                (Color.red, 0), (Color.red, 1)
                                ]),
                         tuple([(card.color, card.value) for card in deck.cards]))




