# Who has more followers on Instagram
from game_data import data
import random

def get_followers(num):
    follower_count = data[num]['follower_count']
    return follower_count

def toString(num):
    name = data[num]['name']
    description = data[num]['description']
    country = data[num]['country']
    return f"{name}, a {description}, from {country}"


def select_and_print_account(numA, numB):
    print(f"A: {toString(numA)}")
    followers_A = get_followers(numA)
    print(f"VS\nB: {toString(numB)}")
    followers_B = get_followers(numB)


    if followers_A > followers_B:
        return 'A'
    else:
        return 'B' 


continue_game = True
numB = random.randint(0, len(data) - 1)
score = 0

while(continue_game == True):
    print(f"The A account has {get_followers(numB)} followers.")
    numA = numB
    numB = random.randint(0, len(data))
    higher = select_and_print_account(numA, numB)

    respuesta = input("\nWho has more followers? Type 'A' or 'B': ")
    print("\n\n")
    if(respuesta == higher):
        continue_game = True
        score += 1
    else:
        print(f"You've lost the game. Final score: {score}")
        continue_game = False

    

