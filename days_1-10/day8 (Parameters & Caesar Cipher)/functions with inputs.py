# One input
def greet(name):
    print("Hello, " + name)

name = input("Write your name: ")
greet(name)

# More tha one input
def greet_with(name, location):
    print(f"Hello, {name}, what is it like in {location}?")

greet_with(name, input("Where are you from? "))

greet_with("Cynthia", "London")


# You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. 

def paint_calc(height, width, cover):
    num_cans = round(height*width/cover)
    print(f"You'll need {num_cans} cans of paint.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


# Prime numbers
def prime_checker(number):
    prime = True
    for i in range(2, int(number/2)):
        if number%i == 0:
            prime = False
    if prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)