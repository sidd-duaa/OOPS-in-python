class Student:
    def __init__(self, fullname, marks):
        self.name = fullname
        self.marks = marks

    def hello(self):
        print("Hello", self.name)

    def get_marks(self):
        print(self.marks)

s1 = Student("Duaa", 87)
s1.hello()