class employee:
    name="Atharva Shirke"
    company="Wripo PVT"

    def show(self):
        self.name="Atharva"
        self.salary="Atharva"

        print(f"The name is {self.name} and salary is {self.salary}")


class programer:
    company="ITC Info"
    def show(self):
        print(f"The name is {self.name} and salary is {self.salary}")

    def showlang(self):
        print(f"The name is {self.name} and he is good with {self.language}") 

a=employee()
b=programer()

print(f"{a.name}\n{b.company}")
a.show()