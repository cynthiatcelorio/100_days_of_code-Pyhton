import coffee_machine_POO
import os

# Creating menu items

espresso = coffee_machine_POO.MenuItem("espresso", 1.5, {"water": 50, "milk": 0, "coffee": 18})
latte = coffee_machine_POO.MenuItem("latte", 2.5, {"water": 200, "milk": 150, "coffee": 24})
cappuccino = coffee_machine_POO.MenuItem("cappuccino", 3.0, {"water": 250, "milk": 100, "coffee": 24})

# Resources
# coffee_machine_POO.CoffeeMaker.initialIngredients()

coffee_machine = coffee_machine_POO.CoffeeMaker()
menu = coffee_machine_POO.Menu()







machine = "on"
while machine != "off":
    
    # Cleaning screen
    os.system('cls')
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    # Introduce "report" to see available ingredients
    if choice == "report":
        coffee_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_machine.is_resource_sufficient((drink)):
            coffee_machine.make_coffee(drink)
        else:
            print("Sorry, there are not enough ingredients")

    machine = input("Would you like another drink? ('on' to continue, 'off' to finish) :")