# Tuplas

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (26, 1.67, "Diego", "Arenas")
my_other_tuple = (20, 30, 40)
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
# print(my_tuple[4])  IndexError
# print(my_tuple[-6]) IndexError

print(my_tuple.count("Diego"))
print(my_tuple.index("Arenas"))

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3: 5])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple.insert(1, "Morado")
print(tuple(my_tuple))

# Eliminación

# del my_tuple[2] TypeError: 'tuple' object doesn't support item deletion

del my_tuple
# print(my_tuple) NameError: name 'my_tuple' is not defined
