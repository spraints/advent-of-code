import fileinput

grid = [[c for c in line.strip()] for line in fileinput.input()]
rows = len(grid)
cols = len(grid[0])
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "^":
            start_pos = (r, c)
            start_dir = (-1, 0)
        elif grid[r][c] == "v":
            start_pos = (r, c)
            start_dir = (1, 0)
        elif grid[r][c] == ">":
            start_pos = (r, c)
            start_dir = (0, 1)
        elif grid[r][c] == ">":
            start_pos = (r, c)
            start_dir = (1, 0)

def inside(pos, rows, cols):
    return pos[0] >= 0 and pos[1] >= 0 and pos[0] < rows and pos[1] < cols

def turn_right(dir):
    return (dir[1], dir[0] * -1)

pos = start_pos
dir = start_dir
log = []
while inside(pos, rows, cols):
    r, c = pos
    if grid[r][c] == "#":
        # backtrack. we were never here.
        pos = (r - dir[0], c - dir[1])
        # turn right 90 degrees.
        dir = turn_right(dir)
    else:
        log.append((pos,dir))
        pos = (r + dir[0], c + dir[1])
print("Part 1: {}".format(len(set([pos for pos, _ in log]))))

def has_loop(grid, obs, dir, previously):
    pos = obs
    visited = set()
    while inside(pos, rows, cols):
        r, c = pos
        if grid[r][c] == "#" or pos == obs:
            # backtrack. we were never here.
            pos = (r - dir[0], c - dir[1])
            # turn right 90 degrees.
            dir = turn_right(dir)
        else:
            next_pos = (r + dir[0], c + dir[1])
            if (pos, dir) in previously:
                return True
            if (pos, dir) in visited:
                return True
            visited.add((pos, dir))
            pos = next_pos
    return False

obstructions = set()
visited = set()
visited_pos = set()
for pos, dir in log:
    if len(visited) == 0:
        # no obstruction at the starting position
        visited.add((pos, dir))
        visited_pos.add(pos)
    else:
        if pos not in obstructions and pos not in visited_pos and has_loop(grid, pos, dir, visited):
            obstructions.add(pos)
        visited.add((pos, dir))
        visited_pos.add(pos)
print("Part 2: {}".format(len(obstructions)))
