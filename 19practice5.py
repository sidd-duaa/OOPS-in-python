# Create a class called Order which stores item and its price.
# Use Dunder function __gt__() to convey that:
# Order1 > Order2 if price of order1 > price of order2

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price
    
    def __gt__(self, order2):
        return self.price > order2.price
            
o1 = Order("Jacket", 5000)
o2 = Order("Bag", 3000)
# o1.gt(o2)
print(o1 > o2) #True