class Student:
    def hello(self):
        print("Hello")
    #regular method having no attribute still can't run without self

    @staticmethod
    def welcome():
        print("Welcome")

s1 = Student()
s1.hello()
s1.welcome()

