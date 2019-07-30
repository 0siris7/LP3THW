people = 20
cats = 30
dogs = 15

if people < cats:
	print("Too many cats! The world is doomed!")

if people > cats:
	print("Not many cats! the world is saved!")

if people < dogs:
	print("The world is drooled on!")

if people > dogs:
	print("the world is dry!")

dogs += 5

if people >= dogs:
	print("People are greater than or equal to dogs")

if people <= dogs:
	print("People are less than or eqaual to dogs.")

if people == dogs:
	print("People are dogs.")

print("Nasty stuff:")
#if print (people == dogs): doesnt work only prints result of people == dogs
#	print("It works")