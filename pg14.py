from sys import argv
from os.path import exists
#import exist
script, from_file, to_file = argv #two files

print(f"Copying from {from_file} to {to_file}")

#in_file = open(from_file)
indata = open(from_file).read() #read from file

print(f"THe input file is {len(indata)} bytes long") #length of file

print(f"Does the output fille exist? {exists(to_file)}") #check if file exist
print("ready, hit RETURN to continue, CTRL-C to abort.")
input(">")

out_file = open(to_file,'w')
out_file.write(indata)

print("Alright, all done. ")

out_file.close()
#from_file.close()