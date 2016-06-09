with open("nos8_second.txt",'r') as v:
	content=v.read
	lines=content.split('\n')
	print (lines[0])

	print (type(lines[0]))	
