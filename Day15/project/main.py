MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            # "milk":0 #no milk 
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
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money_in_machine = 0

def report():
    for source in resources:
        print(f"{source}:{resources[source]}")
    print(f"Money:${money_in_machine}")

machine_on = True
def check_sufficient(flavor):
    for key in MENU[flavor]["ingredients"]:
        if resources[key] < MENU[flavor]["ingredients"][key]:
            return f"Sorry there is not enough {key}"
    return True

def process_coins():
    print("Input Your Coins")
    Quarter = float(input("Insert your Quarters:"))*0.25
    dimes = float(input("Insert your dimes:")) * 0.10
    nickels = float(input("Insert your nickels:")) * 0.05
    pennies = float(input("Insert your pennies:")) * 0.01

    total_coin = Quarter + dimes + nickels +pennies

    return total_coin

def crosscheckPayment(coins,user_input):
    global money_in_machine
    if coins == MENU[user_input]["cost"]:
        money_in_machine+=coins
        return f"Here is your {user_input}! enjoy"
    elif coins >= MENU[user_input]["cost"]:
        change = (coins) - (MENU[user_input]["cost"])
        money_in_machine+=MENU[user_input]["cost"]
        return f"Here is your {user_input} and change:${round(change,2)} Enjoy"
    # elif coins < MENU[user_input]["cost"]:
    else:
        return "Sorry that's not enough money, Money refunded"

while machine_on:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_input in MENU:
        sufficiency_check = check_sufficient(user_input) 
        if sufficiency_check == True:
            coins = process_coins()
            check = crosscheckPayment(coins,user_input)
            print(check)
            if check == f"Here is your {user_input}":
                for key in MENU[user_input]["ingredients"]:
                    resources[key]-=MENU[user_input]["ingredients"][key]
        else:
            print(sufficiency_check)
    elif user_input == "off":
        machine_on = False
    elif user_input == "report":
        report()