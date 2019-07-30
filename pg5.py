formatter = "{} {} {} {}" #string with {}
print(formatter.format(1,2,3,4)) #prints numberes
print(formatter.format("one","two","three","four")) #prints str5ngs
print(formatter.format(True,False,False,True)) #prints bool val
print(formatter.format(formatter, formatter, formatter, formatter)) #prints {} 16 times
print(formatter.format( #prints text in single line
		"Try your",
		"Own text here",
		"Maybe a poem",
		"Or a song about fear"



	))