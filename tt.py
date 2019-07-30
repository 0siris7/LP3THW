def six(numb, x, lis):
	i = 0
	while i < numb: #end condition is when i is less than 6 ie stops when i becomes 6
		print(f"At the top i is {i}") #before incrememnt
		lis.append(i) #add to list

		i = i + x #incrememnt
		print("Numbers now: ", lis) #printing current list

		print(f"At the bottom i is {i}") #after increment
	return lis


n = int(input("Enter a limit: "))
x = int(input("Enter an increment"))
numbers = []

numbers = six(n, x, numbers)

print("The numbers: ")

for num in numbers: #listing list
	print(num)

print(numbers)