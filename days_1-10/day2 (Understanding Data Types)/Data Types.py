# Data types

#String
print("Hello"[0])

#Integer
print(123 + 123)

    #Podemos poner 123_456_789 y va a ignorar los _, pondrá 123456789

#Float
print(3.14)

#Boolean
print(True)
print(False)


'''
num_char = len(input("What is your name? "))
print("Your name has " + num_char + " characters.")

Esto va a dar error porque no permite unir un entero a una cadena de caracteres
Para ello usamos:
'''

# Con esto vemos el tipo de la variable
num_char = len(input("What is your name? "))
print(type(num_char))

# Así cambiamos el tipo a String
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")

# Otras conversiones, convertimos a float un integer
a = float(123)

# Ejemplo de sumar los dígitos de un número de dos cifras
two_digit_number = input("Type a two digit number: ")

number = int(two_digit_number)         #Hay que convertir de string a int
decena = int(number/10)                #Tenemos que poner int porque si no los hace float al dividirlos
unidad = int(number%10)
total = decena + unidad

print(total)