import random
from hangman_art import art

word_list = ["GUYBRUSH", "LECHUCK", "ELAINE", "WALLY", "LARGO", "MURRAY"]
word = word_list[random.randint(0, len(word_list) - 1)]
game_word = "_" * len(word)

game_over = False
lives = len(art) - 1
print(game_word)

while not game_over:
    guess = input("Guess a letter: ")
    
    if guess in game_word:
        print(f"You've already guessed {guess}")

    # comprobar si está esa letra y sustituirla
    for i in range(len(word)):
        if guess == word[i]:
            lst = list(game_word)
            lst[i] = guess
            game_word = ''.join(lst)

    if guess not in word:
        lives -= 1
    print(art[lives])    
    print(game_word + "\n")

    # comprobar game_over
    if lives == 0 or not "_" in game_word:
        game_over = True

    if game_over: 
        if not "_" in game_word:
            print("Congratulations, you win")
        else:
            print("You lost, the word was: " + word)


  

















