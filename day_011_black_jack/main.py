import random

# ############## Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.


def ask_next_move() -> str:
    """Ask player if they want to hit or stand"""
    next_move = ''
    while next_move != "hit" and next_move != 'stand':
        next_move = input("What do you want to next? Input 'hit' or "
                          "'stand': ").lower()
    return next_move


def deal_new_hands(dealer_hand: list[int], player_hand: list[int],
                   cards: list[int]):
    """Deal new cards to hands"""
    for i in range(0, 2):
        dealer_hand.append(random.choice(cards))
        player_hand.append(random.choice(cards))


def sum_equals_to_21(dealer_sum: int, player_sum: int) -> bool:
    """Check if anyone has black jack (exactly two cards: 10 and 11) and
    ends game accordingly"""
    if dealer_sum == 21 and player_sum == 21:
        print("Unbelievable, you both have black jacks. It is a tie!")
        return True
    elif dealer_sum == 21:
        print("Dealer has black jack. Dealer wins! You lose.")
        return True
    elif player_sum == 21:
        print("You have black jack. You win!")
        return True


def change_11_to_1_when_sum_above_21(hand: list[int]):
    """Pass in the list to check if above 21. If above 21, does it contain
    11 that can be reduced to 1"""
    while sum(hand) > 21 and 11 in hand:
        hand[hand.index(11)] = 1


def find_winner(dealer_hand: list[int], player_hand: list[int]):
    """Compare the score and decides who wins"""
    dealer_sum = sum(dealer_hand)
    player_sum = sum(player_hand)
    while dealer_sum > 21:
        change_11_to_1_when_sum_above_21(dealer_hand)
        dealer_sum = sum(dealer_hand)
    while player_sum > 21:
        change_11_to_1_when_sum_above_21(player_hand)
        player_sum = sum(player_hand)
    if dealer_sum > 21:
        print("You win!")
    elif player_sum > 21:
        print("You lose!")
    elif dealer_sum == player_sum:
        print("It's a tie!")
    elif player_sum > dealer_sum:
        print("You win!")
    elif player_sum < dealer_sum:
        print("You lose!")


def dealer_hits(dealer_hand: list[int], cards: list[int]):
    dealer_sum = sum(dealer_hand)
    while dealer_sum <= 16:
        dealer_hand.append(random.choice(cards))
        dealer_sum = sum(dealer_hand)
        print(f"Dealer draws a card, they now have {dealer_hand}, "
              f"their sum is {dealer_sum}")


def player_turn(player_hand: list[int], cards: list[int]) -> bool:
    move = ask_next_move()
    while move == "hit":
        player_hand.append(random.choice(cards))
        change_11_to_1_when_sum_above_21(player_hand)
        player_sum = sum(player_hand)
        print(f"You have {player_hand}. Your sum is {player_sum}")
        game_over = player_sum > 21
        if game_over:
            print("You are greater than 21, you lose!")
            return game_over
        move = ask_next_move()
    return game_over


def dealer_turn(dealer_hand: list[int], cards: list[int]) -> bool:
    print(f"Dealer has {dealer_hand[0]} and {dealer_hand[1]}. Their sum is "
          f"{sum(dealer_hand)}.")
    dealer_hits(dealer_hand, cards)
    change_11_to_1_when_sum_above_21(dealer_hand)
    game_over = sum(dealer_hand) > 21
    if game_over:
        print("Dealer is greater than 21. You win!")
    return game_over


if __name__ == "__main__":
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

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    print(cards)

    while True:
        game_over = False

        while not game_over:
            print(logo)
            dealer_hand = []
            player_hand = []
            deal_new_hands(dealer_hand, player_hand, cards)
            game_over = sum_equals_to_21(sum(dealer_hand), sum(player_hand))
            if game_over:
                break
            print(f"You have {player_hand[0]} and {player_hand[1]}. Your sum "
                  f"is {sum(player_hand)}\n"
                  f"Dealer has {dealer_hand[1]}")
            game_over = player_turn(player_hand, cards)
            if game_over:
                break
            game_over = dealer_turn(dealer_hand, cards)
            if game_over:
                break
            find_winner(dealer_hand, player_hand)
            game_over = True

        input("Press ENTER to restart game")
        game_over = False
