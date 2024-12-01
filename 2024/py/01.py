import fileinput

input = [[int(x) for x in line.strip().split()] for line in fileinput.input()]
#print(input)

list_a = sorted([x[0] for x in input])
list_b = sorted([x[1] for x in input])
part1 = sum(abs(a-b) for a, b in zip(list_a, list_b))
print("Part 1:", part1)
