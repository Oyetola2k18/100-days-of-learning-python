from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()


machine_on = True

while machine_on:
    options = menu.get_items()
    choice = input(f"What would you like ({options})").lower()

    if choice == "off":
        machine_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)#To check if the drink the user inputed exists
        sufficient=coffee_maker.is_resource_sufficient(drink)
        if sufficient:
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
            

