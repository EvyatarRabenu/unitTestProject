from unittest import TestCase
from DeckOfCards import *
from Card import *

class TestDeckOfCards(TestCase):
    def setUp(self):
        self.deck_of_cards = DeckOfCards()

# ============================================= Start of __init__ Tests ========================================

    def test_type_deck_of_cards(self):
        """Test if the type of deck of cards is list"""
        self.assertIsInstance(self.deck_of_cards.deck_cards , [])

    def test_deck_cards_size(self):
        """Initial test that deck cards length is 52"""
        self.assertEqual(len(self.deck_of_cards.deck_cards), 52)


    def test_all_cards_in_deck(self):
        """A test that goes through every card we created
        and checks if it is in the list (the deck of cards)"""
        for value in range(2 , 15):
            for suit in range(1, 5):
                self.assertIn(Card(value , suit) , self.deck_of_cards.deck_cards)

# ======================================= End of __init__ Tests ======================================

# ======================================= Start of card_shuffle() Test ================================

    def test_cards_shuffle(self):
        """ Test that checks the functionality of shuffle.
            Compare the entire deck before and after shuffle to ensure the deck was shuffled properly."""
        deck_before_shuffle = self.deck_of_cards.deck_cards.copy()
        self.deck_of_cards.cards_shuffle()
        deck_after_shuffle = self.deck_of_cards.deck_cards.copy()
        self.assertNotEqual(deck_before_shuffle, deck_after_shuffle)


    def test_count_after_shuffle_is_52_cards(self):
        deck_before_shuffle = self.deck_of_cards.deck_cards.copy()
        self.deck_of_cards.cards_shuffle()
        deck_after_shuffle = self.deck_of_cards.deck_cards.copy()
        self.assertEqual(len(deck_before_shuffle), 52 , "Deck Before Shuffle")
        self.assertEqual(len(deck_after_shuffle), 52 , "Deck After Shuffle")


# ====================================== End of card_shuffle() Tests ====================================

# ====================================== Start of deal_one() Test =======================================

    def test_if_its_card_type(self):
        """Test if the value returned from the method is of card type"""
        deck = DeckOfCards()
        if_card = deck.deal_one()
        self.assertIsInstance(if_card , Card)


    def test_empty_deck_of_cards(self):
        """Test that produces an empty deck of cards and makes
           a test that will throw a value error when trying to
           remove a card from the empty list"""
        deck = DeckOfCards() # Create a deck.
        deck.deck_cards = [] # Making the deck empty
        with self.assertRaises(ValueError):
            deck.deal_one() # Trigger a Value Error because the list is empty .


    def test_removed_card_not_exist_in_deck(self):
        """Test creates a deck of cards, removes one card
         and checks that the card is not in the deck"""
        deck = DeckOfCards()
        pull_one_card = deck.deal_one() # Pull one card from the deck
        self.assertNotIn(pull_one_card , deck.deck_cards)

    def test_removed_card_from_len_of_1_card(self):
        deck = DeckOfCards()
        card = Card(12,3)
        deck.deck_cards = [card]
        deck.deal_one()
        self.assertEqual(len(deck.deck_cards) , 0)









