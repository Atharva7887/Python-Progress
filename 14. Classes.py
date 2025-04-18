import time
class Employee:
    Salary = 30000
    Language = "Python"

    def getinfo(self):
        self.Name = input("Enter a name: ")
        if self.Name =="":
            print("**Enter your name MF!!** (Master Fighter)")
            return
        time.sleep(1)
        self.Gender = input("Enter Male or Female: ")
        time.sleep(0.5)
        print("Collecting information...")
        time.sleep(1.5)
        print("Fetching details...")
        time.sleep(1.5)
        print("Details fetched successfully!")
        time.sleep(1.5)
        n=len(f"{self.Name} has a salary of ₹{self.Salary} per month and {'she' if self.Gender.lower() == 'female' else 'he'} codes in {self.Language}")
        print(f"\n{"*"*n}\n{self.Name} has a salary of ₹{self.Salary} per month and {'she' if self.Gender.lower() == 'female' else 'he'} codes in {self.Language}.\n{"*"*n}\n")

    @staticmethod # Static method,it doesn't require self
    def greet():
        print( "Hello, welcome to the company!")

    def __init__(self): # Constructor
        print("Employee class initializing...")
        time.sleep(1.5)
        

atharva=Employee()

atharva.greet()
atharva.getinfo()
