import fileinput, re

s = "".join(fileinput.input())

class Game:
    def __init__(self, raw, ax, ay, bx, by, px, py):
        self.raw = raw
        self.ax = ax
        self.ay = ay
        self.bx = bx
        self.by = by
        self.px = px
        self.py = py

    def __str__(self):
        return self.raw

    def solve(self):
        d = (self.bx * self.ay - self.by * self.ax)
        if d == 0:
            return None
        b = (self.px * self.ay - self.py * self.ax) // d
        if b < 0:
            return None
        a = (self.px - b * self.bx) // self.ax
        if a * self.ax + b * self.bx != self.px:
            return None
        if a * self.ay + b * self.by != self.py:
            return None
        return (a, b)

games = []
#for ax, bx in re.findall(r'Button A: X+([0-9]+), Y+([0-9]+)', s):
for raw, ax, ay, bx, by, px, py in re.findall(r'(Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+))', s):
    games.append(Game(raw, int(ax), int(ay), int(bx), int(by), int(px), int(py)))

# total cost: a*3 + b
# final position: (a * ax + b * bx, a * ay + b * by) = (px, py)
# 1: a * ax + b * bx = px
# 2: a * ay + b * by = py
# 1 * ay: a * ax * ay + b * bx * ay = px * ay
# 2 * ax: a * ay * ax + b * by * ax = py * ax
# 1 * ay - 2 * ax: b * (bx * ay - by * ax) = px * ay - py * ax
# ..: b = (px * ay - py * ax) / (bx * ay - by * ax)
# 1: a = (px - b * bx) / ax

ta = 0
tb = 0
for g in games:
    print(g)
    sol = g.solve()
    if sol is not None:
        a, b = sol
        print("=> {}, {}".format(a, b))
        ta += a
        tb += b
part1 = ta * 3 + tb
print("Part 1: ", part1, " (42606 is too high)")
