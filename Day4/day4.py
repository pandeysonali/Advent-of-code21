from main import isWinner
file = open("day04.txt", "r")
numbers = [int(x) for x in file.readline().strip().split(",")]

allBoards = []

while file.readline():
	board = []
	for i in range(5):
		board.extend([int(x) for x in file.readline().strip().split() if x != ''])
	allBoards.append(board)	


#Part1

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

#Part2
found = False
while(found == False and len(numbers) > 0):
	number = numbers[0]
	numbers = numbers[1:]
	for index in range(len(allBoards)):
		for i in range(len(allBoards[index])):
			if allBoards[index][i] == number:
				allBoards[index][i] = 100

	index = 0
	while index < len(allBoards):
		if isWinner(allBoards[index]):
			if(len(allBoards) > 1):
				allBoards.pop(index)
			else:
				found = True
				break
		else:
			index += 1	

total = sum([x for x in allBoards[index] if x!= 100])
print("Part2: %d" % (total*number))

