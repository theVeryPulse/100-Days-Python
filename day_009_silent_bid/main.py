#from replit import clear
#HINT: You can call clear() to clear the output in the console.
#from art import logo
#print(logo)

buyers = {}
other_buyer = "yes"

while other_buyer == "yes":
    name = input("Please input your name: ")
    bid = input("How much would you like to bid? ")
    buyers[name] = bid
    other_buyer = input("Are there any other buyer? Please enter 'yes' or 'no': ").lower()
    #clear()

winner = max(buyers, key = buyers.get)
print(f"{winner} wins the bid with {buyers[winner]}.")