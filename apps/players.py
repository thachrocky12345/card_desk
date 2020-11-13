from deck import DeckEmptied


class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        card = deck.draw_card()
        if card:
            self.hand.append(card)
        else:
            raise DeckEmptied("Deck emptied")

    @property
    def hand_score(self):
        return sum([card.color_point for card in self.hand])

    def show_hand(self):
        for card in self.hand:
            card.show()