import fileinput

# each row is a report, each number is a level.
input = [[int(x) for x in line.strip().split()] for line in fileinput.input()]

def all_increasing(report):
    for a, b in zip(report, report[1:]):
        d = b - a
        if d > 3 or d < 1:
            return False
    return True

def all_decreasing(report):
    for a, b in zip(report, report[1:]):
        d = a - b
        if d > 3 or d < 1:
            return False
    return True

safe = 0
for report in input:
    if all_increasing(report) or all_decreasing(report):
        safe += 1
print("Part 1: {}".format(safe))
