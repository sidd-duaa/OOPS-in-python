class Student:
    department = "UBIT" #class attribute
    year = "3rd"
    def __init__(self, name, year):
        self.name = name
        self.year = year

s1 = Student("Duaa", "4th")
s2 = Student("Fatima", "4th")

print(s1.name, s1.department, s1.year)
print(s2.name, s2.department, s2.year)
