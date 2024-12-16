from DeckOfCards import *
from Player import *


class CardGame:
    def __init__(self , player1_name , player2_name, number_of_cards = 26):
        """A method that initializes 2 players and a number of cards for each player"""
        if not isinstance(player1_name , str):
            raise TypeError("Must be a String type!")
        if not isinstance(player2_name , str):
            raise TypeError("Must be a String type!")
        if not isinstance(number_of_cards , int):
            raise TypeError("Must be a Int type!")
        if number_of_cards < 10 or number_of_cards > 26:
            number_of_cards = 26
            print("Number Of Cards Must Be Between 10-26")
        self.deck_cards_to_play = DeckOfCards() # create a full deck cards (52 cards)

        self.you_can_game = True
        self.player1 = Player(player1_name , number_of_cards)
        self.player2 = Player(player2_name , number_of_cards)
        self.new_game()
        self.you_can_game = False


    def new_game(self):
        """A method that will start a new game, shuffle the deck of cards and deal cards to player1 and player2"""
        if not self.you_can_game:
        #if self.you_can_game == False:
            raise RuntimeError ("New Game Activated Only From __init__ Method")

        self.deck_cards_to_play.cards_shuffle() # shuffle the deck cards
        self.player1.set_hand(self.deck_cards_to_play) # deal cards to player1
        self.player2.set_hand(self.deck_cards_to_play) # deal cards to player2

    def get_winner(self):
        """A method that will return the player with the highest number of cards
         in the deck of cards, if the decks of cards are the same, None will be returned"""
        if len(self.player1.cards) > len(self.player2.cards):
            return f"{self.player1.player_name}"
        elif len(self.player2.cards) > len(self.player1.cards):
            return f"{self.player2.player_name}"
        else:
            return None





