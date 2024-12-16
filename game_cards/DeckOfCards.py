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
        """A method that shuffles the cards"""
        random.shuffle(self.deck_cards)


    def deal_one(self):
        """A method that draws, deletes and returns a one random card from the deck"""
        if not self.deck_cards:
            # if len(self.cards) == 0
            raise ValueError("No Cards Left In The Deck!")
        index = random.randint(0 ,len(self.deck_cards) -1) # choose a random card from the list (deck)
        removed_card = self.deck_cards.pop(index) # remove and deleting card from the deck
        return removed_card


