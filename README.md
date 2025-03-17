# Day-11-Blackjack
Your Blackjack Game - Difficulty: Easy
# BlackjackGame

## Author:
Carlos Valerio (CarlosValerioM)

## Date:
2025/03/17

## License:
MIT License

## Dependencies:
None (built-in functions only)

## Description:
`blackjack.py` is a simple Python script that simulates a Blackjack game against the computer (house). It prompts the player for input and deals cards to both the player and the house. The game follows basic Blackjack rules where the player aims to get a hand value as close to 21 as possible without exceeding it.

The game works as follows:
1. The deck is shuffled and cards are dealt to the player and the house.
2. The player can choose to "hit" (draw another card) or "stand" (keep their current hand).
3. The house automatically "hits" until it reaches a hand value of 17 or higher.
4. The winner is determined based on who has the highest hand without exceeding 21.

## Usage:

1. Clone this repository:

```bash
git clone https://github.com/CarlosValerioM/Day-2-Blackjack.git
```
Navigate to the project directory:

```bash
cd Day-2-Blackjack
```
Run the script:

```bash
python blackjack.py
```
The game will prompt you for input, and based on your decisions, it will play out the game and determine the winner.

## Example Output:
```bash
Your hand is: ['A', '8']
House's first card is 10
Type 'y' if you want to get another card: y
Your hand is: ['A', '8', '6']
Your final hand: 15
The House final hand is ['K', '8'] with total 18
You lose!
```
## How it works:
The deck is created with 52 cards and shuffled.

Both the player and the house are dealt two cards.

The player can decide to draw a card by typing 'y' (hit) or stop drawing cards by typing anything else (stand).

The house automatically draws cards (hits) until it has a hand value of 17 or higher.

The winner is determined by comparing the player's and the house's hand values. If both the player and house exceed 21, the game ends in a draw.
## License:
This project is licensed under the MIT License.
