# For Loop
print("For loop:")
for i in range(5):
    print("i =", i)

# While Loop
print("\nWhile loop:")
count = 0
while count < 3:
    print("count =", count)
    count += 1

# Break and Continue
print("\nBreak and Continue:")
for num in range(10):
    if num == 5:
        break
    if num % 2 == 0:
        continue
    print("Odd number:", num)
