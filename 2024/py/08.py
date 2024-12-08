import fileinput
grid = [[c for c in line.strip()] for line in fileinput.input()]
rows = len(grid)
cols = len(grid[0])
by_freq = {}
antinodes = set()
antinodes2 = set()
for r in range(rows):
    for c in range(cols):
        this = (r,c)
        x = grid[r][c]
        if x != ".":
            if x in by_freq:
                for other in by_freq[x]:
                    dr = other[0] - this[0]
                    dc = other[1] - this[1]
                    for m in range(rows + cols):
                        ar = other[0] + m * dr
                        ac = other[1] + m * dc
                        if ar >= 0 and ar < rows and ac >=0 and ac < cols:
                            p = (ar, ac)
                            antinodes2.add(p)
                            if m == 1:
                                antinodes.add(p)
                        else:
                            break
                    for m in range(rows + cols):
                        ar = this[0] - m * dr
                        ac = this[1] - m * dc
                        if ar >= 0 and ar < rows and ac >=0 and ac < cols:
                            p = (ar, ac)
                            antinodes2.add(p)
                            if m == 1:
                                antinodes.add(p)
                        else:
                            break
                by_freq[x].add(this)
            else:
                by_freq[x] = {this}
print("Part 1: {}".format(len(antinodes)))
print("Part 2: {}".format(len(antinodes2)))
