import fileinput

nexts = {}
def mem_blink(n):
    if n not in nexts:
        nexts[n] = blink(n)
    return nexts[n]

def blink(n):
    if n == 0:
        return [1]
    q, r = divmod(countdigits(n), 2)
    if r == 0:
        return divmod(n, 10**q)
    return [n * 2024]

def countdigits(n):
    digits = 0
    while n > 0:
        n //= 10
        digits += 1
    return digits

expanded = {}
def expand(n, blinks):
    if blinks == 0:
        return 1
    if (n, blinks) not in expanded:
        total = 0
        for b in mem_blink(n):
            total += expand(b, blinks - 1)
        expanded[(n, blinks)] = total
    return expanded[(n, blinks)]

numbers = [int(c) for c in fileinput.input().readline().split()]
total = 0
for n in numbers:
    total += expand(n, 25)
print("Part 1: {}".format(total))
total = 0
for n in numbers:
    total += expand(n, 75)
print("Part 2: {}".format(total))
