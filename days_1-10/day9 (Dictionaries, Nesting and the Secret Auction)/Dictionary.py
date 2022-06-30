# {Key: Value}

programming_dictionary = {
    "Bug": "An error in a program that..",
    "Function": "A piece of code that..."
}

# Retrieveving items from dictionary
print(programming_dictionary["Bug"])

# Adding new items to dictionary
programming_dictionary["Loop"] = "The action of doing..."
print(programming_dictionary)

# Create an empty dictionary
empty_dictionary = {}

# Wipe an existing dictionary
programming_dictionary = {}
print(programming_dictionary)

# Edit an item in a dictionary
programming_dictionary["Bug"] = "An error bla bla bla"

# Loop throught a dictionary
for key in programming_dictionary:
    print(key)     # Keys
    print(programming_dictionary[key])     # Values


# Grading program

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for key in student_scores:
    if student_scores[key] > 90:
        student_grades[key] = "Outstanding"
    elif student_scores[key] > 80 and student_scores[key] < 91:
        student_grades[key] = "Exceeds Expectations"
    elif student_scores[key] > 70 and student_scores[key] < 81:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail" 

print(student_grades)

# Nesting

capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"]},     # List inside dict, inside dict
    "Germany": ["Berlin", "Hamburg"]
}

# ["A", "B", ["C", "D"]]   Like JSON xd

# Añadir un diccionario a una lista de diccionarios

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

    # Creamos un país vacío (diccionario) y le vamos introduciendo los diferentes datos, después lo añadimos a la lista

def add_new_country(country, visits, cities):
    new_country = {}
    new_country["country"] = country
    new_country["visits"] = visits
    new_country["cities"] = cities
    travel_log.append(new_country)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)


# Revisar test sección 9 si tengo alguna duda