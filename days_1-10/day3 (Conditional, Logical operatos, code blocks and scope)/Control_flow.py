'''
if condition:
    do this
else:
    do this

Los comparadores son iguales que en java
'''

print("Welcome to the rollercoaste!")
height = int(input("What is your height in cm: "))
if height > 130:
    print("You can ride the rollercoaster!")
else: 
    print("Sorry, you have to grow taller before you can ride")


# Ver si un número es par o impar
number = int(input("Which number do you want to check? "))

if number%2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

# Condiciones anidadas y elif

print("Welcome to the rollercoaste!")
height = int(input("What is your height in cm: "))
if height > 130:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age <= 18:
        print("Please, pay $7")
    elif age > 18 and age < 25:
        print("Please, pay $70")
    else:
        print("Please, pay $12")
else: 
    print("Sorry, you have to grow taller before you can ride")


# BMI 2.0

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
w = float(weight)
h = float(height)
BMI = round(w/h**2)

if BMI < 18.5:
    print(f"Your BMI is {BMI}, you are underweight.")
elif BMI > 18.5 and BMI < 25:
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI > 25 and BMI < 30:
    print(f"Your BMI is {BMI}, you are slightly overweight")
elif BMI > 30 and BMI < 35:
    print(f"Your BMI is {BMI}, you are obese.")
else:
    print(f"Your BMI is {BMI}, you are clinically obese.")


# Calcular si un año es bisiesto

year = int(input("Which year do you want to check? "))

if year%4 == 0:
    if year%100 == 0:   
        if year%400 == 0:
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not leap year")


# Pizza order

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0
# Tamaño pizza
if size == 'S':
    bill += 15
    if add_pepperoni == 'Y':
        bill += 2 
elif size == 'M':
    bill += 20
    if add_pepperoni == 'Y':
        bill += 3 
else:
    bill += 25
    if add_pepperoni == 'Y':
        bill += 3    

if extra_cheese == 'Y':
    bill += 1

print(f"Your final bill is: ${bill}")