import re
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
maker = CoffeeMaker()

is_on = True

while is_on:
    menu_items = menu.get_items()
    user_input = input(f"What would you like to drink? ({menu_items}) ")

    if re.search(user_input, menu_items):
        print("found drink")
    elif user_input == "report":
        maker.report()
    elif user_input == "off":
        is_on = False
    else:
        print("Sorry, I don't understand that.")