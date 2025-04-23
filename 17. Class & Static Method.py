class Employee:
    a=1
    @classmethod # Class method
    def show(cls):
        print(f"Class attribute: {cls.a}")

    @staticmethod #Static method
    def show_static():
        print("Static method called")

b=Employee()
b.a=2
b.show()