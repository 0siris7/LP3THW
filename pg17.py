from sys import argv #get argv

script, input_file = argv #unpack

def print_all(f): #func to print entire file
	print(f.read())

def rewind(f): #func to go back to start of file
	f.seek(0)

def print_a_line(line_count,f): #print a line at a time
	print(line_count,f.readline(),end="")

current_file = open(input_file) #open file

print("First let's print the whole file:\n ")

print_all(current_file) #call first func

print("Now let's rewind, kind of like a tape.")

rewind(current_file) #call second func to rewind

print("Let's print three lines:")
#call last func with line no and file object as arguments
current_line = 1 #c_line = 1
print_a_line(current_line,current_file)

current_line += 1 #c_line = 2
print_a_line(current_line,current_file)

current_line += 1 #c_line = 3
print_a_line(current_line,current_file) 
