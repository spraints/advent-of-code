import fileinput
def p(c):
    if c == ".":
        return -2
    return int(c)
grid = [[p(c) for c in line.strip()] for line in fileinput.input()]
rows = len(grid)
cols = len(grid[0])

scores = [[0 for x in row] for row in grid]
reachable = [[set() for x in row] for row in grid]
pozs = []
zeroes = []
for r, row in enumerate(grid):
    for c, x in enumerate(row):
        match x:
            case 0:
                zeroes.append((r,c))
            case 9:
                pozs.append((r,c))
                scores[r][c] = 1
                reachable[r][c] = {(r,c)}
#print(zeroes)
#print(pozs)
#print(scores)

for height in reversed(range(9)):
    #for r, c in sorted(pozs):
    #    print(" -", (r,c), len(reachable[r][c]), reachable[r][c])
    #print("look for neighbors of height {}".format(height))
    new_pozs = set()
    for r, c in pozs:
        for nr, nc in [
                (r + 1, c),
                (r - 1, c),
                (r, c + 1),
                (r, c - 1),
                ]:
            if nr >= 0 and nc >= 0 and nr < rows and nc < cols:
                #print("{},{} -> {},{}: {}".format(r, c, nr, nc, grid[nr][nc]))
                if grid[nr][nc] == height:
                    scores[nr][nc] += scores[r][c]
                    reachable[nr][nc] |= reachable[r][c]
                    new_pozs.add((nr,nc))
    pozs = new_pozs

#for r, c in zeroes:
#    print(" -", (r,c), len(reachable[r][c]), reachable[r][c])
part1 = sum([len(reachable[r][c]) for r, c in zeroes])
print("Part 1: ", part1)
