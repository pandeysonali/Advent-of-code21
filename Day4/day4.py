from main import isWinner
file = open("day04.txt", "r")
numbers = [int(x) for x in file.readline().strip().split(",")]
print(numbers)

allBoards = []

while file.readline():
	board = []
	for i in range(5):
		board.extend([int(x) for x in file.readline().strip().split() if x != ''])
	allBoards.append(board)	


print(allBoards)

found = False
while (found == False) and (len(numbers) > 0):
	number = numbers[0]
	numbers = numbers[1:]
	for item in allBoards:
		for i in range(len(item)):
			if item[i] == number:
				item[i] = 100
	for item in allBoards:
		if isWinner(item):
			total = sum([x for x in item if x!= 100])
			print("Part1: %d" % (total*number))
			found = True			