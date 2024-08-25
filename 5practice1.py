# Create student class that takes name and marks of 3 subjects as arguments in constructor. Then create a method to print the average.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_average(self):
        sum = 0
        for mark in self.marks:
            sum += mark
        return (sum/3)

s1 = Student("Duaa", [71, 72, 71])
print("Hi", s1.name, "your average marks are", s1.get_average())