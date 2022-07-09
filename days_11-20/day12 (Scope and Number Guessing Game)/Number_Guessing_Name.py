import random

def set_difficulty(difficulty):
    if difficulty == "easy":
        return 10
    elif difficulty == "hard":
        return 5

high, low = 0, 100
guessed = False
number_to_guess = random.randint(1, 100)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
attempts = set_difficulty(difficulty)

while guessed == False and attempts > 0:
    print(f"You have {attempts} attemps remaining to guess the number.\nThe number to guess is between {high} and {low}")
    player = int(input("Make a guess: "))
    if player < number_to_guess:
        high = player
    elif player > number_to_guess:
        low = player
    else:
        guessed = True
    attempts -= 1

if guessed == False:
    print(f"You've run out of guesses, you lose. The number was {number_to_guess}")
else:
    print("You win!!")
