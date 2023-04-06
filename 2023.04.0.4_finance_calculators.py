# Purpose: To calculate the amount of interest you'll earn on your investment
#          or the amount you'll have to pay on a home loan

import math

print("""
investment - to calculate the amount of interest you'll earn on your investment
bond       - to calculate the amount you'll have to pay on a home loan
""")

# Either investment or bond?
type = ""
type = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()
while type != "investment" and type != "bond":
    type = input("Sorry I don't understand. Please enter 'investment' or 'bond': ").lower()


if type == "investment":
    # Ask investment type
    interest = input("Do you want simple or compound interest? (Enter 'simple' or 'compound')\n").lower()
    while interest != "simple" and interest != "compound":
        interest = input("Sorry I don't understand. Please enter 'simple' or 'compound':\n").lower()

    # Ask for basic investment information
    deposit = float(input("How much are you depositing?\n"))
    interest_rate = float(input("What is the annual interest rate? (Enter the number. For example, enter '8' for 8%))\n"))
    interest_rate = interest_rate / 100
    years = int(input("How many years do you plan on investing?\n"))

    # Calculate and display the interest
    if interest == "simple":
        total_amount = deposit * (1 + interest_rate * years)
        print("You will earn R{:.2f} in interest.".format(total_amount - deposit))
    else:    # interest == "compound"
        total_amount = deposit * math.pow((1 + interest_rate / 12 ), years * 12)
        print("You will earn R{:.2f} in interest (by default, monthly compound).".format(total_amount - deposit))

# type == "bond"
else:
    # Ask for basic bond information
    house_value = float(input("What is the present value of the house?\n"))
    interest_rate = float(input("What is the annual interest rate? (Enter the number. For example, enter '8' for 8%))\n"))
    interest_rate = interest_rate / 100 / 12
    months = int(input("How many months do you plan to take to repay the bond?\n"))

    # Calculate and display the repayment
    repayment = house_value * (interest_rate * (1 + interest_rate) ** months) / ((1 + interest_rate) ** months - 1)
    print("You will need to pay R{:.2f} each month.".format(repayment))

# End
