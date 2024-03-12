"""
    En python para crear una variable basta con nombrarla y asignarle un valor.
    El tipo de dato de la variable dependera del valor que le asignemos.

    La sintaxis para las variables sera con la escritura 'snake_case' que
    significa todo en minúsculas y se separan las palabras con un guión bajo.
"""

my_string_variable = "My string variable"
print(my_string_variable)

my_int = 100
print(my_int)

my_bool = True
print(my_bool)

# Concatenación de variables en un print
print(my_string_variable, my_int, my_bool)


# Varias variables en una sola linea, peligroso abusar.
name, surname, alias, age = "Diego", "Arenas", "DevsDav", 26

print("Yo soy:", name, surname, ", mi edad es:", age, "y mi alias es:", alias)

# Función input:

name = input('¿Cuál es tu nombre? ')
age = input('¿Cuántos años tienes? ')
print(name)
print(age)
