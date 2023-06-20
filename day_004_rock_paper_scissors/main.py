import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
RPS = [rock, paper, scissors]
player_choice = int (input ("Let's play rock, paper, scissors. Input 0 for rock, 1 for paper, and 2 for scissors: "))
print (RPS[player_choice])

computer_choice = random.randint (0,2)
print (RPS[computer_choice])

computer_wins = "You lost, computer wins!"
player_wins = "You win!"

if player_choice == computer_choice:
  print ("It's a tie!")
else:
  if (player_choice == computer_choice + 1) or (player_choice == 2 and computer_choice == 0):
    print (computer_wins)
  else:
    print (player_wins)
input ("press any key to exit")