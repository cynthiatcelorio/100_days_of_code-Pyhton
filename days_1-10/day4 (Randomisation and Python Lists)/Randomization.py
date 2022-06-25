import random

'''
randint(a, b) returns a random integer between a and b (both inclusive)

random.random() para float, de [0 a 1)

'''

random_integer = random.randint(1, 23)
print(random_integer)

random_float = random.random()
print(random_float)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")

# Heads and Tails con seed

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

if random.randint(0,1) == 1:
    print("Heads")
else:
    print("Tails")