import fileinput
grid = [[c for c in line.strip()] for line in fileinput.input()]
rows = len(grid)
cols = len(grid[0])

regions = [[None for _ in row] for row in grid]
price_inputs = []
# All new regions have 1 area and 4 perimeter.
def new_region(crop):
    r = {"id": len(price_inputs), "c": crop, "a": 1, "p": 4, "p2": 4}
    price_inputs.append(r)
    return r
# Appending to a region is simple for part 1: we're adding one area and four
# perimeter, but there is one shared side, so we can eliminate two from the
# perimeter.
# For part 2, the perimeter change is more complex.
#
#  XXX
#  AA -> no perimeter change
#
#  AXX
#  AA -> adds 2 (new top and right, extends bottom)
#
#  XXA
#  AA -> no perimeter change4
#
#  AXA
#  AA -> adds 2
#
#  --
#
#  XAX
#  XA -> no perimeter change
#
#  XAA
#  XA -> adds 2 (new right and bottom, extends left)
#
#  AAA
#  XA -> adds 3 (new right and bottom and left)
#
#  AAX
#  XA -> adds 2 (new bottom and left, extends right)
def append_to_region(reg, pos):
    while "goto" in reg:
        reg = price_inputs[reg["goto"]]
    reg["a"] += 1
    reg["p"] += 2 # Add 4 (the new plot), subtract 2 (the shared edge)
    neighbors = 0
    r, c = pos
    ul = region_id((r-1, c-1)) == reg["id"]
    u = region_id((r-1,c)) == reg["id"]
    ur = region_id((r-1,c+1)) == reg["id"]
    l = region_id((r,c-1)) == reg["id"]
    if l:
        if ul:
            reg["p2"] += 2
    else: # u must be true.
        if ul and ur:
            reg["p2"] += 3
        elif ul or ur:
            reg["p2"] += 2
    return reg
# Adding onto a region that touches the top and left is simple for part 1:
# always add 1 area and 0 perimeter (the new square has 4 new sides, but it
# shares 2 edges, so 4 - 2x2 = 0 total new fences).
# For part 2, it depends on other neighbors:
#
#  XAX
#  AA -> reduces total by 2.
#
#  AAX
#  AA -> reduces total by 2.
#
#  XAA
#  AA -> no change
def mega_region(r1, r2, pos):
    while "goto" in r1:
        r1 = price_inputs[r1["goto"]]
    while "goto" in r2:
        r2 = price_inputs[r2["goto"]]
    if r1["id"] != r2["id"]:
        r1["a"] += r2["a"]
        r1["p"] += r2["p"]
        r1["p2"] += r2["p2"]
        r2["goto"] = r1["id"]
    r1["a"] += 1
    # r1["p"] doesn't change
    r, c = pos
    if region_id((r-1,c+1)) != r1["id"]:
        r1["p2"] -= 2
    return r1
def region_id(pos):
    r, c = pos
    if r >= 0 and r < rows and c >= 0 and c < cols:
        reg = regions[r][c]
        while "goto" in reg:
            reg = price_inputs[reg["goto"]]
        return reg["id"]
    else:
        return None
regrid = ""
for r, row in enumerate(grid):
    for c, crop in enumerate(row):
        regrid += crop
        region_above = regions[r-1][c] if r > 0 and grid[r-1][c] == crop else None
        region_left = regions[r][c-1] if c > 0 and grid[r][c-1] == crop else None
        my_region = None
        if region_above is not None and region_left is not None:
            my_region = mega_region(region_above, region_left, (r, c))
        elif region_above is not None:
            my_region = append_to_region(region_above, (r, c))
        elif region_left is not None:
            my_region = append_to_region(region_left, (r, c))
        else:
            my_region = new_region(crop)
        #print(regrid)
        #print(my_region)
        regions[r][c] = my_region
    regrid += "\n"

def price(pi):
    if "goto" in pi:
        return 0
    return pi["a"] * pi["p"]
total_price = sum([price(pi) for pi in price_inputs])
print("Part 1:", total_price)

def price2(pi):
    if "goto" in pi:
        return 0
    return pi["a"] * pi["p2"]
total_price = sum([price2(pi) for pi in price_inputs])
#for pi in price_inputs:
#    if "goto" not in pi:
#        print(pi)
print("Part 2:", total_price)
