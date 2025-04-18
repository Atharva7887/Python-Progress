# Strings, Lists & Tuples

# ----- String Operations -----
string1 = "Hello"
string2 = "World"
full_string = string1 + " " + string2
print("Concatenated String:", full_string)

print("Uppercase:", full_string.upper())
print("Lowercase:", full_string.lower())
print("Length of string:", len(full_string))
print("Is 'World' in full_string?:", "World" in full_string)
print("Split string:", full_string.split())

# ----- List Operations -----
my_list = [10, 20, 30, 40, 50]

print("\nOriginal List:", my_list)
my_list.append(60)
print("After append:", my_list)

my_list.insert(2, 25)
print("After insert at index 2:", my_list)

my_list.remove(30)
print("After removing 30:", my_list)

print("Sliced list [1:4]:", my_list[1:4])
print("Length of list:", len(my_list))

# ----- Tuple Operations -----
my_tuple = (1, 2, 3, 4, 5)

print("\nOriginal Tuple:", my_tuple)
print("Element at index 2:", my_tuple[2])
print("Sliced tuple [1:4]:", my_tuple[1:4])
print("Length of tuple:", len(my_tuple))
print("Is 3 in tuple?:", 3 in my_tuple)
