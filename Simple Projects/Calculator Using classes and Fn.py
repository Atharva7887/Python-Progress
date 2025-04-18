
import time

class Calculator:
    def __init__(self, n):
        self.n = n

    @staticmethod
    def greet():
        print("Hello! I'm here to help you with some calculations...")
        time.sleep(0.5)

    def square(self):
        result = self.n ** 2
        print(f"{self.n} squared is {result}")
        return result

    def multiply(self):
        p = int(input("Enter a number to multiply: "))
        result = self.n * p
        print(f"{self.n} multiplied by {p} is {result}")
        return result

    def divide(self):
        p = int(input("Enter a number to divide: "))
        if p == 0:
            print("Oops! Cannot divide by zero.")
            return None
        result = self.n / p
        print(f"{self.n} divided by {p} is {result}")
        return result

    def add(self):
        p = int(input("Enter a number to add: "))
        result = self.n + p
        print(f"{self.n} plus {p} is {result}")
        return result

    def subtract(self):
        p = int(input("Enter a number to subtract: "))
        result = self.n - p
        print(f"{self.n} minus {p} is {result}")
        return result


Calculator.greet()
B = int(input("Enter a number: "))
A = Calculator(B)

print("\nSelect an operation:")
print("1. Square")
print("2. Multiply")
print("3. Divide")
print("4. Add")
print("5. Subtract")

choice = int(input("Enter your choice (1/2/3/4/5): "))
print("Working on it...")
time.sleep(0.5)

if choice == 1:
    A.square()
elif choice == 2:
    A.multiply()
elif choice == 3:
    A.divide()
elif choice == 4:
    A.add()
elif choice == 5:
    A.subtract()
else:
    print("Invalid choice. Please try again.")
