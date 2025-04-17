#Functions
# Sorted function
list1 = [3, 1, 4, 1, 5]
sorted_list = sorted(list1)
print("Sorted function:", sorted_list)

# Reversed function
reversed_list = list(reversed(list1))
print("Reversed function:", reversed_list)

# Sum function
sum_list = sum(list1)
print("Sum function:", sum_list)

# Lambda function
add = lambda x, y: x + y
print("Lambda function (addition):", add(a, b))

# Map function
squared_map = list(map(lambda x: x**2, range(10)))
print("Map function (squared):", squared_map)

# Filter function
even_filter = list(filter(lambda x: x % 2 == 0, range(10)))
print("Filter function (even numbers):", even_filter)

# Reduce function
from functools import reduce
sum_reduce = reduce(lambda x, y: x + y, range(10))
print("Reduce function (sum):", sum_reduce)

# Zip function
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = list(zip(list1, list2))
print("Zip function:", zipped)

# Enumerate function
list1 = ['a', 'b', 'c']
enumerated = list(enumerate(list1))
print("Enumerate function:", enumerated)

# Min and Max functions
min_value = min(list1)
max_value = max(list1)
print("Min function:", min_value)
print("Max function:", max_value)

# Length function
length = len(list1)
print("Length function:", length)

# Type function
type_value = type(list1)
print("Type function:", type_value)