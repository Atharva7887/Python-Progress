#part 1
class employee: #Parent class
    
    name="Atharva Shirke"
    company="Wripo PVT"

    def show(self):
        self.name="Atharva"
        self.salary="Atharva"

        print(f"The name is {self.name} and salary is {self.salary}")


class programer(employee): #Inherits from employee, child class
    #name="Atharva Shirke"
    
    def showlang(self, language):
        print(f"The name is {self.name} and he is good with {language}") 

b=programer()
print(b.name)
b.show()
b.showlang("Python")

class company(programer): #Inherits from programer, multiply level inheritance
    name="Infosys"

    def department(self):
        print(f"The name is {self.name} and he is in the IT department")



#Part 2
class Employee:
    a=1
    def __init__(self):
        print("Employee constructor")

class Department(Employee): #Single classInheritance, 
    b=2
    def __init__(self):
        super().__init__()
        print("Department constructor") #Super constructor is called first

class Company(Department): #
    c=3
    def __init__(self):
        super().__init__()
        print("Company constructor")

#class Project(Company,Department): #Multiple class inheritance

d=Company()
print(d.a,d.b,d.c)