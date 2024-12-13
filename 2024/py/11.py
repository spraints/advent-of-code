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

numbers = [int(c) for c in fileinput.input().readline().split()]
for _ in range(25):
    numbers = [b for n in numbers for b in mem_blink(n)]
print("Part 1: {}".format(len(numbers)))
for _ in range(50):
    numbers = [b for n in numbers for b in mem_blink(n)]
print("Part 2: {}".format(len(numbers)))
