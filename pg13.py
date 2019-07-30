from sys import argv #import argv

script, filename = argv #unpack

print(f"We're going to erase {filename}") #print statements
print("If you dont want that, hit CTRL-C(^C).")
print("If you do want that, hit RETURN.")

input("?") #no point in this

print("Opening the file...")
target = open(filename, 'w') #open file in write mode

print("Truncating the file. Goodbye!")
target.truncate() #truncate file but no point in it as opening in w mode truncates it

print("Now i'm going to ask you for three lines.")
#input
line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print("I'm going to write these to the file.")
#write to file
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close() #close