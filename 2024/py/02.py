import fileinput

# each row is a report, each number is a level.
input = [[int(x) for x in line.strip().split()] for line in fileinput.input()]

# ex 1: 1
# ex 2: 4
# real 1: 624

def is_safe(report):
    #print(report)
    if report[0] < report[1]:
        #print("ASC")
        for a, b in zip(report, report[1:]):
            d = b - a
            if d < 1 or d > 3:
                return False
        #print("SAFE")
        return True
    elif report[0] > report[1]:
        #print("DESC")
        for a, b in zip(report, report[1:]):
            d = a - b
            if d < 1 or d > 3:
                return False
        #print("SAFE")
        return True
    else:
        return False

safe = filter(is_safe, input)
part1 = sum(1 for _ in safe)
print("Part 1: {}".format(part1))

#safe = 0
#for report in input:
#    if all_increasing(report, tolerance = 1) or all_decreasing(report, tolerance = 1):
#        safe += 1
#print("Part 2: {}".format(safe))
