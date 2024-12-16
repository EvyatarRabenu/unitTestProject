from Card import *
from DeckOfCards import *


class Player:
    def __init__(self , player_name , number_of_cards = 26):
        """A method that initializes a player's name and the number of cards he has,
           the default for providing cards to the player is a maximum of 26 and a minimum of 10"""
        if not isinstance(player_name , str):
            raise TypeError("Player Name Must be String!")
        if not isinstance(number_of_cards , int):
            raise TypeError("Number of Cards Must Be Int!")
        if number_of_cards < 10 or number_of_cards > 26:
            number_of_cards = 26
            print("Number of Cards Must Be Between 10-26")
        self.player_name = player_name
        self.number_of_cards = number_of_cards # number of cards the player's have
        self.cards = [] # list of card the player have




    def set_hand(self , deck_cards : DeckOfCards):
        """A method that receives a deck of cards of the game,
           and deals out of it random cards that the player should receive,
           use the deal_one() method from DeckOfCards class"""
        if not isinstance(deck_cards , DeckOfCards):
            raise TypeError("Must be DeckOfCards type!")
        if len(deck_cards.deck_cards) < self.number_of_cards: # if there is no cards in the original deck (52)
            raise ValueError (f"Not enough cards in the deck {self.number_of_cards} cards.")
        for _ in range(self.number_of_cards): # goes over the number of cards the player has
            self.cards.append(deck_cards.deal_one()) # inserts random cards into the card list , as the number of cards


    def get_card(self):
        """The same method as deal_one(), only in the current method ,
         the card is drawn from the player's deck and not from the original deck"""
        if not self.cards: # if there is no cards in the deck (list)
            raise ValueError("No Cards Left In The Deck!")
        index = random.randint(0 ,len(self.cards) -1) # create a variable that catch the random card from the player's deck
        removed_card =  self.cards.pop(index) # remove the card from the player's deck
        return removed_card


    def add_card(self , card : Card):
        """A method that receives a card and adds it to the player's deck"""
        if not isinstance(card , Card):
            raise TypeError("Must be a Card type!")
        self.cards.append(card) # Add card to the win player deck cards (list).


