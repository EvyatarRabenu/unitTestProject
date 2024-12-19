import random
from Card import *

class DeckOfCards:
    def __init__(self):
        """Initialize the deck of cards with 52 cards, 13 of each value , 4 for each suit"""
        self.deck_cards = []
        for value in range(2 , 15): # 13 value types
            for suit in range(1, 5): # 4 suit types --> 13 * 4 = 52 (deck of cards)
                self.deck_cards.append(Card(value,suit)) # create List (deck) of 52 Cards .


    def cards_shuffle(self):
        """A method that shuffles the deck of cards"""
        random.shuffle(self.deck_cards)


    def deal_one(self):
        """A method that removes and returns one random card from the deck of cards"""
        if not self.deck_cards: # If The List Is Empty
            print("The List (Deck Of Cards) Is Empty")
            return None
        index = random.randint(0 ,len(self.deck_cards) -1) # choose a random card from the list (deck)
        removed_card = self.deck_cards.pop(index) # remove the card from the original deck of cards
        return removed_card # return the choose removed card


