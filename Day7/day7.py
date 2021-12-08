my_file = open("day07.txt", "r")
my_list = [int(x) for x in my_file.readline().split(",")]
my_list.sort()

med = my_list[len(my_list)//2]

#Part1 - Calculate the median
best_path_total = 0
for item in my_list:
	best_path_total += abs(item-med)

print(best_path_total)	


#Part2
#Sum of n numbers
def total_sum(num):
	return num*(num+1)/2

best_path = 1e9
for x in range(2000):
	score = 0
	for y in my_list:
		d = abs(y-x)
		score += total_sum(d)
	if score < best_path:
		best_path = score

print(best_path)			

