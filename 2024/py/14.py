import fileinput, re, os

robots = [re.match(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)", line) for line in fileinput.input()]
robots = [((int(x[1]),int(x[2])), (int(x[3]),int(x[4]))) for x in robots]
size = (101, 103) if os.getenv("IS_REAL_INPUT") == "Y" else (11, 7)

grid = [[0 for _ in range(size[0])] for _ in range(size[1])]
final_positions = []
for p, v in robots:
    px, py = p
    vx, vy = v
    fpx = (px + 100 * vx) % size[0]
    fpy = (py + 100 * vy) % size[1]
    final_positions.append((fpx, fpy))
    #print((fpx, fpy))
    grid[fpy][fpx] += 1
#for line in grid:
#    for count in line:
#        if count == 0:
#            print(".", end="")
#        else:
#            print(count, end="")
#    print("")
qs = [0, 0, 0, 0]
midx = size[0] // 2
midy = size[1] // 2
for fpx, fpy in final_positions:
    if fpx < midx and fpy < midy:
        qs[0] += 1
    elif fpx > midx and fpy < midy:
        qs[1] += 1
    elif fpx < midx and fpy > midy:
        qs[2] += 1
    elif fpx > midx and fpy > midy:
        qs[3] += 1
res = qs[0]
for q in qs[1:]:
    res *= q
print("Part 1: ", res)
