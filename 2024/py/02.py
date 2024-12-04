import fileinput, itertools

# each row is a report, each number is a level.
input = [[int(x) for x in line.strip().split()] for line in fileinput.input()]

def is_safe(report, skip = -1):
    i = 0
    if skip == 0:
        i = 1
    dir = 0
    prev = report[i]
    for i in range(i+1, len(report)):
        if i != skip:
            cur = report[i]
            diff = cur - prev
            prev = cur
            if diff >= 1 and diff <= 3 and (dir == 0 or dir == 1):
                dir = 1
            elif diff <= -1 and diff >= -3 and (dir == 0 or dir == -1):
                dir = -1
            else:
                return False
    return True

def is_safe2(report):
    if is_safe(report):
        return True
    for i in range(len(report)):
        if is_safe(report, skip = i):
            return True
    return False

safe = filter(is_safe, input)
part1 = sum(1 for _ in safe)
print("Part 1: {}".format(part1))

safe = filter(is_safe2, input)
part2 = sum(1 for _ in safe)
print("Part 2: {}".format(part2))
