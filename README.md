# MAPUTE ANDRAE M
# CMSC12 
# Final Project: Blackjack Game with Leaderboard

## Overview

This project is a standard blackjack game implemented in Python, featuring a scoring system and a leaderboard to track players' scores. Players can enjoy the classic blackjack experience against a computer dealer, aiming to achieve a higher score without exceeding 21 points.

## Game Features

- **Deck Creation:** A standard deck of cards is created with four suits (Clubs ♣, Hearts ❤, Diamonds ♦, Spades ♠) and thirteen ranks (2 to 10, Jack, Queen, King, Ace).
  
- **Player Interaction:** Players can choose to hit (receive another card) or stand (end their turn) during their round.

- **Scoring:** The game calculates scores based on the value of cards in hand. Face cards (Jack, Queen, King) are worth 10 points each, and Aces can be worth either 1 or 11 points.

- **Gameplay Flow:** 
  - Players start with two cards, and the dealer also receives two cards.
  - If a player's initial two-card hand totals 21 (a blackjack), they win extra points.
  - Players can continue hitting until they choose to stand or exceed 21 points (bust).
  - The dealer's actions are automated based on set rules.

- **Leaderboard:** The game includes a leaderboard that records and displays players' scores. Players can save their scores with their names after each session.

## Instructions

### Installation and Setup

1. **Python Installation:**
   - Ensure Python is installed on your system. If not, download and install Python from [python.org](https://www.python.org).

2. **Run the Game:**
   - Copy and paste the provided Python code into a file named `blackjack.py`.
   - Open a terminal or command prompt and navigate to the directory where `blackjack.py` is located.
   - Run the game by executing the command:
     ```
     python blackjack.py
     ```

### Gameplay

- **Main Menu Options:**
  - **[1] Play:** Start a new game of blackjack.
  - **[2] Leaderboard:** View the current leaderboard with top scores.
  - **[3] Exit:** Exit the game.

- **Player Actions:**
  - **Hit:** Receive another card to increase your hand total.
  - **Stand:** End your turn without taking any additional cards.

- **End of Game:**
  - Players' scores are recorded on the leaderboard based on their performance in each session.

### Leaderboard

- The leaderboard displays the top scores achieved by players.
- Scores are ranked from highest to lowest, showing the player's name and score.

## Enjoy Your Game!

Experience the thrill of blackjack and compete for the top spot on the leaderboard. Have fun playing and testing your luck and strategy with this Python-based blackjack game!
