# Define an Employee class with attributes role, department and salary. This class also has a showDetails() method.
# Create an Engineer class that inherits properties from Employee and has additional attributes: name and age

class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def showDetails(self):
        print('Role: ', self.role)
        print('Department: ', self.department)
        print('Salary: ', self.salary)

e1 = Employee("Manager", "IT", "2M")
e1.showDetails()

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Intern", "IT", "50K")
    
    def details(self):
        print("Name:", self.name)
        print("Age", self.age)

eng1 = Engineer("Duaa", "22")
eng1.details()
eng1.showDetails()