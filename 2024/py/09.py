import fileinput
def p(c):
    match c:
        case "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9":
            return int(c)
        case _:
            return None
digits = [d for d in (p(c) for line in fileinput.input() for c in line) if d is not None]
positions = []
sz = 0
for i, x in enumerate(digits):
    if i % 2 == 0:
        positions.append((i//2, sz, x))
        sz += x
    else:
        sz += x

def show(positions):
    s = ""
    for id, start, w in positions:
        while len(s) < start:
            s += "."
        for _ in range(w):
            s += "{}".format(id)
    print(s)

def csum(positions):
    csum = 0
    for id, start, w in positions:
        csum += id * (start * w + w * (w - 1) // 2)
    return csum

pos1 = []
i = 0
while len(positions) > 0:
    # Get the next file.
    id, start, w = positions[0]
    positions = positions[1:]
    while start > i and len(positions) > 0:
        # fill in the gap from files at the end.
        gap = start - i
        lid, lstart, lw = positions[-1]
        if lw > gap:
            positions[-1] = (lid, lstart, lw - gap)
            lw = gap
        else:
            positions = positions[:-1]
        pos1.append((lid, i, lw))
        i += lw
    # append this file.
    pos1.append((id, i, w))
    i += w
#show(positions)
#show(pos1)
print("Part 1: {}".format(csum(pos1)))
