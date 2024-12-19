from unittest import TestCase
from unittest.mock import patch
from Card import *
from DeckOfCards import *
from Player import *
from game_cards.CardGame import CardGame


class TestCardGame(TestCase):
    def setUp(self):
        self.card_game = CardGame("Avi", "Moshe", 26)

# ============================= Start of __init__ Tests ======================================================

    def test_init_is_valid(self):
        """Test simple valid case of init """
        self.assertEqual("Avi", self.card_game.player1.player_name) # Player1 Name Test
        self.assertEqual("Moshe", self.card_game.player2.player_name) # Player2 Name Test
        self.assertEqual(26, self.card_game.player1.number_of_cards) # Player1 Number of cards Test
        self.assertEqual(26, self.card_game.player2.number_of_cards) # Player2 Number of cards Test

    def test_invalid_player1_type(self):
        """""Test for an invalid type for player1's name"""
        with self.assertRaises(TypeError):
            card_game = CardGame(123 , "Lotem" , 10)

    def test_invalid_player2_type(self):
        """""Test for an invalid type for player2's name"""
        with self.assertRaises(TypeError):
            card_game = CardGame("Moti" , [7,8,9] , 10)

    def test_invalid_number_of_cards_type(self):
        """""Test for an invalid type for player1's and players2's
             number of cards"""
        with self.assertRaises(TypeError):
            card_game = CardGame("Gabi" , "Lotem" , "777")



    def test_valid_lowest_number_of_cards_player1(self):
        """Test for a valid lowest value for players'1 number of cards"""
        self.card_game.player1.number_of_cards = 10
        self.assertEqual(10, self.card_game.player1.number_of_cards)

    def test_valid_lowest_number_of_cards_player2(self):
        """Test for a valid lowest value for players'2 number of cards"""
        self.card_game.player2.number_of_cards = 10
        self.assertEqual(10, self.card_game.player2.number_of_cards)

    def test_valid_highest_number_of_cards_player1(self):
        """Test for a valid highest value for players'1 number of cards"""
        self.card_game.player1.number_of_cards = 26
        self.assertEqual(26, self.card_game.player1.number_of_cards)

    def test_valid_highest_number_of_cards_player2(self):
        """Test for a valid highest value for players'2 number of cards"""
        self.card_game.player1.number_of_cards = 26
        self.assertEqual(26, self.card_game.player2.number_of_cards)

    def test_invalid_lowest_number_of_cards_player1(self):
        """Test for invalid value - when dealing a number of cards with a low invalid
          value to player1, the default value should work"""
        card_game = CardGame("Gabi", "Lotem", 9)
        self.assertEqual(card_game.player1.number_of_cards, 26)

    def test_invalid_lowest_number_of_cards_player2(self):
        """Test for invalid value - when dealing a number of cards with a low invalid
          value to player2, the default value should work"""
        card_game = CardGame("Gabi", "Lotem", 9)
        self.assertEqual(card_game.player2.number_of_cards, 26)

    def test_invalid_highest_number_of_cards_player1(self):
        """Test for invalid value - when dealing a number of cards with a high invalid
          value to player1, the default value should work"""
        card_game = CardGame("Gabi", "Lotem", 27)
        self.assertEqual(card_game.player1.number_of_cards, 26)

    def test_invalid_highest_number_of_cards_player2(self):
        """Test for invalid value - when dealing a number of cards with a high invalid
          value to player2, the default value should work"""
        card_game = CardGame("Gabi", "Lotem", 27)
        self.assertEqual(card_game.player2.number_of_cards, 26)


    def test_deck_cards_is_created(self):
        """Test that deck card has been created well and equal to the
           Original deck from DeckOfCards()"""
        deck = DeckOfCards()
        self.card_game.deck_cards_to_play = DeckOfCards()
        self.assertEqual(len(deck.deck_cards), len(self.card_game.deck_cards_to_play.deck_cards))

    def test_unique_deck_of_cards(self):
        """Test that all cards in the deck are unique."""
        unique_cards = set(self.card_game.deck_cards_to_play.deck_cards) # Create a unique deck
        self.assertEqual(len(self.card_game.deck_cards_to_play.deck_cards), len(unique_cards))


    def test_you_can_game_false(self):
        """Test that you_can_game is false after init called.
        Cant do a True case because its will be true only when
        we Created the cardGame object"""
        self.assertFalse(self.card_game.you_can_game)

# ====================================== End of __init__ Tests ========================================

# ======================================== Start new_game Tests ========================================


    def test_new_game_not_in_init_method(self):
        """Test that check if the method new_game() not activate from __init__"""
        self.card_game.you_can_game = False
        self.assertFalse(self.card_game.you_can_game)

    def test_mock_shuffle_called_only_once(self):
        """A test with a mock that checks that the cards_shuffle() method is called only once"""
        with patch("DeckOfCards.DeckOfCards.cards_shuffle") as mock_shuffle:
            CardGame("Player1" , "Player2"  , 26)
            mock_shuffle.assert_called_once()

    def test_mock_set_hand_called_only_twice(self):
        """A test with a mock that checks that the set_hand() method is only called twice"""
        with patch("Player.Player.set_hand") as mock_set_hand:
            CardGame("Player1" , "Player2"  , 26)
            self.assertEqual(mock_set_hand.call_count , 2)



# ===================================== End of new_game Test ============================================

# ===================================== Start get_winner Tests ==========================================


    def test_more_cards_to_player1_is_the_winner(self):
        """A test that checks who wins the game. The winner is the one who has more
            Cards at the end of the game. in this case - player1 """
        card1 = Card(9,4)
        card2 = Card(10,4)
        card3 = Card(11,4)
        card4 = Card(12,4)
        self.card_game.player1.cards = [card1 , card2 , card3]
        self.card_game.player2.cards = [card4]
        self.assertEqual(self.card_game.get_winner(), f"{self.card_game.player1}")

    def test_more_cards_to_player2_is_the_winner(self):
        """A test that checks who wins the game. The winner is the one who has more
            Cards at the end of the game. in this case - player2 """
        card1 = Card(9,4)
        card2 = Card(10,4)
        card3 = Card(11,4)
        card4 = Card(12,4)
        self.card_game.player1.cards = [card1]
        self.card_game.player2.cards = [card4 , card3 , card2]
        self.assertEqual(self.card_game.get_winner(), f"{self.card_game.player2}")


    def test_even_cards_to_both_players_draw(self):
        """"A test that checks that there is a draw in the game.
         If player1 and player2 have the same number of cards,
          the result will be a draw and return value will be None"""
        card1 = Card(9,4)
        card2 = Card(10,4)
        card3 = Card(11,4)
        card4 = Card(12,4)
        self.card_game.player1.cards = [card1 , card2]
        self.card_game.player2.cards = [card3 , card4]
        self.assertIsNone(self.card_game.get_winner())
