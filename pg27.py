i = 0
numbers = [] #empty list

while i < 6: #end condition is when i is less than 6 ie stops when i becomes 6
	print(f"At the top i is {i}") #before incrememnt
	numbers.append(i) #add to list

	i = i + 1 #incrememnt
	print("Numbers now: ", numbers) #printing current list

	print(f"At the bottom i is {i}") #after increment

print("The numbers: ")

for num in numbers: #listing list
	print(num)

print(numbers)