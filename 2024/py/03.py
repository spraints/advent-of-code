import fileinput, re
input = "\n".join(fileinput.input())

part1 = sum([int(a) * int(b) for a, b in re.findall(r'mul\((\d+),(\d+)\)', input)])
print("Part 1: {}".format(part1))

enabled = True
part2 = 0
for a, b, yes, no in re.findall(r"mul\((\d+),(\d+)\)|(do)\(\)|(don't)\(\)", input):
    if yes != "":
        enabled = True
    elif no != "":
        enabled = False
    elif enabled:
        part2 += int(a) * int(b)
print("Part 2: {}".format(part2))
