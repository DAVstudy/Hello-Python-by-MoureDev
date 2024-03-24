
# Operadores Aritméticos

# Operaciones con números
print(3 + 4)    # Suma
print(3 - 4)    # Resta
print(3 * 4)    # Multiplicación
print(3 / 4)    # División
print(3 % 4)    # Modulo
print(9 // 4)   # División Entera
print(2 ** 8)   # Potenciación


# Operadores con Cadenas de Texto
print("Hola" + " " + "Python")  # Concatenación
print("Hola " + str(5))         # Concatenación


# Operadoraciones Mixtas
print("Hola " * 5)          # Genera el string 5 veces
print("Hola " * (2 ** 3))

my_float = 2.5 * 2
print("Hola " * int(my_float))

# Operadores comparativos (Retorna un booleano dependiendo los argumentos)
print(3 > 4)    # Mayor que
print(3 < 4)    # Menor que
print(3 >= 4)   # Mayor igual que
print(4 <= 4)   # Menor igual que
print(3 == 4)   # Igual a
print(3 != 4)   # Distinto a

# Operaciones con cadenas de texto
print("Hola" > "Python")
print("Hola" < "Python")
print("aaaa" >= "abaa")  # Ordenación alfabética por ASCII
print(len("aaaa") >= len("abaa"))  # Cuenta caracteres
print("Hola" <= "Python")
print("Hola" == "Hola")
print("Hola" != "Python")

# Basada en el Álgebra de Boole
# https://es.wikipedia.org/wiki/%C3%81lgebra_de_Boole

print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" > "Python")
print(3 < 4 or ("Hola" > "Python" and 4 == 4))
print(not (3 > 4))
