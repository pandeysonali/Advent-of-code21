from main import increases, window_increases

file = open('day01.txt', 'r')
data = []
for line in file:
    data.append(int(line))

print("Part 1: %d" % increases(data))
print("Part 2: %d" % window_increases(data))