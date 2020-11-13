from config import Color, NUMBER_VALUE_FOR_EACH_COLOR
from cards import Card
import random

class DeckEmptied(Exception):
    pass


class Deck(object):
    def __init__(self, size=NUMBER_VALUE_FOR_EACH_COLOR):
        self.value_each_color = size
        self.cards = []
        self.build()

    def build(self):
        for color in [Color.red, Color.yellow, Color.green]:
            for value in range(1, self.value_each_color):
                self.cards.append(Card(color, value))

    def show(self):
        for card in self.cards:
            card.show()

    def shuffle(self):
        for index in range(len(self.cards)):
            r = random.randint(0, index)
            self.cards[index], self.cards[r] = self.cards[r], self.cards[index]

    def draw_card(self):
        if len(self.cards) > 0:
            return self.cards.pop(0)
        else:
            raise DeckEmptied("Card is out")

    def sort_cards(self, orders=["yellow", "red", "green"]):
        color1 = []
        color2 = []
        color3 = []
        for card in self.cards:
            if card.color.name == orders[0].lower():
                color1.append(card)
            elif card.color.name == orders[1].lower():
                color2.append(card)
            elif card.color.name == orders[2].lower():
                color3.append(card)
        self.cards = sorted(color1, key=lambda card: card.value) \
                        + sorted(color2, key=lambda card: card.value) \
                        + sorted(color3, key=lambda card: card.value)
        self.show()


if __name__ == "__main__":
    deck = Deck()
    deck.sort_cards(["green", "red", "yellow"])

