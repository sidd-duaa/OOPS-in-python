class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        # self.percentage = str((self.phy + self.chem + self.math) / 3) + '%'
        # percentage is fixed and doesn't change with phy, chem or math attribute

    # also correct but property is better
    # def calcPercentage(self):
    #     return str((self.phy + self.chem + self.math) / 3) + '%'

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + '%'
    
s1 = Student(98, 97, 99)
print(s1.percentage)

s1.phy = 86
print(s1.phy)
print(s1.percentage)
