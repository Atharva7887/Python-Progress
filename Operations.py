a=int(input("Enter number 1: "))
b=int(input("Enter number 2: "))

# Arithmetic operations
print("Addition:", a+b)
print("Subtraction:", a-b)
print("Multiplication:", a*b)
print("Division:", a/b)
print("Floor Division:", a//b)
print("Modulus:", a%b)
print("Exponentiation:", a**b)

# Comparison operations
print("Greater than:", a>b)
print("Less than:", a<b)
print("Equal to:", a==b)
print("Not equal to:", a!=b)
print("Greater than or equal to:", a>=b)
print("Less than or equal to:", a<=b)

# Assignment operations
a+=b
print("After addition assignment, a:", a)
a-=b
print("After subtraction assignment, a:", a)
a*=b
print("After multiplication assignment, a:", a)
a/=b
print("After division assignment, a:", a)
a//=b
print("After floor division assignment, a:", a)
a%=b
print("After modulus assignment, a:", a)
a**=b
print("After exponentiation assignment, a:", a)

# Logical operations
print("Logical AND:", a and b)
print("Logical OR:", a or b)
print("Logical NOT:", not a)

# Identity operations
print("Identity is:", a is b)
print("Identity is not:", a is not b)

# Membership operations
list1 = [1, 2, 3, 4, 5]
print("Membership in list:", a in list1)
print("Membership not in list:", a not in list1)

# Bitwise operations
print("Bitwise AND:", a & b)
print("Bitwise OR:", a | b)
print("Bitwise XOR:", a ^ b)
print("Bitwise NOT:", ~a)
print("Left Shift:", a << 1)
print("Right Shift:", a >> 1)

# Ternary operator
result = a if a > b else b
print("Ternary operator result:", result)

# All operations
all_true = all([True, True, True])
print("All function (all true):", all_true)
any_true = any([False, True, False])
print("Any function (any true):", any_true)

