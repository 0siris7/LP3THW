from sys import argv
from os.path import exists

sname, fname = argv
def fun(finame,l):
	print("Inside the function\nGonna use this function to write to file")
	f1 = open(finame,'w')
	f1.write(l)
	f1.close()
	print("Complete")
	print("Ya wanna see the content?",end="") #sticks next print statement with this statement
	f1 = open(finame)
	print("Content of file:\n",f1.read())

print(f"For {sname} we got {fname} ")
print(f"File exists: {exists(fname)}")
print("Enter to continue:")
input(">")
k = input("Enter some text:\n>")
print(f"{k} is about {len(k)} bytes")
fun(fname,k)
print("Thats all folks")
