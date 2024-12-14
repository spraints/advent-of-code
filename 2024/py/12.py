import fileinput
grid = [[c for c in line.strip()] for line in fileinput.input()]

regions = [[None for _ in row] for row in grid]
price_inputs = []
def new_region(crop):
    r = {"id": len(price_inputs), "c": crop, "a": 1, "p": 4}
    price_inputs.append(r)
    return r
def append_to_region(r):
    while "goto" in r:
        r = price_inputs[r["goto"]]
    r["a"] += 1
    r["p"] += 2 # Add 4 (the new plot), subtract 2 (the shared edge)
    return r
def mega_region(r1, r2):
    while "goto" in r1:
        r1 = price_inputs[r1["goto"]]
    while "goto" in r2:
        r2 = price_inputs[r2["goto"]]
    if r1["id"] != r2["id"]:
        r1["a"] += r2["a"]
        r1["p"] += r2["p"]
        r2["goto"] = r1["id"]
    r1["a"] += 1
    # r1["p"] doesn't change
    return r1
for r, row in enumerate(grid):
    for c, crop in enumerate(row):
        region_above = regions[r-1][c] if r > 0 and grid[r-1][c] == crop else None
        region_left = regions[r][c-1] if c > 0 and grid[r][c-1] == crop else None
        my_region = None
        if region_above is not None and region_left is not None:
            my_region = mega_region(region_above, region_left)
        elif region_above is not None:
            my_region = append_to_region(region_above)
        elif region_left is not None:
            my_region = append_to_region(region_left)
        else:
            my_region = new_region(crop)
        regions[r][c] = my_region
        #print(((r,c), region_above, region_left, my_region))
def price(pi):
    if "goto" in pi:
        return 0
    return pi["a"] * pi["p"]
total_price = sum([price(pi) for pi in price_inputs])
print("Part 1:", total_price)
