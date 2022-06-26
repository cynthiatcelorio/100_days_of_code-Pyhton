'''
for item in list_of_items:
    # Do something to each item
    Es como un for each
'''

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")

# Calcular la media de las alturas contenidas en una lista
# Metemos los datos en una lista
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

suma = 0 
cont = 0
for height in student_heights:
    suma += height
    cont += 1

print(round(suma/cont))


# Mayor número de un array
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

mayor = 0
for score in student_scores:
    if score > mayor:
        mayor = score

print(f"The highest score in the class is: {mayor}")


'''
for number in range(a, b):
    print(number)
'''

for number in range(1, 10):       # No incluye el último, el 10
    print(number)                 # Va de uno en uno

for number in range(1, 11, 3):    # Crece de 3 en 3 (1, 4, 7, 10)
    print(number)    

total = 0
for number in range(1, 101):
    total += number
print(total)


# Sumar los números pares del 1 al 100
total = 0
for number in range(1, 101):
    if(number%2 == 0):
        total += number

print(total)

'''
Your program should print each number from 1 to 100 in turn.

When the number is divisible by 3 then instead of printing the number it should print "Fizz".

When the number is divisible by 5, then instead of printing the number it should print "Buzz".`

And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"
'''

for number in range(1, 101):
    if number%3 == 0 and number%5 != 0:
        print("Fizz")
    elif number%5 == 0 and number%3 != 0:
        print("Buzz")
    elif number%5 == 0 and number%3 == 0:
        print("FizzBuzz")
    else:
        print(number)
