from unittest.mock import patch
from unittest import TestCase , mock
from Card import *
from DeckOfCards import *
from Player import *



class TestPlayer(TestCase):
    def setUp(self):
        self.player = Player("Moris" ,26)
        self.deck1 = DeckOfCards()

# ============================================= Start of __init__ Tests ==========================================

    def test_init_is_valid(self):
        """Test simple valid case of init"""
        self.assertEqual("Moris" , self.player.player_name) # Name Test
        self.assertEqual(26 , self.player.number_of_cards) # Number of cards Test
        self.assertEqual([] , self.player.cards)

    def test_valid_name_type(self):
        """Test valid player name"""
        player = Player("Avi" , 15)
        self.assertEqual("Avi" , player.player_name)

    def test_valid_number_of_cards_type(self):
        """Test valid player - number of cards"""
        player = Player("Avi" , 15)
        self.assertEqual(player.number_of_cards , 15)

    def test_invalid_name_type(self):
        """Test for invalid value type of player name"""
        with self.assertRaises(TypeError):
            player = Player({"a":1 , "b":2} , 26)

    def test_invalid_number_of_cards_type(self):
        """Test for invalid value type of number of cards"""
        with self.assertRaises(TypeError):
            player = Player("Yoav" , (4,5,6))

    def test_number_of_cards_valid_lowest(self):
        """End value check - lowest valid number of cards a player can have"""
        player = Player("Eli" , 10)
        self.assertEqual(player.number_of_cards , 10)

    def test_number_of_cards_valid_highest(self):
        """End value check - highest valid number of cards a player can have"""
        player = Player("Eli" , 26)
        self.assertEqual(player.number_of_cards , 26)

    def test_number_of_cards_default(self):
        """Checking the default value, we did not put a value to
        the number of cards to check that the default value works."""
        player = Player("Oren")
        self.assertEqual(26 , player.number_of_cards)

    def test_number_of_cards_invalid_lowest(self):
        """Invalid low end value check - the number of cards
         should be updated to the default number"""
        player = Player("Eli" , 9)
        self.assertEqual(player.number_of_cards , 26)

    def test_number_of_cards_invalid_highest(self):
        """Invalid high end value check - the number of cards
         should be updated to the default number"""
        player = Player("Eli" , 27)
        self.assertEqual(player.number_of_cards , 26)

    def test_cards_list_empty(self):
        """Checking that the deck is empty when
        no deck object has been created yet"""
        self.assertEqual(self.player.cards , [])


    def test_set_hand_type(self):
        """Test set_hand with invalid deck type"""
        with self.assertRaises(TypeError):
            self.player.set_hand("I am a deck of cards")


    def test_full_deck_of_cards_at_the_beginning(self):
        """Checking when creating a new deck is equal to 52 cards"""
        deck = DeckOfCards()
        self.assertEqual(len(deck.deck_cards) , 52)

# ======================================== End of __init__ Tests =============================================

# ======================================= Start of set_hand() Test ===========================================

    def test_valid_set_hand_middle_cards(self):
        """Checking when creating a deck of cards, when dealing a deck to a player that the number
         of cards have been inserted correctly (middle value)"""
        deck = DeckOfCards()
        player = Player("Avi" , 13)
        player.set_hand(deck)
        self.assertEqual(player.number_of_cards, len(player.cards))

    def test_valid_test_set_hand_lowest_cards(self):
        """Checking when creating a deck of cards, when dealing a deck to a player that the number
         of cards have been inserted correctly (lowest value)"""
        deck = DeckOfCards()
        player = Player("Avi" , 10)
        player.set_hand(deck)
        self.assertEqual(player.number_of_cards, (len(player.cards)))

    def test_valid_test_set_hand_highest_cards(self):
        """Checking when creating a deck of cards, when dealing a deck to a player that the number
         of cards have been inserted correctly (highest value)"""
        deck = DeckOfCards()
        player = Player("Avi", 26)
        player.set_hand(deck)
        self.assertEqual(player.number_of_cards, (len(player.cards)))


    def test_invalid_set_hand_lowest_cards(self):
        """Testing When dealing an illegal low number of cards from a deck
        to a player, the number of cards is updated to the default number"""
        player = Player("Avi", 9)
        player.set_hand(DeckOfCards())
        self.assertEqual(player.number_of_cards , 26)

    def test_invalid_set_hand_highest_cards(self):
        """Testing When dealing an illegal high number of cards from a deck
        to a player, the number of cards is updated to the default number"""
        player = Player("Avi", 27)
        player.set_hand(DeckOfCards())
        self.assertEqual(player.number_of_cards , 26)

    def test_valid_size_deck_after_dealing_cards(self):
        """Checking when a deck of cards is dealt to a player, that the number of cards
         dealt to him falls properly from the original deck of cards (middle value)"""
        deck = DeckOfCards()
        player = Player("Moshe" , 13)
        player.set_hand(deck)
        self.assertEqual(len(deck.deck_cards) , 39)

    def test_valid_size_deck_after_dealing_cards_lowest(self):
        """Checking when a deck of cards is dealt to a player, that the number of cards
         dealt to him falls properly from the original deck of cards (lowest value)"""
        deck = DeckOfCards()
        player = Player("Moshe" , 10)
        player.set_hand(deck)
        self.assertEqual(len(deck.deck_cards) , 42)

    def test_valid_size_deck_after_dealing_cards_highest(self):
        """Checking when a deck of cards is dealt to a player, that the number of cards
         dealt to him falls properly from the original deck of cards (highest value)"""
        deck = DeckOfCards()
        player = Player("Moshe" , 26)
        player.set_hand(deck)
        self.assertEqual(len(deck.deck_cards) , 26)

    def test_unique_cards_in_player_deck(self):
        """Test that all cards in player deck cards are unique"""
        player = Player("Roi" , 26)
        player.set_hand(DeckOfCards())
        unique_cards = set()
        for card in player.cards:
            unique_cards.add(str(card))
        self.assertEqual(len(unique_cards) , len(player.cards))

    def test_no_enough_cards_in_deck(self):
        """Test that it is not possible to deal cards to a player when the deck is empty"""
        deck = DeckOfCards()
        player1 = Player("Avi" , 26)
        player2 = Player("Ori" , 26)
        player3 = Player("Gadi" , 10)
        player1.set_hand(deck)
        player2.set_hand(deck)
        with self.assertRaises(ValueError):
            player3.set_hand(deck)


    def test_deal_card_set_hand(self):
        """Test if cards dealt are correctly assigned to player hand."""
        with patch("DeckOfCards.DeckOfCards.deal_one", return_value=Card(11, 1)) as mock_deal_one:
            self.player.set_hand(self.deck1)
            expected_cards = [Card(11, 1)] * 26  # Expected 26 cards of Card(11, 1)
            self.assertEqual(self.player.cards, expected_cards)

