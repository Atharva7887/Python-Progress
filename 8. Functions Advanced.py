# Function with arguments and return

def greet(name):
    return f"Hello, {name}!"

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(greet("Atharva"))
print("Factorial of 5:", factorial(5))

# Default and keyword arguments
def power(base, exponent=2):
    return base ** exponent

print("Power (default exponent):", power(3))
print("Power (3^4):", power(3, 4))
