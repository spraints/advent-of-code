import fileinput, os

nexts = {}
def mem_blink(n):
    if n not in nexts:
        nexts[n] = blink(n)
    return nexts[n]

def blink(n):
    if type(n) is tuple:
        a, b = n
        return (mem_blink(a), mem_blink(b))
    if n == 0:
        return 1
    q, r = divmod(countdigits(n), 2)
    if r == 0:
        return divmod(n, 10**q)
    return n * 2024

def countdigits(n):
    digits = 0
    while n > 0:
        n //= 10
        digits += 1
    return digits

def count(x):
    if type(x) is list or type(x) is tuple:
        n = 0
        for a in x:
            n += count(a)
        return n
    else:
        return 1

numbers = [int(c) for c in fileinput.input().readline().split()]
for _ in range(25):
    for i in range(len(numbers)):
        numbers[i] = mem_blink(numbers[i])
print("Part 1: {}".format(count(numbers)))

for _ in range(50):
    for i in range(len(numbers)):
        numbers[i] = mem_blink(numbers[i])
print("Part 2: {}".format(count(numbers)))
