import random

game = ["rock", "paper", "scissors"]

computer = game[random.randint(0, len(game) - 1)]

player = input("rock, paper or scissors?")

if player == "rock":
    print('''Has elegido:   
        _______
    ---'   ____)
          (_____)
         (_____)
         (____)
    ---.__(___)
    ''')
    if computer == "paper":
        print('''La máguina ha elegido:
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________) 
        ''')
        print("\nHAS PERDIDO")
    elif computer == "scissors":
        print('''La máguina ha elegido:
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
        ''')
        print("\nHAS GANADO")
    else:
        print('''La máguina ha elegido:
        _______
    ---'   ____)
          (_____)
         (_____)
         (____)
    ---.__(___)
        ''')
        print("\nEMPATE")




elif player == "paper":
    print('''Has elegido:   
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    ''')

    if computer == "paper":
        print('''La máguina ha elegido:
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________) 
        ''')
        print("\nEMPATE")
    elif computer == "scissors":
        print('''La máguina ha elegido:
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
        ''')
        print("\nHAS PERDIDO")
    else:
        print('''La máguina ha elegido:
        _______
    ---'   ____)
          (_____)
         (_____)
         (____)
    ---.__(___)
        ''')
        print("\nHAS GANADO")




else:
    print('''Has elegido:   
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    ''')
    if computer == "paper":
        print('''La máguina ha elegido:
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________) 
        ''')
        print("\nHAS GANADO")
    elif computer == "scissors":
        print('''La máguina ha elegido:
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
        ''')
        print("\nEMPATE")
    else:
        print('''La máguina ha elegido:
        _______
    ---'   ____)
          (_____)
         (_____)
         (____)
    ---.__(___)
        ''')
        print("\nPERDIDO")
    










