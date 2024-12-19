import fileinput, heapq
grid = [[c for c in line.strip()] for line in fileinput.input()]
s = None
e = None
for r, row in enumerate(grid):
    for c, cell in enumerate(row):
        if cell == 'S':
            s = (r, c)
        if cell == 'E':
            e = (r, c)
print(s)
print(e)
