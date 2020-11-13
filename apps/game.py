from players import Player
from deck import Deck, DeckEmptied


class Game(object):
    def __init__(self, players):
        self.players = [Player(name) for name in players]

    def play(self, cards=3):
        deck = Deck()
        self.distribute_cards(cards, deck)
        winner = self.find_winner()
        print("{} is the winner with scores: {}".format(winner.name, winner.hand_score))
        for player in self.players:
            print("{}'s hand:".format(player.name))
            player.show_hand()
            print("")
        return winner

    def find_winner(self):
        sorted_winners = sorted(self.players, key=lambda player: player.hand_score, reverse=True)
        return sorted_winners[0]

    def distribute_cards(self, cards, deck):
        deck.shuffle()
        for turn in range(cards):
            for player in self.players:
                try:
                    player.draw(deck)
                except DeckEmptied:
                    print("Deck is emptied")
                    break


if __name__ == "__main__":
    game = Game(players=["Thach", "Sean"])
    game.play()
    # game.play(cards=50)


