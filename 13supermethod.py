class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("Car started.. ")

    @staticmethod
    def stop():
        print("Car stopped.. ")

class ToyotaCar(Car):
    def __init__(self, brand, type):
        self.brand = brand
        super().__init__(type) #to access the type of parent class
        super().start()

c1 = ToyotaCar('Maruti', 'electric')
print(c1.brand)
print(c1.type)