from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
maker = CoffeeMaker()
money = MoneyMachine()

is_on = True

while is_on:
    menu_items = menu.get_items()
    user_input = input(f"What would you like to drink? ({menu_items}) ")
    drink = menu.find_drink(user_input)
    if drink is not None:
        if maker.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                maker.make_coffee(drink)

    elif user_input == "report":
        maker.report()
        money.report()
    elif user_input == "off":
        is_on = False
    else:
        print("Sorry, I don't understand that.")