import random

# initialize

deck = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13]
player = [random.choice(deck), random.choice(deck)]
dealer = [random.choice(deck), random.choice(deck)]
player_sum, dealer_sum = 0, 0
another_card = 'y'

for card in player:
    player_sum += card

for card in dealer:
    dealer_sum += card

# add cards functions

def player_add_card(player_sum):
    new_player_card = random.choice(deck)
    deck.remove(new_player_card)
    player.append(new_player_card)
    player_sum += new_player_card
    return player_sum

def dealer_add_card(dealer_sum):
    new_dealer_card = random.choice(deck)
    deck.remove(new_dealer_card)
    dealer.append(new_dealer_card)
    dealer_sum += new_dealer_card
    return dealer_sum

# game

while another_card == 'y' and player_sum < 22 and dealer_sum < 21:

    print(f"Your cards: {player}")
    print(f"Computer's first card: {dealer[-1]}")
    another_card = input("Type 'y' to get another card, type 'n' to pass: ")
    if another_card == 'y':
        player_sum = player_add_card(player_sum)
    if player_sum < 17 and dealer_sum < 16:
        dealer_sum = dealer_add_card(dealer_sum) 

# results

if dealer_sum == player_sum:
    print("Draw")
elif player_sum > 21:
    print("You lose!!")
elif dealer_sum > 21:
    print("You win!!")
elif dealer_sum > player_sum:
    print("You lose!!")
else:
    print("You win!!")


print(f"Your final hand: {player}")
print(f"Computer's final hand: {dealer}")






