#printing
print("Lets practice everything.")
print('You\'d need to know \'bout escapes with \\ that do:')
poem = """
\tThe lovely world
	with logic so firnly planted
	cannot discern \nthe needs of love
	nor comprehend passion from intuition
	and requires an explanation
	\n\t\twhere there is none
"""


print("--------------")
print(poem) #print poem
print("--------------")

five = 10 - 2 + 3 - 6
print(f"This shoulf be five: {five}") #print formatted string
#func definition
def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000 #tend to be float vals
	crates = jars / 100
	return jelly_beans, jars, crates
#func call
start_point = 10000
beans, jars, crates = secret_formula(start_point)
#.format function
print("With a starting point of : {}".format(start_point))
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("we can also do that this way:")
formula = secret_formula(start_point) #return to a single var rather than 3
print("We'd have {} beans, {} jars, and {} crates.".format(*formula)) #use * to get stuff from single var		