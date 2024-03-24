
# STRINGS

my_string = "Mi String"
my_other_string = 'Mi otro String'

print(len(my_string))   # Longitud del string
print(len(my_other_string))

print(my_string + " " + my_other_string)    # Concatenación de strings

my_new_line_string = "Este es un String \ncon salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación"
print(my_tab_string)

my_scape_string = "\\tEste es un String \n escapado"
print(my_scape_string)

# Formateo

name, surname, age = "Diego", "Arenas", 26
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" % (name, surname, age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")


# Desenpaqutar caracteres

language = "Python"
a, b, c, d, e, f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# División

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

# Reverse
reversed_language = language[::-1]
print(reversed_language)

# Funciones

print(language.capitalize())  # Mayuscula a la primera letra
print(language.upper())  # todos los carateres en mayus
print(language.count("t"))  # Cuenta los caracteres iguales al argumento
print(language.isnumeric())
print("1".isnumeric())
print(language.lower().isupper())
print(language.startswith("Py"))
