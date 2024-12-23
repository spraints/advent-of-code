import fileinput

VIZ = False

grid = []
grid2 = []
input = fileinput.input()
for line in input:
    line = line.strip()
    if line == "":
        break

    row = [c for c in line]
    grid.append(row)

    row2 = []
    for c in row:
        match c:
            case "#":
                row2 += ["#", "#"]
            case "O":
                row2 += ["[", "]"]
            case ".":
                row2 += [".", "."]
            case "@":
                row2 += [".", "."]
    grid2.append(row2)
instructions = [c for line in input for c in line.strip()]

robot = None
for r, row in enumerate(grid):
    for c, x in enumerate(row):
        if x == "@":
            robot = (r,c)
            grid[r][c] = "."
robot2 = (robot[0], 2*robot[1])

def show(g, r):
    rr, rc = r
    g[rr][rc] = "@"
    for row in g:
        print("".join(row))
    g[rr][rc] = "."

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
        print("\n[{}] Move {}:".format(i, step))
        show(grid, (rr, rc))

total_score = 0
for r, row in enumerate(grid):
    for c, x in enumerate(row):
        if x == "O":
            total_score += 100 * r
            total_score += c
print("Part 1:", total_score)

def shift2(g, d, r):
    is_vertical = d[1] == 0
    nr = r[0] + d[0]
    nc = r[1] + d[1]
    match (g[nr][nc], is_vertical):
        case ".", _:
            return (nr, nc)
        case "#", _:
            return None
        case _, False:
            nn = shift2(g, d, (nr, nc))
            if nn is None:
                return None
            nnr, nnc = nn
            g[nnr][nnc] = g[nr][nc]
            g[nr][nc] = "."
            return (nr, nc)
        case "[", True:
            ln = shift2(g, d, (nr, nc))
            rn = shift2(g, d, (nr, nc+1))
            if ln is None or rn is None:
                if VIZ:
                    print("todo: may need to undo [")
                return None
            g[ln[0]][ln[1]] = g[nr][nc]
            g[rn[0]][rn[1]] = g[nr][nc+1]
            g[nr][nc] = "."
            g[nr][nc+1] = "."
            return (nr, nc)
        case "]", True:
            ln = shift2(g, d, (nr, nc-1))
            rn = shift2(g, d, (nr, nc))
            if ln is None or rn is None:
                if VIZ:
                    print("todo: may need to undo ]")
                return None
            g[ln[0]][ln[1]] = g[nr][nc-1]
            g[rn[0]][rn[1]] = g[nr][nc]
            g[nr][nc-1] = "."
            g[nr][nc] = "."
            return (nr, nc)
    raise RuntimeError("illegal {},{} {}".format(nr, nc, grid[nr][nc]))

if VIZ:
    print("\n[*] Start part 2:")
    show(grid2, robot2)
for i, step in enumerate(instructions):
    next_robot2 = shift2(grid2, dirs[step], robot2)
    if next_robot2 is not None:
        robot2 = next_robot2
    if VIZ:
        print("\n[{}] Move {}:".format(i, step))
        show(grid2, robot2)

show(grid2, robot2)
total_score = 0
for r, row in enumerate(grid2):
    for c, x in enumerate(row):
        if x == "[":
            if VIZ:
                print("({},{}) = {}".format(r, c, 100 * r + c))
            total_score += 100 * r
            total_score += c
print("Part 2:", total_score) # 1506094 is too low
