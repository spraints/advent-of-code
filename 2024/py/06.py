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
obstructions = set()
while pos[0] >= 0 and pos[1] >= 0 and pos[0] < rows and pos[1] < cols:
    r, c = pos
    if grid[r][c] == "#":
        # backtrack. we were never here.
        pos = (r - dir[0], c - dir[1])
        # turn right 90 degrees.
        dir = turn_right(dir)
    else:
        next_pos = (r + dir[0], c + dir[1])
        if pos in visited:
            r = turn_right(dir)
            if turn_right(dir) in visited[pos]:
                obstructions.add(next_pos)
        else:
            visited[pos] = set()
        visited[pos].add(dir)
        pos = next_pos
print("Part 1: {}".format(len(visited)))
#print(obstructions)
print("Part 2: {}".format(len(obstructions)))
