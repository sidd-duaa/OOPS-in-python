class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
    
    def start(self):
        self.acc = True
        self.clutch = True
        print("car started...")
        # things written in function are hidden for users
c1 = Car()
c1.start()