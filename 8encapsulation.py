class Student:
    def __init__(self, name, year):
        self.name = name
        self.year = year
    
    def user(self):
        print("Hi", self.name, "is in his/her", s1.year, "year")

s1 = Student("Duaa", "4th")
s2 = Student("Fatima", "4th")

s1.user()
s2.user()