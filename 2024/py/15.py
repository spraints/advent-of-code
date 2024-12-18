import fileinput

VIZ = False

grid = []
input = fileinput.input()
for line in input:
    line = line.strip()
    if line == "":
        break
    grid.append([c for c in line])
instructions = [c for line in input for c in line.strip()]

robot = None
for r, row in enumerate(grid):
    for c, x in enumerate(row):
        if x == "@":
            robot = (r,c)
            grid[r][c] = "."

dirs = {">": (0,1), "<": (0,-1), "^": (-1,0), "v": (1,0)}
rr, rc = robot
for i, step in enumerate(instructions):
    dr, dc = dirs[step]
    r2r = nr = rr + dr
    r2c = nc = rc + dc
    while grid[nr][nc] == "O":
        nr += dr
        nc += dc
    if grid[nr][nc] == ".":
        grid[r2r][r2c], grid[nr][nc] = grid[nr][nc], grid[r2r][r2c]
        rr = r2r
        rc = r2c
    if VIZ:
        grid[rr][rc] = "@"
        print("\n[{}] Move {}:".format(i, step))
        for row in grid:
            print("".join(row))
        grid[rr][rc] = "."

total_score = 0
for r, row in enumerate(grid):
    for c, x in enumerate(row):
        if x == "O":
            total_score += 100 * r
            total_score += c
print("Part 1:", total_score)
