class animals:
    def __init__(self):
        self.harbivors="harbivors"
        self.carnivores="carnivores"
        self.omnivores="omnivores"
        self.mammals="mammals"
        self.birds="birds"
        self.reptiles="reptiles"
        self.fish="fish"
        self.amphibians="amphibians"
        self.insects="insects"
        self.arthropods="arthropods"
        

class pets(animals):
    def __init__(self):
        super().__init__()
        self.dogs="dogs"
        self.cats="cats"
        self.fish="fish"
        self.birds="birds"
        self.reptiles="reptiles"
        self.rodents="rodents"

class dog(pets):
    def __init__(self):
        super().__init__()
        self.breed="Labrador"
        self.color="Black"
        self.age=5
        self.weight=30
        self.height=2
        self.size="Large"
    def bark(self):
        print("Woof Woof")
    

a=animals()
p=pets()
d=dog()
print(a.harbivors)
print(p.dogs)
print(d.breed)
print(d.color)
print(d.age)
d.bark()