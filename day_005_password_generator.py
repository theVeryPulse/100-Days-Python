#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""
# add expected number of letters to the string
for i in range(nr_letters):
  password += random.choice(letters)
  print(password)

# add expected number of symbols to the string
for i in range(nr_symbols):
  password += random.choice(symbols)
  print(password)

#add expected number of numbers to the string
for i in range(nr_numbers):
  password += random.choice(numbers)
  print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password = list(password)
print(password)
scrambled_password = ""
while password != []:
  ran_index = random.randint(0,len(password)-1)
  print(f"ran_index is: {ran_index}")
  scrambled_password += password[ran_index]
  print(f"scrambled_password is {scrambled_password}")
  password.pop(ran_index)
  print(f"password is {password}")