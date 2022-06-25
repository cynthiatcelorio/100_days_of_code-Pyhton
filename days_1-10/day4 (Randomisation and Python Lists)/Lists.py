import random
# En una lista se pueden almacenar datos de diferentes tipos

comunidades_autonomas = ["Galicia", "Valencia", "Cataluña", "Madrid", "Andalucía", "Extremadura"]

print(comunidades_autonomas[0])   # Devuelve el primero, obviamente
print(comunidades_autonomas[-1])  # Devuelve el último, -2 pues el penúltimo etc

comunidades_autonomas[0] = "Galiza"  # Lo cambia

print(comunidades_autonomas[0]) 

comunidades_autonomas.append("Melilla")  # Añade un nuevo elemento al final
comunidades_autonomas.extend(["Ceuta", "Rusia"]) # Añade varios

#En la documentación de python hay muchas más cosas de estas

# Banker Roulette

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

print(f"{names[random.randint(0, len(names) - 1)]} is going to buy the meal today!")



# Treasure Map


row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

#seleccionamos la fila
row = map[int(position[1]) - 1]

row[int(position[0]) - 1] = "X"
map[int(position[1]) - 1] = row

print(f"{row1}\n{row2}\n{row3}")