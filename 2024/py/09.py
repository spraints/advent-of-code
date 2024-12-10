import fileinput
def p(c):
    match c:
        case "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9":
            return int(c)
        case _:
            return None
digits = [d for d in (p(c) for line in fileinput.input() for c in line) if d is not None]
orig_positions = []
gaps = [] # dict of {size: set(positions)}
sz = 0
for i, x in enumerate(digits):
    if i % 2 == 0:
        orig_positions.append((i//2, sz, x))
        sz += x
    else:
        while x >= len(gaps):
            gaps.append(set())
        gaps[x].add(sz)
        sz += x
#print(gaps)

def show(positions):
    s = ""
    l = 0
    for id, start, w in positions:
        if l < start:
            s += "."*(start - l)
            l += (start - l)
        s += ("[{}]".format(id))*w
        l += w
    print(s)

def csum(positions):
    csum = 0
    for id, start, w in positions:
        csum += id * (start * w + w * (w - 1) // 2)
    return csum

positions = orig_positions
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
show(orig_positions)
#show(pos1)
print("Part 1: {}".format(csum(pos1)))

def choose_gap(gaps, start, w):
    best_idx = None
    best_w = None
    for off, idxs in enumerate(gaps[w:]):
        if len(idxs) == 0:
            continue
        if best_idx is None:
            best_idx = min(idxs)
            best_w = w + off
        else:
            new_idx = min(idxs)
            if new_idx < best_idx:
                best_idx = new_idx
                best_w = w + off
    return best_idx, best_w

pos2 = []
for id, start, w in reversed(orig_positions):
    new_start, gap_size = choose_gap(gaps, start, w)
    if new_start is not None:
        pos2.append((id, new_start, w))
        gaps[gap_size].remove(new_start)
        gaps[gap_size - w].add(new_start + w)
    else:
        pos2.append((id,start,w))

def st(pos):
    return pos[1]
pos2 = sorted(pos2, key=st)
#print(orig_positions)
#print(pos2)
show(pos2)
print("Part 2: {} (8439434080946 is too high)".format(csum(pos2)))
