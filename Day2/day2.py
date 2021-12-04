with open('day02.txt', 'r') as f:
	values = [x for x in f.read().split("\n")]
	print (values)

	hori = 0
	depth = 0
	for val in values:
		line = val.split()
		if line[0] == "forward":
			hori += int(line[1])
		elif line[0] == "down":
			depth += int(line[1])
		elif line[0] == "up":
			depth -= int(line[1])
		else:
			print("Invalid input")
	print (hori)
	print (depth)
	print (hori * depth)						