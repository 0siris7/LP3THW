from sys import argv

a,b = argv

print(f"we got {a} and {b}")

x = int(input("enter a number:"))
y = float(input("enter a float number:"))
z= x+y
print("the result of {} and {} is {}  ".format(x,y,z))