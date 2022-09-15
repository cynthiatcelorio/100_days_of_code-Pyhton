
class MenuItem:
    instances = []
    def __init__(self, name, cost, ingredients):
        self.name = name
        self.cost = cost
        self.ingredients = ingredients
        self.__class__.instances.append(self)

# I could have created a class for the ingredients, but I ended up integrating them into the coffee maker

'''class Ingredients:
    instances = []
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
        self.__class__.instances.append(f"{self.name} : {self.amount}")'''


class Menu:
    def get_items():
        # Returns all the names of the availablee menu items as a concatenated string
        for item in MenuItem.instances:
            return item.name

    def find_drink(self, order_name):
        # Searches the menu for a particular drink by name. Returns a MenuItem object if it exists,otherwise returns None

        for item in MenuItem.instances:
            if item.name == order_name:
                return item

class CoffeeMaker:
    def __init__(self):
        self.resources = {
            "water": 1000,
            "milk": 1000,
            "coffee": 200,
        }

    def report(self):
        print(self.resources)
    
    def is_resource_sufficient(self, drink):
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print("Here is your coffee")






