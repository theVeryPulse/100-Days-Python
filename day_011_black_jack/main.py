logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
print(cards)


def what_to_do():
    """Ask player if they want to hit or stand"""
    next_move = ''
    while next_move != "hit" and next_move != 'stand':
        next_move = input("What do you want to next? Input 'hit' or 'stand': ").lower()
    return next_move


def deal_new_hands(dealer_hand, player_hand):
    """Deal new cards to hands"""
    for i in range(0, 2):
        dealer_hand.append(random.choice(cards))
        player_hand.append(random.choice(cards))


def black_jack(dealer_sum, player_sum):
    """Check if anyone has black jack (exactly two cards: 10 and 11) and ends game accordingly"""
    if dealer_sum == 21 and player_sum == 21:
        print("Unbelievable, you both have black jacks. It is a tie!")
        return True
    elif dealer_sum == 21:
        print("Dealer has black jack. Dealer wins! You lose.")
        return True
    elif player_sum == 21:
        print("You have black jack. You win!")
        return True


def above_21_A(hand):
    """Pass in the list to check if above 21. If above 21, does it contain 11 that can be reduced to 1"""
    while sum(hand) > 21:
        if 11 in hand:
            hand[hand.index(11)] = 1
        else:
            break


def compare_score(dealer_hand, player_hand):
    """Compare the score and decides who wins"""
    dealer_sum = sum(dealer_hand)
    player_sum = sum(player_hand)
    while dealer_sum > 21:
        above_21_A(dealer_sum)
        if not 11 in dealer_sum:
            break
    while player_sum > 21:
        above_21_A(player_hand)
        if not 11 in player_sum:
            break
    if dealer_sum > 21:
        print("You win!")
        return True
    elif player_sum > 21:
        print("You lose!")
        return True
    elif dealer_sum == player_sum:
        print("It's a tie!")
        return True
    elif player_hand > dealer_hand:
        print("You win!")
        return True
    elif player_hand < dealer_hand:
        print("You lose!")
        return True


while True:
    game_over = False
    while not game_over:
        print(logo)
        dealer_hand = []
        player_hand = []
        deal_new_hands(dealer_hand, player_hand)
        # print(player_hand, dealer_hand)

        dealer_sum = sum(dealer_hand)
        player_sum = sum(player_hand)

        # Check if anyone has exactly 21 points, i.e., black jack
        game_over = black_jack(dealer_sum, player_sum)
        if game_over:
            break

        # Show player the available information
        print(f"You have {player_hand[0]} and {player_hand[1]}. Your sum is {player_sum}")
        print(F"Dealer has {dealer_hand[1]}")

        # Ask player if they want to hit or stand
        move = "hit"
        while move == "hit":
            move = what_to_do()
            # If player chooses to hit
            if move == "hit":
                player_hand.append(random.choice(cards))
                above_21_A(player_hand)
                player_sum = sum(player_hand)

                print(f"You have {player_hand}. Your sum is {player_sum}")

                if player_sum > 21:
                    print("You are greater than 21, you lose!")
                    game_over = True
                    break
                # print("line 174")
        if game_over:
            break
        # print("line 177")
        # Players chooses stand, dealer reveal hand"
        print(F"Dealer has {dealer_hand[0]} and {dealer_hand[1]}. Their sum is {dealer_sum}.")

        while dealer_sum <= 16:
            dealer_hand.append(random.choice(cards))
            dealer_sum = sum(dealer_hand)
            print(F"Dealer draws a card, they now have {dealer_hand}, their sum is {dealer_sum}")

        above_21_A(dealer_hand)
        dealer_sum = sum(dealer_hand)
        if dealer_sum > 21:
            print("Dealer is greater than 21. You win!")
            game_over = True
        if game_over:
            break
        # print("line 193")

        # Compare hands and decides who wins
        game_over = compare_score(dealer_hand, player_hand)
        game_over = True
    input("Press any key to restart game")
    game_over = False
