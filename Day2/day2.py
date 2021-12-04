from main import part1, part2

with open('day02.txt', 'r') as f:
	data = [x for x in f.read().split("\n")]

	print("Part 1: %d" % part1(data))
	print("Part 2: %d" % part2(data))
