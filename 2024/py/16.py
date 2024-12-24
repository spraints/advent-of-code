import fileinput, heapq

VIZ = True

grid = [[c for c in line.strip()] for line in fileinput.input()]

s = None
e = None
for r, row in enumerate(grid):
    for c, cell in enumerate(row):
        if cell == 'S':
            s = (r, c)
        if cell == 'E':
            e = (r, c)

#      (-1,0)
# (0,-1)  @  (0,1)
#       (1,0)
d = (0,1)

options = [ (s,d,0,frozenset([s])) ]

def trydir(p, nd, ns, v):
    np = (p[0] + nd[0], p[1] + nd[1])
    x = grid[np[0]][np[1]]
    if x != "." and x != "E":
        return
    if np in v:
        return
    if VIZ:
        print(" also check {} (dir={})".format(np, nd))
    options.append( (np, nd, ns, v | frozenset([np])) )

def show(score, p, v):
    print("score={} vs {}, p={} end={}".format(score, best, p, e))
    for r, row in enumerate(grid):
        vr = []
        for c, x in enumerate(row):
            if p == (r,c) or (r,c) in v:
                vr.append("x")
            else:
                vr.append(x)
        print("".join(vr))

best = 0
while len(options) > 0:
    s, d, score, visited = options.pop()
    if VIZ:
        show(score, s, visited)
    if s == e:
        if VIZ:
            print("END!!!!!")
        if score > best:
            best = score
        continue

    l = (-d[1], d[0])
    r = (d[1], -d[0])
    trydir(s, d, score + 1, visited)
    trydir(s, l, score + 1001, visited)
    trydir(s, r, score + 1001, visited)

print("Part 1: ", best)
