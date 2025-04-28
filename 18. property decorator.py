class Company:
    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self, name):
        self.fname=name.split(" ")[0]
        self.lname=name.split(" ")[1]
    
    # @name.deleter
    # def name(self):
    #     del self.ename
    #     print("Deleted")

c=Company()
c.name="Atharva Shirke"
print(c.name)
