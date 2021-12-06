data = open("day06.txt", "r")
myList = [int(x) for x in data.read().split(",")]
newList = []
numDays = 256
count = len(myList)

#Part 1
# outer loop for number of days
for i in range(numDays):
	newList = []
	for num in myList:
		if num > 0 and num <= 8:
			num -= 1
			newList.append(num)
		elif num == 0:
			newList.append(6)
			newList.append(8)
			count += 1
		else:
			print("invalid entry")
	myList = newList			
print(count)


#Part 2
#Can't go over ~trillion nums so let's keep track of fish 

	 