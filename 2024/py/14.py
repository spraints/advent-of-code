import fileinput, re, os

robots = [re.match(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)", line) for line in fileinput.input()]
robots = [((int(x[1]),int(x[2])), (int(x[3]),int(x[4]))) for x in robots]
is_real_input = os.getenv("IS_REAL_INPUT") == "Y"
size = (101, 103) if is_real_input else (11, 7)

def show_grid(positions):
    for y in range(size[1]):
        for x in range(size[0]):
            print(positions.get((x,y), "."), end="")
        print("")

def steps(n):
    res = {}
    for p, v in robots:
        px, py = p
        vx, vy = v
        fp = ((px + n * vx) % size[0], (py + n * vy) % size[1])
        if fp in res:
            res[fp] += 1
        else:
            res[fp] = 1
    return res

def score(positions):
    qs = [0, 0, 0, 0]
    midx = size[0] // 2
    midy = size[1] // 2
    for fp, count in positions.items():
        fpx, fpy = fp
        if fpx < midx and fpy < midy:
            qs[0] += count
        elif fpx > midx and fpy < midy:
            qs[1] += count
        elif fpx < midx and fpy > midy:
            qs[2] += count
        elif fpx > midx and fpy > midy:
            qs[3] += count
    res = qs[0]
    for q in qs[1:]:
        res *= q
    return res

part1_positions = steps(100)
print("Part 1: ", score(part1_positions))

if is_real_input:
    needed = 2
    for i in range(1, 100000):
        pos = steps(i)
        if len(pos) == len(robots):
            x = steps(i)
            show_grid(x)
            print("Part 2: ", i, " ", score(x))
            needed -= 1
            if needed < 1:
                break
