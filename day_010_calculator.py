logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

print(logo)

def add(num1, num2):
    """Return the sum of two numbers"""
    return num1 + num2
def substract(num1, num2):
    """Return the difference of num1 minues num2"""
    return num1 - num2
def multiply(num1, num2):
    """Return the product of two numbers multiplying"""
    return num1 * num2
def divide(num1, num2):
    """Return the quotient of num1 divided by num2"""
    return num1 / num2

calc_dict = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}

while True:
    calc_type = input("Which type of calculation do you want to do? Input + for addition, - for substraction, * for multiply, and / for division\n").upper()
    if calc_type not in calc_dict:
        print("Wrong input.")
        continue
    num1 = float(input("Please input first number: "))
    num2 = float(input("Please input second number: "))
    outcome = calc_dict[calc_type](num1, num2)
    print(f"{num1}{calc_type}{num2}={outcome}")
    input("Press any key to continue")
