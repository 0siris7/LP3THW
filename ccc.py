class Sumtot(object):
    def __init__(self, x, y):
        x.self = x
        y.self = y
    def tot(self, ops):
        switcher = {'+' : x.self + y.self, '-' : x.self - y.self}
        print(switcher.get(ops))

x = int(input("enter number1: "))
y = int(input("enter number2: "))
#Sumtot(int(input("enter number1: ")), int(input("enter number two: "))).tot(input("Enter ops:"))
Sumtot(x, y).tot(input("Enter ops: "))
