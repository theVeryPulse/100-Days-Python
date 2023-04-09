from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

operating = True

# operation loop
while operating:

    # service loop
    while True:
        user_input = input(F"\nWhat would you like? ({menu.get_items()}):\n").lower()

        ###########################
        #    maintenance mode     #
        if user_input == 'report':
            coffee_maker.report()
            money_machine.report()
            continue
        elif user_input == 'off':
            print("Turning off...")
            operating = False
            break
        #     maintenance mode    #
        ###########################

        choice = menu.find_drink(user_input)
        if choice is None:
            continue
        if not coffee_maker.is_resource_sufficient(choice):
            continue

        print(F"Choice: {choice.name}\n"
              F"cost: {choice.cost}\n")

        pay_success = money_machine.make_payment(choice.cost)

        if not pay_success:
            continue

        coffee_maker.make_coffee(choice)
