import os
clear = lambda: os.system('cls')

bidders = {}

are_there_bidders = True


while are_there_bidders:
    clear()
    bidder = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    
    bidders[bidder] = bid

    if input("Are there any other bidders? (yes/no): ") == "no":
        are_there_bidders = False

winner = ""
max = 0
for key in bidders:
    if bidders[key] > max:
        max = bidders[key]
        winner = key

print(f"The winner is {winner} with a bid of ${max}.")

