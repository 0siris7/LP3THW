from sys import exit

def begin():
	items = ["flare gun","bottle"]
	print("You wake up from a bad dream and you notice that you're somewhere in the ocean.")
	print("You find {} and a {}".format(*items))
	print("What do you do?")
	act = input("> ")
	if "flare gun" in act:
		flare_gun_arc()

	elif "bottle" in act:
		bottle_arc()

	else:
		print("You were hallucinating and wake up at home")



def flare_gun_arc():
	print("You take the flare gun but there's no ammo in it.")
	print("What now?")
	ans = input("> ")
	while True:
		if "search" in ans:
			rescue()

		elif "scream" in ans:
			print("You do so but there's no help to be found.")
			print("You looked everywhere and find flare gun ammo among the debris.")
			print("What do you do?")
			hope = input("> ")
			if "take" in hope:
				rescue()
			else:
				print("You {} but help doesn't arrive and you wither away")
				exit(0)


def rescue():
	print("You shoot the flare gun and decide to wait.")
	print("How long do you plan on waiting?")
	a = ['0', '1' ,'2' ,'3' ,'4' ,'5' ,'6' ,'7' ,'8' ,'9']
	r_ans = input("> ")
	b = r_ans.split(" ")
	c = ''
	flag = 0
	#num = str([int(s) for s in r_ans.split() if s.isdigit()]) #Find out more about this
	for i in a:
		for j in b:
			if i in j:
				if flag == 0:
					print("You wait for {} hours".format(j))
					flag = -1
					c = j
					break


	if int(c) > 50:
		print("Help Arrives")
		exit(0)
	else:
		print("You die of dehydration")
		begin()


def bottle_arc():
	print("You take the bottle and then what do you do?")
	b_ans = input("> ")
	if "read" in b_ans:
		print("You wake up from your dream.")

	else:
		print("You literally threw away your hope of waking up from this nightmare.")






begin()
