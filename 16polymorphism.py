# For class int
print(1 + 2) #3

# For class str
print('a' + 'b') #ab

# For class list
print([1, 2], [3, 4]) #[1, 2, 3, 4]

# Our Own Class
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    
    def comp_num(self):
        print(self.real, 'i +', self.img, 'j')

    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)

    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)

num1 = Complex(1, 2)
num1.comp_num()

num2 = Complex(3, 5)
num2.comp_num()

num3 = num1 + num2
# num3 = num1.adding(num2)
num3.comp_num()

num4 = num1 - num2
num4.comp_num()
