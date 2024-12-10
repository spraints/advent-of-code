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
#show(positions)

#res = ""
i = 0
csum = 0
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
            positions.pop()
        csum += (lid * (i * lw + lw * (lw - 1) // 2))
        #res += (str(lid) * lw)
        i += lw
        #print(res)
        #print(csum)
    # append this file.
    csum += (id * (i * w + w * (w - 1) // 2))
    #res += (str(id) * w)
    i += w
    #print(res)
    #print(csum)
#print(res)
print("Part 1: {}".format(csum))
