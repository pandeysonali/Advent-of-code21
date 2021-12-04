def part1(values: list) -> int:
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
	#Return product of hori and depth		
	return (hori * depth)	
