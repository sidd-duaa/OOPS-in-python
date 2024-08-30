class Person:
    name = "anonymous"

    '''
    def changeName(self, name):
        self.name = name #creates a new attribute
        Person.name = name #can change using Class name
        self.__class__.name = name #class method
    '''

    @classmethod #to change class attribute directly
    def changeName(cls, name): #cls is just a word used 
        cls.name = name

p1 = Person()
print(p1.name) #anonymous
p1.changeName("Duaa")
print(p1.name) #Duaa
print(Person.name)