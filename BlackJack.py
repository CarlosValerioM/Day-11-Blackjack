#!/usr/bin/env python3
"""
blackjack.py - A simple blackjack game where you play against the computer (house).

Author: Carlos Valerio (CarlosValerioM)
Date: 2025/03/17
License: MIT
Dependencies: None (built-in functions only)

Description:
This script simulates a simple game of blackjack where the player competes against the house.
The player and house both receive two cards, and the player can choose to 'hit' (get another card) or 'stand' (keep their current hand).
The goal is to get as close to 21 as possible without exceeding it.

The script takes the following actions:
1. Deals two cards to the player and two cards to the house.
2. Displays the player's hand and one of the house's cards.
3. Allows the player to choose to 'hit' or 'stand'.
4. The house then plays according to basic blackjack rules (house must hit if under 17).
5. The game determines if the player wins or loses based on the final hands.

Usage:
Run the script and follow the prompts:
    python blackjack.py

Example Output:
    Your hand is: ['A', '8']
    House's first card is A
    Type 'y' if you want to get another card: y
    Your hand is: ['A', '8', '4']
    Type 'y' if you want to get another card: n
    Your final hand: 13
    The House final hand is ['A', '7', '10'] with total 18
    You lose!
"""
import random

# Function to draw a card from the deck and remove it from the respective suit
def draw_card(deck):
    # Randomly select a suit (0 = hearts, 1 = diamonds, 2 = clubs, 3 = spades)
    suit_index = random.randint(0, 3)
    # Randomly select a card from the chosen suit
    card = random.choice(deck[suit_index])
    # Remove the card from the deck to simulate it being drawn
    deck[suit_index].remove(card)
    return card, deck

# Function to draw a number of cards (hand) from the deck
def draw_hand(deck, num_cards):
    hand = []
    for _ in range(num_cards):
        card, deck = draw_card(deck)
        hand.append(card)
    return hand, deck

# Function to evaluate the total value of a hand
def evaluate_hand(hand):
    result = sum(map(lambda x: 10 if x in ['J', 'Q', 'K']  # Face cards are worth 10
                             else 11 if x == 'A'             # Ace is worth 11 by default
                             else int(x), hand))             # Other cards are their integer value
    return result

# Function to simulate the house's (dealer's) turn in the game
def house_turn(house_hand, deck, player_hand_value):
    # House must keep drawing until its hand is at least as high as the player's hand, but not exceeding 21
    while evaluate_hand(house_hand) < player_hand_value and evaluate_hand(house_hand) <= 21:
        card, deck = draw_card(deck)
        house_hand.append(card)
    return house_hand, deck

# Main game function
def main():
    # The deck consists of four suits (hearts, diamonds, clubs, spades), each with 13 cards
    hearts = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    clubs = hearts.copy()
    spades = hearts.copy()
    diamonds = hearts.copy()

    # Combine all suits into the deck
    deck = [hearts, diamonds, clubs, spades]

    # Deal two cards to both the player and the house
    hand, deck = draw_hand(deck, 2)  # Player's hand
    house_hand, deck = draw_hand(deck, 2)  # House's hand

    print(f"Your hand is: {hand}")
    print(f"House's first card is {house_hand[0]}")

    # Initial hand values
    player_hand_value = evaluate_hand(hand)
    house_hand_value = evaluate_hand(house_hand)

    # Player's turn (loop for drawing cards)
    while player_hand_value <= 21:
        deal = input("Type 'y' if you want to get another card: ").lower()
        if deal == 'y':
            card, deck = draw_card(deck)
            hand.append(card)
            print(f"Your hand is: {hand}")
            player_hand_value = evaluate_hand(hand)
        else:
            # If player decides to stop, it's the house's turn
            house_hand, deck = house_turn(house_hand, deck, player_hand_value)
            house_hand_value = evaluate_hand(house_hand)
            print(f"Your final hand: {player_hand_value}")
            print(f"The House final hand is {house_hand} with total {house_hand_value}")
            break  # Exit the loop once the player stops

    # Determine the outcome based on the final values of both hands
    if player_hand_value > 21:
        print("You went over 21. You lose!")
    elif house_hand_value > 21:
        print("The House went over 21. You win!")
    elif player_hand_value > house_hand_value:
        print("You win!")
    elif player_hand_value < house_hand_value:
        print("You lose!")
    else:
        print("It's a tie!")

# Run the game if this file is executed directly
if __name__ == '__main__':
    main()