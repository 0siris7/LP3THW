from sys import argv #import

snam, fname1 = argv #unpack

f1 = open(fname1) #open file

print(f"from {fname1} we get: ") #print
print(f1.read()) #print content

fname2 = input("Enter another file name:\n>") #get second file

f2=open(fname2) #open
k = f2.read() #store content to a variable
print(f"from {fname2} we get \n{k}") #print file content
f2.close()
f1.close()
#print(k)