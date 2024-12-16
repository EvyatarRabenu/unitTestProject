from unittest import TestCase
from Card import *


class TestCard(TestCase):
    def setUp(self):
        self.card = Card(12 , 2)

# ====================================== Start Of __init__ Test ==================================

    def test_init_is_valid(self):
        """Test simple valid case of init"""
        self.assertEqual(12 , self.card.value) # Value Test
        self.assertEqual(2 , self.card.suit) # Suit Test

    def test_valid_value(self):
        """Test values - valid middle card value"""
        card1 = Card(7 , 2)
        self.assertEqual(7 , card1.value)

    def test_valid_lowest_value(self):
        """Test edge values - valid low card value"""
        card1 = Card(2 , 2)
        self.assertEqual(2 , card1.value)

    def test_valid_highest_value(self):
        """Test edge values - valid high card value"""
        card1 = Card(14 , 2)
        self.assertEqual(14 , card1.value)

    def test_invalid_lowest_value(self):
        """Test edge values - invalid low card value"""
        with self.assertRaises(ValueError):
            card1 = Card(1 , 2)

    def test_invalid_highest_value(self):
        """Test edge values - invalid high card value"""
        with self.assertRaises(ValueError):
            card1 = Card(15 , 2)

    def test_valid_suit(self):
        """Test suit - valid middle card suit"""
        card1 = Card(2, 2)
        self.assertEqual(2 , card1.suit)

    def test_valid_lowest_suit(self):
        """Test edge suits - valid low card suit"""
        card1 = Card(2, 1)
        self.assertEqual(1 , card1.suit)

    def test_valid_highest_suit(self):
        """Test edge suits - valid high card suit"""
        card1 = Card(2, 4)
        self.assertEqual(4, card1.suit)

    def test_invalid_lowest_suit(self):
        """Test edge suits - invalid low card suit"""
        with self.assertRaises(ValueError):
            card1 = Card(2 , 0)

    def test_invalid_highest_suit(self):
        """Test edge suits - invalid high card suit"""
        with self.assertRaises(ValueError):
            card1 = Card(2 , 5)

    def test_value_type(self):
        """Test value type - invalid value type"""
        with self.assertRaises(TypeError):
            card1 = Card("abc" , 5)

    def test_suit_type(self):
        """Test suit type - invalid suit type"""
        with self.assertRaises(TypeError):
            card1 = Card(13 , [1,2,3])

    def test_card_comparison(self):
        """Test comparison between cards"""
        card1 = Card(10, 2)
        card2 = Card(12, 1)
        self.assertTrue(card2 > card1)
        self.assertFalse(card1 > card2)

 # ======================================= End Of __init__ Tests ======================================

# ======================================== Start Of __gt__ Tests ======================================

    def test_gt_valid_different_values_true(self):
        """Size check between 2 different values - returns True """
        card1 = Card(11 , 4)
        card2 = Card(12 , 1)
        self.assertTrue(card2 > card1)

    def test_gt_valid_different_values_false(self):
        """Size check between 2 different values - returns False """
        card1 = Card(11 , 4)
        card2 = Card(12 , 1)
        self.assertFalse(card1 > card2)

    def test_gt_valid_same_values_true(self):
        """Test size between 2 different suits - returns True for the higher suit"""
        card1 = Card(10 , 2)
        card2 = Card(10 , 3) # Highest suit win
        self.assertTrue(card2 > card1)


    def test_gt_valid_same_values_false(self):
        """Test size between 2 different suits - returns False for the lowest suit"""
        card1 = Card(10 , 2)
        card2 = Card(10 , 3) # Highest suit win
        self.assertFalse(card1 > card2)

    def test_gt_end_of_valid_values(self):
        """Testing edge values for values between 2 different cards
         - returns True for the higher value"""
        card1 = Card(2 , 2)
        card2 = Card(14 , 3)
        self.assertTrue(card2 > card1)

    def test_gt_end_of_valid_values_false(self):
        """Testing edge values for values between 2 different cards
         - returns False for the lowest value"""
        card1 = Card(2 , 2)
        card2 = Card(14 , 3)
        self.assertFalse(card1 > card2)

    def test_gt_end_of_valid_suits_true(self):
        """Testing edge values for suits between 2 different cards
         - returns True for the highest suit"""
        card1 = Card(8 , 1)
        card2 = Card(8 , 4)
        self.assertTrue(card2 > card1)

    def test_gt_end_of_valid_suits_false(self):
        """Testing edge values for suits between 2 different cards
         - returns False for the lowest suit"""
        card1 = Card(8 , 1)
        card2 = Card(8 , 4)
        self.assertFalse(card1 > card2)

    def test_gt_same_values_and_suits_1(self):
        """Test similar card values for values and suits between 2 different cards
         - returns False when comparing size (when card1>card2) """
        card1 = Card(12 , 2)
        card2 = Card(12 , 2)
        self.assertFalse(card1 > card2)

    def test_gt_same_values_and_suits_2(self):
        """Test similar card values for values and suits between 2 different cards
         - returns False when comparing size (when card2>card1) """
        card1 = Card(12 , 2)
        card2 = Card(12 , 2)
        self.assertFalse(card2 > card1)

    def test_gt_invalid_other_type(self):
        """Test if the other parameter contains card values"""
        with self.assertRaises(TypeError):
            card1 = Card(10,"123") #String , Must be int

# ============================= End Of __gt__ Tests =====================================================

# ============================= Start Of __eq__ Tests ===================================================

    def test_eq_invalid_other_type(self):
        """Test if the other parameter contains card values"""
        with self.assertRaises(TypeError):
            card1 = Card(11, ["a", "b", "c"])


    def test_eq_card_comparison_draw(self):
        """Test comparison between cards - draw situation"""
        card1 = Card(12, 3)
        card2 = Card(12, 3)
        self.assertTrue(card2 == card1)


    def test_eq_same_value_different_suit(self):
        """Test 2 cards with similar values and different suits,
           return False if the cards are not equal"""
        card1 = Card(10, 2)
        card2 = Card(10, 3)
        self.assertFalse(card1 == card2)

    def test_eq_same_suit_different_value(self):
        """Test 2 cards with similar values and different suits,
           return False if the cards are not equal"""
        card1 = Card(11, 3)
        card2 = Card(10, 3)
        self.assertFalse(card1 == card2)

    def test_eq_edge_cases(self):
        """Edge value check - comparison between a card with
         low edge values and a card with high edge values"""
        lowest_card = Card(2,1) # Lowest Value And Suit
        highest_card = Card(14,4) # Highest Value And Suit
        self.assertFalse(lowest_card == highest_card)