# =========================== End of set_hand() Tests =========================

# =========================== Start of get_card() Tests =======================

    def test_type_return_value(self):
        """Test if the return Value its Card type"""
        player = Player("Moshe" , 26)
        player.set_hand(DeckOfCards())
        card = player.get_card()
        self.assertIsInstance(card , Card)

    def test_enough_cards_in_deck_cards(self):
        """"Test getCard() when the player deck pull out one card"""
        player = Player("Yosi", 26)
        player.set_hand(DeckOfCards())
        player.get_card()
        self.assertEqual(len(player.cards), 25)

    def test_get_card_not_enough_cards(self):
        """Test getCard() when the player deck doesnt have enough cards"""
        player = Player("Ori", 26)
        deck = DeckOfCards()
        player.set_hand(deck)
        for _ in range(player.number_of_cards):
            player.get_card()
        with self.assertRaises(ValueError):
            self.player.get_card()

    def test_get_card_not_in_player_deck_after(self):
        """Checking when a deck of cards is dealt to a player and one card is removed from him, that the same card
        that was removed is not in the player's deck of cards"""
        player = Player("Kobi" , 26)
        deck = DeckOfCards()
        player.set_hand(deck)
        remove_card = player.get_card()
        self.assertNotIn(remove_card , player.cards)

    def test_deal_card_set_hand_with_mock(self):
        """Test if cards dealt are correctly assigned to player hand."""
        with patch("DeckOfCards.DeckOfCards.deal_one", return_value=Card(11, 1)) as mock_deal_one:
            self.player.set_hand(self.deck1)
            expected_cards = [Card(11, 1)] * 26 # 26 cards of (11,1)
            self.assertEqual(expected_cards, self.player.cards)

    # ============================== End of get_card() Tests ================================

    # ============================== Start of add_card() Tests ==============================

    def test_valid_type_value_add_card(self):
        """A test where a card is inserted into
         the player's deck of cards that it actually enters"""
        player = Player("Oleg" , 10)
        new_card = Card(2,4)
        player.add_card(new_card)
        self.assertIn(new_card , player.cards)


    def test_invalid_type_value_add_card(self):
        """Test if the return Value its not Card type"""
        player = Player("Moshe" , 10)
        with self.assertRaises(TypeError):
            self.player.add_card("ABC")

    def test_add_card_in_player_deck(self):
        """Test the player's deck of cards,
           when a card is added the list is updated"""
        player = Player("Amnon" , 26)
        new_card = Card(10,3)
        player.add_card(new_card)
        self.assertEqual(len(player.cards) , 1)

    def test_add_card_in_player_deck_to_cards_list(self):
        """A test where a player is dealt a deck of cards and a new card is added to him,
         that the new card was inserted into the deck as expected"""
        player = Player("Amnon" , 26)
        new_card = Card(10,3)
        player.set_hand(DeckOfCards())
        player.add_card(new_card)
        self.assertIn(new_card , player.cards)

    def test_add_card_deck_size_goes_up(self):
        """A test where a player is dealt a deck of cards, and a new card is
         added to the deck, the deck of cards is updated"""
        player = Player("Amnon" , 19)
        new_card = Card(10,3)
        player.set_hand(DeckOfCards())
        player.add_card(new_card)
        self.assertEqual(len(player.cards) , 20)
