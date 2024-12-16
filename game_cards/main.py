from CardGame import *
from Player import *
from DeckOfCards import *
from Card import *

player1_name = (input("Player 1 - Please Enter Your Name: "))
player2_name = (input("Player 2 - Please Enter Your Name: "))

game = CardGame(player1_name , player2_name , 26) # Create a game with 2 players and 26 card for each player.

print(f"Hey {player1_name} , Your Cards Are: {game.player1.cards}")
print(f"Hey {player2_name} , Your Cards Are: {game.player2.cards}")

for i in range(10):
    print(f" ========== Round {i+1} ==========")
    cards_of_player_1 = game.player1.get_card()
    cards_of_player_2 = game.player2.get_card()

    print(f"{player1_name} Pull out the card: {cards_of_player_1}")
    print(f"{player2_name} Pull out the card: {cards_of_player_2}")

    if cards_of_player_1 > cards_of_player_2:
        game.player1.add_card(cards_of_player_1)
        game.player1.add_card(cards_of_player_2)
        print(f"{player1_name} Won This Round!")

    elif cards_of_player_2 > cards_of_player_1:
        game.player2.add_card(cards_of_player_1)
        game.player2.add_card(cards_of_player_2)
        print(f"{player2_name} Won This Round!")

    else: # Tie - Should Never happen with 1 deck of cards because if values is the same - the suit will win.
        print(f"No Cards for {player1_name} or {player2_name}.")


print(" ========== Game Over ===========")
print(f"The Cards left with {player1_name}: {len(game.player1.cards)}")
print(f"The Cards left with {player2_name}: {len(game.player2.cards)}")
print(" ========== Game Results: ===========")

winner = game.get_winner()
if winner: #Like if winner == True
    print(f"The WINNER is : {winner}")
else:
    print("The Game Ended In A Draw!")

