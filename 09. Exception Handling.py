# Exception Handling

try:
    num = int(input("Enter a number: "))
    print("100 divided by your number:", 100 / num)
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Please enter a valid number.")
finally:
    print("Execution completed.")
