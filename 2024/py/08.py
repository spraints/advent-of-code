import fileinput
grid = [[c for c in line.strip()] for line in fileinput.input()]
rows = len(grid)
cols = len(grid[0])
by_freq = {}
antinodes = set()
for r in range(rows):
    for c in range(cols):
        this = (r,c)
        x = grid[r][c]
        if x != ".":
            if x in by_freq:
                for other in by_freq[x]:
                    dr = other[0] - this[0]
                    dc = other[1] - this[1]
                    ar = other[0] + dr
                    ac = other[1] + dc
                    if ar >= 0 and ar < rows and ac >=0 and ac < cols:
                        antinodes.add((ar, ac))
                    br = this[0] - dr
                    bc = this[1] - dc
                    if br >= 0 and br < rows and bc >=0 and bc < cols:
                        antinodes.add((br, bc))
                    # print([x, this, other, (ar, ac), (br, bc)])
                by_freq[x].add(this)
            else:
                by_freq[x] = {this}
print("Part 1: {}".format(len(antinodes)))
