from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
maker = CoffeeMaker()

is_on = True

while is_on:
    user_input = input("What would you like to drink? ")

    if user_input == "report":
        maker.report()
    elif user_input == "menu":
        menu_str = menu.get_items()
        print(menu_str)
    elif user_input == "off":
        is_on = False
    else:
        print("Sorry, I don't understand that.")