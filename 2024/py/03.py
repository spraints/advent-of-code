import fileinput, re
input = "\n".join(fileinput.input())
part1 = sum([int(a) * int(b) for a, b in re.findall(r'mul\((\d+),(\d+)\)', input)])
print("Part 1: {}".format(part1))
