a = {'a' : 1, 'b' : 2, 'c' : 3}
b = {1 : 'hello', 2 : 'There', 3 : 'General Kenobi'}

#print(list(a.items())) prints list with key n values
#print(a) prints dict

for i in a.items():
	print(i)

c = [[1,2,3], ('a', 'b')] #('a', 'b') is a tuple and values in a tuple can't be changed

for i,j in list(a.items()):
	print(f" {i} from a gives {b[j]} from b") 