class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Duaa Sidd")
del s1
print(s1.name) #not found