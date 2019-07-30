class Sumtot(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def tot(self, ops):
        switcher = {'+' : self.x + self.y , '-' : self.x - self.y}
        print(switcher.get(ops))

x = int(input("enter number1: "))
y = int(input("enter number2: "))
#Sumtot(int(input("enter number1: ")), int(input("enter number two: "))).tot(input("Enter ops:"))
Sumtot(x, y).tot(input("Enter ops: "))
