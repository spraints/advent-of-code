import fileinput, re

s = "".join(fileinput.input())

class Game:
    def __init__(self, ax, ay, bx, by, px, py):
        self.ax = ax
        self.ay = ay
        self.bx = bx
        self.by = by
        self.px = px
        self.py = py

    def __str__(self):
        return "A:({},{}) B:({},{}) => ({},{})".format(self.ax, self.ay, self.bx, self.by, self.px, self.py)

games = []
#for ax, bx in re.findall(r'Button A: X+([0-9]+), Y+([0-9]+)', s):
for ax, ay, bx, by, px, py in re.findall(r'Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)', s):
    games.append(Game(int(ax), int(ay), int(bx), int(by), int(px), int(py)))
