print("""You enter a dark room with two doors.
	Do you go through door #1 or door #2?""")
door = input("> ")

if door == "1":
	print("There's a giant bear here eating a cheese cake. ")
	print("What do you do?")
	print("1. Take the cake.")
	print("2. Scream at the bear.")
	bear = input("> ")

	if bear == "1":
		print("The bear eats your face off. Good job!")
		print("The bear is about to eat your face\nWhat do you do?\n1. punch\n2. kick")
		attac = input("Enter the action:\n> ")
		if attac == "punch":
			print(f"You {attac} and the bear faints.")
		elif attac == "kick":
			print(f"You {attac} and the bear gets annoyed and rips your face.\nGG")
		else:
			print(f"You started {attac} and the bear lost interest and left")
	elif bear == "2":
		print("The bear eats your legs off. Good job!")

	else:
		print(f"Well, doing {bear} is probably better.")
		print("Bear runs away.")

elif door == "2":
	print("You stare into the endless abyss at Cthulhu's retina.")
	print("1. Blueberries.")
	print("2. Yellow jacket clothespins.")
	print("3. Understandin revolvers yelling melodies.")

	insanity = input("> ")

	if insanity == "1" or insanity == "2":
		print("Your body survies powered by a mind of jello.")
		print("Good job!")
		print("Cthulhu wants to commune with you.\nDo you...\n1. Commune\n2. Ignore")
		ans = input("> ")
		if ans == "1":
			print("The elder god wishes to take over the world.\nWhat say you?\n1. Help\n2. Fight the god")
			god = input("> ")
			if god == "1":
				print("The elder god is grateful and you guys take over the world.")
			else:
				print("The elder god vanquishes you.")

		if ans == "2":
			print("You ignore the god and now he'sad \n :C")
	else:
		print("The insanity rots your eyes into a pool of muck.")
		print("Good job!")

else:
	print("You stumbled arounf and fall on a knife and fie. Good job!")
