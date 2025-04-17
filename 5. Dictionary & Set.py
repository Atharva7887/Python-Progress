# Dictionaries and Sets in Python

# ----- Dictionary Operations -----
my_dict = {
    "name": "Atharva",
    "age": 22,
    "college": "Vishwakarma University"
}

print("Dictionary:", my_dict)
print("Access 'name':", my_dict["name"])

my_dict["age"] = 23  # Update value
print("Updated age:", my_dict["age"])

my_dict["city"] = "Pune"  # Add new key-value
print("Added city:", my_dict)

print("Keys:", my_dict.keys())
print("Values:", my_dict.values())
print("Items:", my_dict.items())

# ----- Set Operations -----
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}

print("\nSet1:", set1)
print("Set2:", set2)

print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Difference (set1 - set2):", set1.difference(set2))

set1.add(8)
print("After adding 8 to set1:", set1)

set1.remove(2)
print("After removing 2 from set1:", set1)
