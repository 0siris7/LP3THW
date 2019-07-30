a = ["98", "hours"]
b = ['0','1','2','3','4','5','6','7','8','9']
flag = 0

for i in b:
	#print("Outer for loop", i)
	for j in a:
		#print("Inner for loop", j)
		if i in j:
			if flag == 0:
				print("Found")
				print(j)
				flag = 1
				break

			else:
				break

	#break	