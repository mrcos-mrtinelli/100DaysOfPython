MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0.0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_enough_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, we do not have enough {item}")
            return False
    return True


def process_coins(drink):
    coins = {
        "Quarters": 0.25,
        "Dimes": 0.10,
        "Nickels": 0.05,
        "Pennies": 0.01
    }
    total_cost = drink["cost"]
    money_provided = 0.0

    for coin in coins:
        number_of_coins = input(f"How many {coin} do you have? ")
        money_provided = money_provided + (float(number_of_coins) * coins[coin])

    return money_provided


def is_transaction_successful(money, drink_cost):
    if money < drink_cost:
        return False
    elif money > drink_cost:
        change = money - drink_cost
        print(f"Transaction successful. \nYour change is ${'%.2f' % change}.")
    else:
        print("Transaction successful.")

    global profit
    profit += drink_cost
    return True


def make_drink(drink):
    ingredients = MENU[drink]["ingredients"]
    for item in ingredients:
        global resources
        resources[item] -= ingredients[item]

    print(f"Here is your {drink} ☕️ Enjoy!")


is_on = True

while is_on:
    response = input("What would you like? ")
    if response == "off":
        is_on = False
    elif response == "report":
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: {profit}")
    elif response in MENU:
        if is_enough_resources(MENU[response]["ingredients"]):
            payment = process_coins(MENU[response])
            if is_transaction_successful(payment,MENU[response]["cost"]):
                make_drink(response)
    else:
        print("I don't understand that.")
