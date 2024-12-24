import fileinput, heapq

VIZ = False

grid = [[c for c in line.strip()] for line in fileinput.input()]

#      (-1,0)
# (0,-1)  @  (0,1)
#       (1,0)
alldirs = frozenset([(-1,0), (0,1), (1,0), (0,-1)])

INFINITY = float("inf")

start = None
end = None
init_dir = (0,1)
unvisited = set()
dist = {}
for r, row in enumerate(grid):
    for c, cell in enumerate(row):
        if cell == "#":
            continue
        p = (r,c)
        for d in alldirs:
            node = (p, d)
            unvisited.add(node)
            dist[node] = INFINITY
        if cell == "S":
            start = p
        if cell == "E":
            end = p

def neighbors(node):
    p, d = node
    l = (-d[1], d[0])
    r = (d[1], -d[0])
    for nd, cost in [(d, 1), (l, 1001), (r, 1001)]:
        np = (p[0] + nd[0], p[1] + nd[1])
        if grid[np[0]][np[1]] != "#":
            yield (np, nd), cost

dist[(start, init_dir)] = 0
best = None
while unvisited:
    cur = min(unvisited, key=lambda node: dist[node])
    unvisited.remove(cur)
    if dist[cur] == INFINITY:
        raise("no path, sorry")
    for neighbor, cost in neighbors(cur):
        ns = cost + dist[cur]
        if ns < dist[neighbor]:
            dist[neighbor] = ns
    if cur[0] == end:
        best = dist[cur]
        break
print("Part 1: ", best)
