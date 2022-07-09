# Local Scope (Inside Functions)
# Global Scope 
'''
enemies = 1

def increase_enemies():
    enemies += 1
    print(f"Enemies inside function: {enemies}")

increase_enemies()
print(f"Enemies outside function: {enemies}") # It fails cause it's declared inside the function

'''

# solution

enemies = 1

def increase_enemies():
    global enemies
    enemies += 1
    print(f"Enemies inside function: {enemies}")

increase_enemies()
print(f"Enemies outside function: {enemies}")

# Be careful with the use of global variables

# Constants

pi = 3.14159