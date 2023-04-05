# This is a game where the player is given two subjects and asked to guess which one has more followers on social media.

import art
import random
from game_data import data
# from data_test import data    # Debug

# Notes: code for taking out a dictionary from a list:
# Notes: thelist[:] = [d for d in thelist if d.get('id') != 2]


while True:
    # Initialize the game
    print(art.logo)
    game_over = False
    score = 0
    data_in_game = data

    # Randomly select 2 subjects from the list, then remove these two from the list
    subject1 = random.choice(data_in_game)
    data_in_game[:] = [item for item in data_in_game if item.get('name') != subject1['name']]
    subject2 = random.choice(data_in_game)
    data_in_game[:] = [item for item in data_in_game if item.get('name') != subject2['name']]
    
    while not game_over:
        # Print the subjects for player to compare
        print(F"\nCompare A: {subject1['name']}, a {subject1['description'].lower()} from {subject1['country']}.")
        print(art.vs)
        print(F"Against B: {subject2['name']}, a {subject2['description'].lower()} from {subject2['country']}.")
        print(F"A {subject1['follower_count']} vs B {subject2['follower_count']}")    # Debug

        # Read in player's guess
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        while guess != 'a' and guess != 'b':
            guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        # Check player's guess
        if guess == 'a':
            if subject1['follower_count'] > subject2['follower_count']:
                score += 1
            else:
                print("\nYou are wrong! Game over!")
                game_over = True
                break
        else: # guess == 'b'
            if subject1['follower_count'] < subject2['follower_count']:
                score += 1
            else:
                print("\nYou are wrong! Game over!")
                game_over = True
                break

        # Clear the console and print the result
        print("\033[H\033[J", end="")
        print(art.logo)
        print(F"You are right! Current score: {score}.")

        # subject1 is now subject 2, subject2 is a new random subject
        subject1 = subject2
        subject2 = random.choice(data_in_game)
        data_in_game[:] = [item for item in data_in_game if item.get('name') != subject2['name']]

    print(F"Your final score: {score}.")
    input("Press any key to restart...")
    print("\033[H\033[J", end="")
