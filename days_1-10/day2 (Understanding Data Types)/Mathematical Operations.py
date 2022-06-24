# Al hacer una division SIEMPRE lo va a convertir a float

# Potencia 2^3
print(2 ** 3)

# IMC Calculator que lo devualva en un int

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
w = float(weight)
h = float(height)
BMI = (w/h**2)
print(int(BMI))

# Redondear números, en el segundo parámetro se pone cuántos decimales
print(round(8 / 3, 2))

# Si queremos un entero al hacer una división sin convertirlo usamos //
print(8 // 3)

# Aumentar un valor
score = 0
score += 1

# Imprimir valores de diferentes tipos -> f-String
# Una f antes del String
print(f"Your score is {score} and your height is {height}")

# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old
age = input("What is your current age?")
total_days = 90*365
total_weeks = 90*52
total_months = 90*12
days = int(age)*365
weeks = int(age)*52
months = int(age)*12

print(f"You have {total_days - days} days, {total_weeks - weeks} weeks, and {total_months - months} months left")
