def add(a: float, b: float):
    """Returns (a + b)"""
    return a + b


def subtract(a: float, b: float):
    """Returns (a - b)"""
    return a - b


def multiply(a: float, b: float):
    """Returns (a * b)"""
    return a * b


def divide(a: float, b: float):
    """Return (a / b)"""
    return a / b


if __name__ == '__main__':

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

    calc_dict = {"+": add, "-": subtract, "*": multiply, "/": divide}
    while True:
        calc_type = input("Which type of calculation do you want to do? Input "
                          "+ for addition, - for subtraction, * for multiply, "
                          "and / for division\n").upper()
        if calc_type not in calc_dict:
            print("Wrong input.")
            continue
        num1 = float(input("Please input first number: "))
        num2 = float(input("Please input second number: "))
        if calc_type == '/' and num2 == 0:
            print("0 divide error.")
            continue
        outcome = calc_dict[calc_type](num1, num2)
        print(f"{num1}{calc_type}{num2}={outcome}")
        input("Press Enter to continue")
