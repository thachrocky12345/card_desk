"# card_desk"
Card has 3 colors associated with value:
red = 3, yellow =2, green = 1

As default each color will have 13 cards with value from 1 to 14.
However you can set it with differently using by changing the NUMBER_VALUE_FOR_EACH_COLOR on config.py

To sorted the card:
deck = Deck()
deck.sort_cards(["green", "red", "yellow"])

To start the game, you input the players with only names:
example:
game = Game(players=["Thach", "Sean"])

to play, at default, each player will only get 3 cards
example:
game.play()
output:

Sean is the winner with scores: 46
Thach's hand:
3 of green
8 of red
4 of green

Sean's hand:
9 of yellow
6 of green
11 of yellow


;however, you can set it differently using:
game.play(cards=50)
the card will be distributed until the deck is emptied

The winner is the one that has highest hand_score which is calculated by color point * number (color point calculation, red = 3, yellow =2, green = 1).



Code interview question:
1.	Work with the language you are most familiar with, but preferably the language which is the focus of the hiring.
2.	The code you produce should be as close to “production quality” as possible, time permitting.
This means you should document all assumptions, perform all tests, linting, etc. Tests should be extensible.
3.	Code should be Object Oriented.
4.	Defer to a “standard” deck of cards.
5.	Post the completed product to a public Github and send the link to recruiter.


Create a card game which supports all of the operations below.
1.	Shuffle cards in the deck: randomly mix the cards in the card deck, and return a whole deck of cards with a mixed order.

2.	Get a card from the top of the deck: get one card from the top of the card deck, return a card, and if there is no card left in the deck, return error or exception. 

3.	Sort cards: take a list of color as parameter and sort the card in that color order.
Numbers should be in ascending order. 
i.e. If the deck has a card contains with following order 
    (red, 1), (green, 5), (red, 0), (yellow, 3), (green, 2)
i.	Sort cards ([yellow, green, red]) will return the cards with following order
   (yellow, 3), (green, 0), (green, 5), (red, 0), (red, 1) 

4.	Determine winners: 2 players play the game. They will draw 3 cards by taking turns.
Whoever has the high score wins the game. (color point calculation, red = 3, yellow =2, green = 1) the point is calculated by color point * number in the card.  

