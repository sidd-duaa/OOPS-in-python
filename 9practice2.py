# Create Account class with 2 attributes - balance and account no. Create methods for debit, credit and printing the balance.

class Account:
    def __init__(self, bal, acc_no):
        self.balance = bal
        self.account_no = acc_no

    def acc_balance(self):
        return self.balance
    
    def debit(self, amount):
        self.balance -= amount
        print("Your account has been debited with", amount, "leaving your current balance", self.acc_balance())

    def credit(self, amount):
        self.balance += amount
        print("Your account has been credited with", amount, "making your current balance", self.acc_balance())

a1 = Account(40000, 5356465)
print(a1.balance, a1.account_no)
print("Your account number is", a1.account_no)
a1.acc_balance()
a1.debit(5000)
a1.credit(2000)
a1.credit(4000)
a1.debit(10000)