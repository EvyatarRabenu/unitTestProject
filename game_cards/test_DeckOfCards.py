from unittest import TestCase
from DeckOfCards import *
from Card import *

class TestDeckOfCards(TestCase):
    def setUp(self):
        self.deck_of_cards = DeckOfCards()

# ============================================= Start of __init__ Tests ========================================

    def test_type_deck_of_cards(self):
        """Test if the type of deck of cards is list"""
        self.assertIsInstance(self.deck_of_cards.deck_cards , list)

    def test_deck_cards_size(self):
        """Initial test that deck cards length is 52"""
        self.assertEqual(len(self.deck_of_cards.deck_cards), 52)

    def test_card_values_range(self):
        """test that will verify that the values of the cards
         are within the standard range 2-14:"""
        for card in self.deck_of_cards.deck_cards:
            self.assertTrue(2 <= card.value <= 14) # Range from 2 to Ace , 2-14

    def test_card_suits_range(self):
        """A test that will verify that the suits of the cards
         are within the standard range 1-4:"""
        for card in self.deck_of_cards.deck_cards:
            self.assertTrue(1 <= card.suit <= 4) # Range from 1 to 4

    def test_all_cards_in_deck(self):
        """A test that goes through every card we created
        and checks if it is in the list (the deck of cards)"""
        for value in range(2 , 15):
            for suit in range(1, 5):
                self.assertIn(Card(value , suit) , self.deck_of_cards.deck_cards)

# ======================================= End of __init__ Tests ======================================

# ======================================= Start of card_shuffle() Test ================================


    def test_cards_shuffle(self):
        """A test that checks the functionality of shuffle.
            Create variables that save an original deck and a shuffled deck
            and compare their first cells that the decks were really shuffled"""
        deck_before_shuffle = self.deck_of_cards.deck_cards.copy() # Go through the list from beginning to end
        self.deck_of_cards.cards_shuffle()
        deck_after_shuffle = self.deck_of_cards.deck_cards.copy() # Go through the list from beginning to end
        self.assertNotEqual(deck_before_shuffle[0] , deck_after_shuffle[0])

# ====================================== End of card_shuffle() Tests ====================================

# ====================================== Start of deal_one() Test =======================================

    def test_if_its_card_type(self):
        """Checking if the value returned from the method is of card type"""
        deck = DeckOfCards()
        if_card = deck.deal_one()
        self.assertIsInstance(if_card , Card)


    def test_empty_deck_of_cards(self):
        """A test that produces an empty deck of cards and makes
           a test that will throw a value error when trying to
           remove a card from the empty list"""
        deck = DeckOfCards() # Create a deck.
        deck.deck_cards = [] # Making the deck empty
        with self.assertRaises(ValueError):
            deck.deal_one() # Trigger a Value Error because the list is empty .


    def test_removed_card_not_exist_in_deck(self):
        """A test creates a deck of cards, removes one card
         and checks that the card is not in the deck"""
        deck = DeckOfCards()
        pull_one_card = deck.deal_one() # Pull one card from the deck
        self.assertNotIn(pull_one_card , deck.deck_cards)


    def test_pull_out_all_the_cards(self):
        """A test that draws all the cards, and then when try to pull out
           again from an empty deck it will throw an error"""
        deck = DeckOfCards()
        for _ in range(len(self.deck_of_cards.deck_cards)): # 52 Cards in Deck
            deck.deal_one()
        with self.assertRaises(ValueError):
            deck.deal_one() # Trigger a value Error because the list is empty

    def test_deal_one_without_shuffled_deck(self):
        """Checking if the deal_one() method works as expected."""
        deck = DeckOfCards()
        deck.deal_one()
        self.assertEqual(len(deck.deck_cards), 51)


    def test_deal_one_with_shuffled_deck(self):
        """Integration Test : Checking if the deal_one() method
           works as expected after the shuffle."""
        deck = DeckOfCards()
        deck.cards_shuffle()
        deck.deal_one()
        self.assertEqual(len(deck.deck_cards), 51)








