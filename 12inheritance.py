# SINGLE INHERITANCE

class Parent:
    @staticmethod
    def start():
        print("car started.. ")
    
    @staticmethod
    def stop():
        print("car stopped.. ")

class Child(Parent):
    def __init__(self, name):
        self.name = name

c1 = Child("Fortuner")
print(c1.name)
# inherited start and stop methods from parent class Car
c1.start()
c1.stop()


# MULTI-LEVEL INHERITANCE

class Car:
    @staticmethod
    def start():
        print("car started.. ")
    
    @staticmethod
    def stop():
        print("car stopped.. ")

class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand

class Fortuner(ToyotaCar):
    def __init__(self, color):
        self.color = color

car1 = Fortuner("black")
print(car1.color)
# print(car1.brand)
car1.start()
car1.stop()


# MULTIPLE INHERITANCE

class A:
    varA = "Welcome to class A"

class B:
    varB = "Welcome to class B"

class C(A, B):
    varC = "Welcome to class C"

class1 = C()
print(class1.varA, class1.varB, class1.varC)