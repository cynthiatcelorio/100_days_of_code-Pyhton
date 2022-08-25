from menu import MENU
import os

# Initial ingredients

available_ingredients = {
    "water": 1000,
    "milk": 1000,
    "coffee": 200
}

# Initialized variables

machine = "on"

# Functions

def check_ingredients(drink):           # Function to check if there are ingredients available to make the drink
    return MENU[drink]["ingredients"]["water"] < available_ingredients["water"] and MENU[drink]["ingredients"]["coffee"] < available_ingredients["coffee"] and MENU[drink]["ingredients"]["milk"] < available_ingredients["milk"]


def reduce_ingredients():               # Function to reduce the number of available ingredients
    available_ingredients["coffee"] -= MENU[drink]["ingredients"]["coffee"]
    available_ingredients["water"] -= MENU[drink]["ingredients"]["water"]
    available_ingredients["milk"] -= MENU[drink]["ingredients"]["milk"]


while machine != "off":
    
    # Cleaning screen
    os.system('cls')

    drink = input("What would you like? (espresso/latte/cappuccino): ")

    # Introduce "report" to see available ingredients
    if drink == 'report':
        print(available_ingredients)
    else:
        if check_ingredients(drink):
            drink_cost = MENU[drink]["cost"]
            money = float(input("Please insert coins: "))
            if money >= drink_cost:
                reduce_ingredients()
                print("Here is you coffee.")
                print(f"The machine gives you {money - drink_cost} euros back.")
            else: 
                print("The amount is insufficient.")
        else:
            print("Sorry, there are not enough ingredients")

    machine = input("Would you like another drink? ('on' to continue, 'off' to finish) :")
    
    
   
        



    

