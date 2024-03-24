# Listas

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [26, 28, 30, 12, 17, 20, 29]

print(my_list)
print(len(my_list))

my_other_list = [26, 1.67, "Diego", "Arenas"]

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])

print(my_other_list.count("Diego"))
print(my_list.count(30))

age, height, name, surname = my_other_list
print(name)

# Creación, inserción, actualización y eliminación

my_other_list.append("MoureDev")
print(my_other_list)

my_other_list.insert(1, "Rojo")
print(my_other_list)

my_other_list[1] = "Azul"
print(my_other_list)

my_other_list.remove("Azul")
print(my_other_list)

my_list.remove(30)
print(my_list)

print(my_list.pop())
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

del my_list[2]
print(my_list)

# Operaciones con listas

my_new_list = my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

# Sublistas

print(my_new_list[1:3])

# Cambio de tipo

my_list = "Hola Python"
print(my_list)
print(type(my_list))
