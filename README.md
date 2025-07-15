🃏 War Game Unit Test Project

This project simulates a simplified **War card game** between two players, built in Python, with a strong focus on writing **unit tests** using the `unittest` framework.

 🎮 Game Description

- Two players compete in a game of War.
- Each player receives a random hand of cards.
- The deck includes traditional suits: ♣ Clubs, ♥ Hearts, ♠ Spades, ♦ Diamonds.
- The game runs for **10 rounds**, and in each round both players play one card.
- The player with the higher card wins the round.
- At the end of the game, the player with the most winning rounds is declared the winner.

 🧱 Project Structure

- The project is divided into **4 main classes** that handle the game logic:
  - `Card` – represents a single playing card.
  - `DeckOdCards` – represents and manages the deck of cards.
  - `Player` – handles player behavior and hands.
  - `CardGame` – controls the game flow and rounds.

- For each class, there is a corresponding **unit test class**:
  - `test_Card`
  - `test_DeckOfCards`
  - `test_Player`
  - `test_CardGame`

All tests are implemented using Python's built-in `unittest` module.

 🧪 Features

- Clear separation of game logic and testing logic.
- Extensive test coverage for each class.
- Testing includes:
  - Valid card creation
  - Deck integrity and shuffling
  - Player turn logic
  - Game flow and win conditions

## 🚀 How to Run the Tests

Make sure you have Python installed. Then, from the project root directory, run:

```bash
python -m unittest discover
