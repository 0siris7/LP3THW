from sys import argv
from os.path import exists
script , fname = argv	#import argv and exists and upack argv

def calc(x,op,y): #funct depicting simple calc
	if op == '+':
		return int(x) + int(y)

	elif op == '-':
		return int(x) - int(y)

	elif op == '*':
		return int(x) * int(y)

	elif op == '/':
		return int(x) // int(y)

	else:
		return int(x) % int(y)

f = open(fname,'w') #open file in write mode

a = input("Enter a number: ") #inputs
b = input("Enter another number: ")		
c = input("Enter operation: ")
z = str(calc(int(a)+13, c, int(b)+4)) #input must be converted to int as input is always string and strings are immutable
print("Result={}".format(z))
f.write(z)
f.close()
l = "waffle"
q = "Cheese"
y = l + q
print(y)