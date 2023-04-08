# This is a number guessing game. The player will have to guess a number between 1 and 100.
import random

logo = '''
  _   _                 _                  _____                     
 | \ | |               | |                / ____|                    
 |  \| |_   _ _ __ ___ | |__   ___ _ __  | |  __ _   _  ___  ___ ___ 
 | . ` | | | | '_ ` _ \| '_ \ / _ \ '__| | | |_ | | | |/ _ \/ __/ __|
 | |\  | |_| | | | | | | |_) |  __/ |    | |__| | |_| |  __/\__ \__ \\
 |_| \_|\__,_|_| |_| |_|_.__/ \___|_|     \_____|\__,_|\___||___/___/'''

print(logo)


# check the guess against the correct number, return True if the game is over, guessed right or out of life
def check(correct_num: int, guess_num: int, left_guess: int):
    """Check the guess. Return True if the game is over, either guess is right or out of life"""
    if guess_num != correct_num:
        left_guess -= 1
    if left_guess == 0:
        print("You guessed wrong. You ran out of guesses, you lose.")
        return True
    if guess_num > correct_num:
        print("Too big, guess again")
        return False
    elif guess_num < correct_num:
        print("Too small, guess again")
        return False
    else:
        print(F"You guessed right! The correct number is {correct_num}! You win!")
        return True

    
game_over = False
while not game_over:
    number = random.randint(1, 100)
    # print(number)    # Debug

    # Ask for game difficulty
    diff = input("Guess a number between 1 and 100, including 1 and 100. Do you want to play easy mode or hard mode? ").lower()
    while diff != "easy" and diff != "hard":
        input("I do not understand, please input again.").lower()
    if diff == "easy":
        life = 10
    else:
        life = 5
    print(F"You have chosen {diff} mode. You can guess {life} times.")

    # Game loop
    while life > 0:
        # Ask for guess, check if the input is an integer between 0 and 100, including 0 and 100
        while True:
            guess = input("\nGuess a number: ")
            try:
                guess = int(guess)
            except:
                print("It doesn't look like an integer. Please input an integer.")
                continue
            else:
                guess = int(guess)
                if 1 <= guess <= 100:
                    break
                else:
                    print("Please input a number between 0 and 100, including 0 and 100.")

        # check the guess against the correct number.
        game_over = check(number, guess, life)
        if game_over:
            break
        life -= 1
        print(F"You still have {life} guesses.")
        
    # Ask if the player wants to play again
    input("Press any key to restart")
    game_over = False
