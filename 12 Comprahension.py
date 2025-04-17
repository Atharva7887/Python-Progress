#Comprehensions
# List comprehension
squares = [x**2 for x in range(10)]
print("List comprehension (squares):", squares)

squares = [x**2 for x in range(10)]
print("Squares:", squares)

even_numbers = [x for x in range(20) if x % 2 == 0]
print("Even numbers:", even_numbers)

words = ["python", "rocks", "awesome"]
capitalized = [word.upper() for word in words]
print("Capitalized:", capitalized)


# Dictionary comprehension
squares_dict = {x: x**2 for x in range(10)}
print("Dictionary comprehension (squares):", squares_dict)

# Set comprehension
squares_set = {x**2 for x in range(10)}
print("Set comprehension (squares):", squares_set)

# Generator expression
squares_gen = (x**2 for x in range(10))
print("Generator expression (squares):", list(squares_gen))