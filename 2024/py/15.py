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

def move(g, d, r):
    moves_in = {} # (r,c) => new_c
    moves_out = set() # (r,c) of vacated spaces
    nr = (r[0] + d[0], r[1] + d[1])
    if not can_move(g, d, nr, ".", moves_in, moves_out):
        return r
    for pos in moves_out:
        g[pos[0]][pos[1]] = "."
    for pos, c in moves_in.items():
        g[pos[0]][pos[1]] = c
    return nr

def can_move(g, d, pos, new_c, moves_in, moves_out):
    is_vertical = d[1] == 0
    old_c = g[pos[0]][pos[1]]
    next_pos = (pos[0] + d[0], pos[1] + d[1])
    match (old_c, is_vertical):
        case ".", _:
            moves_in[pos] = new_c
            return True
        case "#", _:
            return False
        case _, False:
            if not can_move(g, d, next_pos, old_c, moves_in, moves_out):
                return False
            moves_out.add(pos)
            moves_in[pos] = new_c
            return True
        case "[", True:
            if not can_move(g, d, next_pos, old_c, moves_in, moves_out):
                return False
            pair_pos = (next_pos[0], next_pos[1]+1)
            if not can_move(g, d, pair_pos, "]", moves_in, moves_out):
                return False
            moves_out.add(pos)
            moves_out.add((pos[0], pos[1]+1))
            moves_in[pos] = new_c
            return True
        case "]", True:
            if not can_move(g, d, next_pos, old_c, moves_in, moves_out):
                return False
            pair_pos = (next_pos[0], next_pos[1]-1)
            if not can_move(g, d, pair_pos, "[", moves_in, moves_out):
                return False
            moves_out.add(pos)
            moves_out.add((pos[0], pos[1]-1))
            moves_in[pos] = new_c
            return True
    raise RuntimeError("illegal pos={} dir={} c={}".format(pos, d, old_c))

if VIZ:
    print("\n[*] Start part 2: ", robot2)
    show(grid2, robot2)
for i, step in enumerate(instructions):
    robot2 = move(grid2, dirs[step], robot2)
    if VIZ:
        print("\n[{}] Move {}: {}".format(i, step, robot2))
        show(grid2, robot2)

# show(grid2, robot2)
total_score = 0
for r, row in enumerate(grid2):
    for c, x in enumerate(row):
        if x == "[":
            if VIZ:
                print("({},{}) = {}".format(r, c, 100 * r + c))
            total_score += 100 * r
            total_score += c
print("Part 2:", total_score) # 1506094 is too low
