# Lo voy a hacer de dos maneras, una poniendo los caracteres desordenados y otra ordenados por su tipo
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")
num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like?\n"))
num_numbers = int(input("How many numbers would you like?\n"))

sum_elements = num_letters + num_symbols + num_numbers

# Con el String lo hacemos para que salgan en orden, letras, números y símbolos
password = ""
# Con una lista lo hacemos para que sea random
password_list = []

for letter in range(1, num_letters + 1):
    password += letters[random.randint(0 , 51)]
    password_list.append(letters[random.randint(0 , 51)])

for number in range(1, num_numbers + 1):
    password += numbers[random.randint(0 , 9)]
    password_list.append(numbers[random.randint(0 , 9)])

for symbol in range(1, num_symbols + 1):
    password += symbols[random.randint(0 , 8)]
    password_list.append(symbols[random.randint(0 , 8)])
    
random.shuffle(password_list)
shuffled_password = ""

for char in password_list:
    shuffled_password += char

print("Contraseña ordenada: " + password)
print("Contraseña desordenada: " + shuffled_password)
