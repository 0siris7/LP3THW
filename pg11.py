from sys import argv	#import argv

script, user_name = argv #unpacking
prompt= ">"

print(f"Hi {user_name}, I'm the {script} script")
print("I'd ike to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

#print(f"Where do you live {user_name}?")
lives = input(f"Where do you live {user_name}?\n{prompt}")

print("What kind of computer do you have?")
computer = input(prompt)

print(f""" 
			Alright, so you said {likes} about me.
			You kuve in {lives}. Not sure where that is.
			And you have a {computer} computer. Nice.

	""")