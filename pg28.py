from sys import exit #exit used to exit the program

def gold_room(): #a function
	print("This room is full of gold. how much do you take? ")

	choice = input("> ") #python takes strings as i/p , nothing else
	if "0" in choice or "1" in choice: #checks if there is 0 or 1 in i/p
		how_much = int(choice) #input converted

	else:	
		dead("Man, learn to type a number.")

	if how_much < 50: #second if-else pair checks how_much
		print("Nice, you're not greedy, you win!")
		exit(0)
	else:
		dead("You greedy bastard!") #function call to dead() game over


def bear_room():
	print("There is a bear here.")	
	print("The bear has a bunch of honey")
	print("The fat bear is in front of another door.")
	print("How are you going to move the bear?")
	bear_moved = False #initial value

	while True: #infinite look until called to dead()
		choice = input("> ")

		if choice == "Take honey":
			dead("The bear looks at you then slaps your face off.") #loop ends when dead called
		elif choice == "taunt bear" and not bear_moved: # (#1) works only once if choice is taunt bear and then bear_moved becomes true so if encounterd again ,condition wont be true 
			print("THe bear has moved from the door")
			print("You can go through it now")
			bear_moved = True
		elif choice == "taunt bear" and bear_moved: #happens when taunt bear is selected twice 
			dead("The bear gets pissed off and chew you leg off") #loops ends here
		elif choice == "open door" and bear_moved: #checks if bear_moved became true after #1
			gold_room() #loop ends here and control passed to gold_room()
		else:
			print("I got no idea what that means") 

def cthulhu_room(): #if right room selected
	print("Here you see the great evil Cthulhu")	
	print("He, it, whatever stares at you and you go insane.")
	print("Do you flee for your life or eat your head?")

	choice = input("> ")

	if "flee" in choice: #checks if substring flee is in string
		start() #game started again
	elif "head" in choice: 
		dead("well that was tasty!")
	else: #another way to loop
		cthulhu_room()

def dead(why): #ending
	print(why, "Good job!")
	exit(0)

def start(): #to start the game
	print("You are in a dark room.")		
	print("There is a door to your right and left")
	print("Which one do you take?")

	choice = input("> ") #based on choice
	if choice == "left":
		bear_room()
	elif choice == "right":
		cthulhu_room()
	else:
		dead("You stumble around the room until you starve")

start() #function call

