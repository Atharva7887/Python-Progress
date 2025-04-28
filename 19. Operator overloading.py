class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overloading the + operator
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    # Overloading the * operator (scalar multiplication)
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    # String representation for easy printing
    def __str__(self):
        return f"Vector({self.x}, {self.y})"


# Example usage
v1 = Vector(2, 3)
v2 = Vector(4, 5)

v3 = v1 + v2        # Calls __add__
v4 = v1 * 3         # Calls __mul__

print("v1 + v2 =", v3)
print("v1 * 3  =", v4)
