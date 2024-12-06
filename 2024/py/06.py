import fileinput

grid = [[c for c in line.strip()] for line in fileinput.input()]
rows = len(grid)
cols = len(grid[0])
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "^":
            pos = (r, c)
            dir = (-1, 0)
        elif grid[r][c] == "v":
            pos = (r, c)
            dir = (1, 0)
        elif grid[r][c] == ">":
            pos = (r, c)
            dir = (0, 1)
        elif grid[r][c] == ">":
            pos = (r, c)
            dir = (1, 0)

def inside(pos, rows, cols):
    return 

def turn_right(dir):
    return (dir[1], dir[0] * -1)

visited = {}
while pos[0] >= 0 and pos[1] >= 0 and pos[0] < rows and pos[1] < cols:
    r, c = pos
    if grid[r][c] == "#":
        # backtrack.
        pos = (r - dir[0], c - dir[1])
        # turn right 90 degrees.
        dir = turn_right(dir)
    else:
        if pos not in visited:
            visited[pos] = []
        visited[pos].append(dir)
        pos = (r + dir[0], c + dir[1])
print("Part 1: {}".format(len(visited)))
