from sys import argv

def listn(f):
	k = f.read()
	return k.split(' ')

script , fname = argv

print("Got {} and {} from cmd".format(*argv))

f = open(fname, 'w')

print("Enter stuff:")
f.write(input("> "))
print("Writing to a file")
f.close()

f = open(fname)

print("Got this from file:\n", f.read())
f.seek(0)
print("Turning it into a list")

a = listn(f)
f.close()
print("The list:\n> ",a)

ans = ['Y', 'y']

print("Want to enter some more? [Y/N]")

if input("> ") in ans:
	while True:
		l = input("Enter a word:\n> ")
		a.append(l)
		print("Want to continue?[Y/N]\n>",end = '')
		if input() in ans:
			continue
		else:
			break

print("The list as a list: {}".format(a))
print("The list as a statement: ", ' '.join(a))

print("Printing them individually")

i = 0

while i < len(a):
	print(f"index[{i}] : {a[i]}")
	i += 1

f = open(fname, 'a')
f.write("\n" + ' '.join(a))
f.close()

