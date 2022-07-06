# Calculator combining dictionaries and functions

def add(num1, num2):
    return num1 + num2

def divide(num1, num2):
    return num1 / num2

def multiply(num1, num2):
    return num1 * num2

def substract(num1, num2):
    return num1 - num2

num1 = int(input("What's the first number? "))
op = input("Pick an operation: ")
num2 = int(input("What's the second number? "))

operation = {
    "+": add(num1, num2),
    "/": divide(num1, num2),
    "*": multiply(num1, num2),
    "-": substract(num1, num2)
}

print(f"{num1} {op} {num2} = {operation[op]}")