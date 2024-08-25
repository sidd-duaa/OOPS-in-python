class Student():
    name = "Duaa"
    def __init__(self):
        print(self)
        print(self.name)
        print("Constructor Executed asa object created")
  
s1 = Student()

class Car():
    # Default constructor
    def __init__(self):
        print("Default Constructor")

    # Parametrized constructor
    def __init__(self, color):
        self.color = color
        print("Adding new car")

c1 = Car("Blue")
print(c1.color)
