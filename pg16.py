def cheese_and_crackers(cheese_count, boxes_of_crackers): #function definition
	print(f"You have {cheese_count} cheeses!")
	print(f"You have {boxes_of_crackers} boxes of crackers!")
	print("Man thats enough for a party!")
	print("Get a blanket.\n")

def cnc(a,b):
	c = a+b
	print("Sum :",c)

print("We can just give the function numbers directly:") #print
cheese_and_crackers(20,20)  #func call

print("OR, we can use variables for our script:") 
amount_of_cheese = 10 #varialbes
amount_of_crackers = 50
#func call with variables
cheese_and_crackers(amount_of_cheese,amount_of_crackers)
#function call with math
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)
#func call with var and nos
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese+100,amount_of_crackers+1000)
#my func calls
cnc(2,3)
cnc(amount_of_crackers,amount_of_cheese)
cnc(2+amount_of_cheese,3+amount_of_crackers)
