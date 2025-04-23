class Employee:
    a=1
    def __init__(self):
        print("Employee constructor")

class Department(Employee): #Single classInheritance, 
    b=2
    def __init__(self):
        super().__init__()
        print("Department constructor") #Super constructor is called first

class Company(Department): #multiply level inheritance
    c=3
    def __init__(self):
        super().__init__()
        print("Company constructor")

#class Project(Company,Department): #Multiple class inheritance

d=Company()
print(d.a,d.b,d.c)