def part1(data: list) -> int:
	build_gamma = ""
	build_epsilon = ""
	idx = 0
	while (idx < (len(data[0]))):
		zero = 0
		one = 0
		for val in data:
			if val[idx] == '0':
				zero += 1
			elif val[idx] == '1':
				one += 1	
			else:
				print("invalid")
	
		if zero > one:
			build_gamma += '0'
			build_epsilon += '1'
		else:
			build_gamma += '1'
			build_epsilon += '0'
		idx += 1			
		
	print(build_gamma)
	print(build_epsilon)
	return int(build_gamma, 2) * int(build_epsilon, 2)


