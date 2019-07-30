peeps = 10
x = f"there are {peeps} types of people" #formatted

binary="binary"
do_not="don't"
y=f"Those who know {binary} and those who {do_not}" #string in string

print(x)
print(y)

print(f"I said: {x}") #string in string
print(f"I also said: '{y}'") #string in string

hilarious = False
joke_evaluation="Isn't that joke so funny?! {} and {}" #string in string and empty {}
print(joke_evaluation.format(hilarious,hilarious)) #format function used to fill empty {}

w = "This is the left side of..."
e = "a String with a right side"

print(w + e) # + is concatenation
