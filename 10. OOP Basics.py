# OOP Basics

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I'm {self.age} years old.")

# Object creation
person1 = Person("Atharva", 22)
person1.introduce()
