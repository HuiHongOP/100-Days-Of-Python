from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()


machine_on = True

while machine_on:
    options = menu.get_items()
    user_choice = input(f"What would you like? ({options}): ").lower()
    if user_choice == 'off':
        machine_on = False
    elif user_choice == 'report':
        coffee_machine.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_choice)
        if coffee_machine.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)