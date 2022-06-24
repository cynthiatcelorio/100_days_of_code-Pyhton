print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
percentage = float(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = float(input("How many people to split the bill? "))
total = bill/percentage + bill
person = total/people

print(f"Each person should pay: ${round(person, 2)}")
