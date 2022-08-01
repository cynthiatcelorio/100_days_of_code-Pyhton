# Who has more followers on Instagram
from game_data import data
import random

def get_data(num):
    name = data[num]['name']
    follower_count = data[num]['follower_count']
    description = data[num]['description']
    country = data[num]['country']
    print(f"{name}, a {description}, from {country}")
    return follower_count


def select_and_print_account(numA, numB):
    print("A: ")
    followers_A = get_data(numA)
    print("VS\nB:")
    followers_B = get_data(numB)
    if followers_A > followers_B:
        return 'A'
    else:
        return 'B' 


continue_game = True
numA = random.randint(0, len(data) - 1)
numB = random.randint(0, len(data) - 1)
score = 0

while(continue_game == True):
    numA = numB
    numB = random.randint(0, len(data))
    higher = select_and_print_account(numA, numB)

    respuesta = input("\nWho has more followers? Type 'A' or 'B': ")
    if(respuesta == higher):
        continue_game = True
        score += 1
    else:
        print(f"You've lost the game. Final score: {score}")
        continue_game = False



