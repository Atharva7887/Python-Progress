class employee:
    name="Atharva Shirke"
    company="Wripo PVT"

    def show(self):
        self.name="Atharva"
        self.salary="Atharva"

        print(f"The name is {self.name} and salary is {self.salary}")


class programer(employee): #Inherits from employee
    

    def showlang(self, language):
        print(f"The name is {self.name} and he is good with {language}") 

b=programer()
print(b.name)
b.show()
b.showlang("Python")