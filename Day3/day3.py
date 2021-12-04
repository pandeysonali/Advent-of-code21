from main import part1

file = open('day03.txt', 'r')
data = []
for line in file:
    data.append(line.strip('\n'))
   
print("Part 1: %d" % part1(data))