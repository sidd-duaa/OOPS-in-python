class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass # using underscores made acc_pass private

    def get_pass(self):
        return self.__acc_pass

acc1 = Account("46464546", "hghhjnjn")
# print(acc1.acc_no, acc1.__acc_pass) => throws error
print(acc1.acc_no, acc1.get_pass()) #can be accessed using public method


class Person:
    __name = "anonymous"

    def __hello(self):
        return self.__name

    def get_name(self):
        return self.__name, self.__hello()
p1 = Person()
# print(p1.__name)
print(p1.get_name())
# print(p1.__hello())