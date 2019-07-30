from sys import argv #import argv

scrpit, filename = argv #get scriptname and file name 

txt = open(filename) #open file and associate a variable with it (txt)

print(f"Here;s your file {filename}:")
print(txt.read()) #print what we get from file

txt.close()

#print("Type filename again: ")
#file_again = input("> ")

#txt_again = open(file_again) #associate a variable with file

#print(txt_again.read()) #print what is read