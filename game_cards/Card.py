class Card:
    def __init__(self, value, suit):
        """ method that initializes a card value and a suit """
        if value < 2 or value > 14:
            raise ValueError("Value Must Be Between 2 - 14")
        if not isinstance(value, int):
            raise TypeError("Value Must Be Int!")
        if not isinstance(suit, int):
            raise TypeError("Suit Must Be Int!")
        if suit < 1  or suit > 4:
            raise ValueError("Suit Must Be Int Between 1 - 4")
        self.value = value
        self.suit = suit

    def __repr__(self):
        """Presentation of the card"""
        suits = {1: "Diamond♦️", 2: "Spade♠️", 3: "Heart♥️", 4: "Club♣️"}

        values = {2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "10",
                  11: "Jack", 12: "Queen", 13: "King", 14: "Ace"}

        return f"{values[self.value]} of {suits[self.suit]}"


    def __gt__(self, other):
        """ Comparison (>) by value, and if equal - by suit """
        if not isinstance(other , Card):
            raise TypeError("Type Must Be Card!")
        if self.value != other.value: # if the value is not the same
            return self.value > other.value # the large value is greater
        return self.suit > other.suit  # if its same - suit its greater


    def __eq__(self, other):
        """ Comparison of cards by value and symbol """
        if not isinstance(other , Card):
            raise TypeError("Must be a Card!")
        return self.value == other.value and self.suit == other.suit



