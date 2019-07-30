from sys import argv

sp, fname = argv
#NOTE: YOU CANT READ FROM A FILE THAT IS OPEN IN ANOTHER MODE EVEN WITH + MODIFIER
print(f"We got file {fname}")
f1 = open(fname,'w+')
k = input("Enter some stuff\n>")
f1.write(k)
f1.close()
f2 = open(fname,'r+')
print(f"Content of file {fname}")
f2.seek(0)
print(f2.read())

f2.close()