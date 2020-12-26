# advent of code 2020, day 17

# my part 1 solution did not scale well to higher dimensions.
# I'm not cleaning up the extra prints and stuff.

inFile = 'd17.txt'

grid = []

def neighbors(i, j, k):
    # use nonnegative indices
    depth = len(grid)
    height = len(grid[0])
    width = len(grid[0][0])

    z_range = range(max(i-1, 0), min(i+2, depth))
    y_range = range(max(j-1, 0), min(j+2, height))
    x_range = range(max(k-1, 0), min(k+2, width))

    return [grid[a][b][c] for a in z_range for b in y_range for c in x_range
            if (a, b, c) != (i, j, k)]

def preprocess():
    layer = []
    with open(inFile, 'r') as f:
        for line in f:
            layer.append(list(line.strip()))
    grid.append(layer)

def iterate():
    global grid
    new_grid = []
    for i in range(-1, len(grid)+1):
        layer = []
        for j in range(-1, len(grid[0])+1):
            row = []
            for k in range(-1, len(grid[0][0])+1):
                if (i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or
                    k < 0 or k >= len(grid[0][0])):
                    cur = "."
                else:
                    cur = grid[i][j][k]
                if cur == ".":
                    if neighbors(i, j, k).count("#") == 3:
                        next_sym = "#"
                    else:
                        next_sym = "."
                elif cur == "#":
                    if neighbors(i, j, k).count("#") in [2, 3]:
                        next_sym = "#"
                    else:
                        next_sym = "."
                row.append(next_sym)
                # print(cur, neighbors(i, j, k).count("#"), next_sym)
            layer.append(row)

        new_grid.append(layer)
    grid = new_grid

def part1(cycles = 6):
    for _ in range(cycles):
        iterate()
    return(sum(1 for layer in grid for row in layer for item in row if item == "#"))

def part2(cycles = 6):
    global grid
    hypergrid = [grid]






    for _ in range(cycles):
        hypergrid = iterate2(hypergrid)

    # grid = hypergrid
    # for i in range( len(grid) ):
    #     for j in range(len(grid[0]) ):
    #         for k in range(len(grid[0][0]) ):
    #             for l in range(len(grid[0][0][0])):
    #                 print(grid[i][j][k][l], neighbors2(i,j,k,l).count("#"))
    #             print()
    #         print()
    #     print()

    # for box in hypergrid:
    #     for layer in box:
    #         for row in layer:
    #             print(row)
    #         print()
    #     print()

    return(sum(1 for box in hypergrid for layer in box for row in layer
               for item in row if item == "#"))

def neighbors2(i, j, k, l, grid):
    # use nonnegative indices
    depth = len(grid)
    height = len(grid[0])
    width = len(grid[0][0])
    next_dim = len(grid[0][0][0])

    z_range = range(max(i-1, 0), min(i+2, depth))
    y_range = range(max(j-1, 0), min(j+2, height))
    x_range = range(max(k-1, 0), min(k+2, width))
    w_range = range(max(l-1, 0), min(l+2, next_dim))

    return [grid[a][b][c][d] for a in z_range for b in y_range for c in x_range
            for d in w_range if (a, b, c, d) != (i, j, k, l)]

def iterate2(grid):
    new_grid = []
    for i in range(-1, len(grid)+1):
        box = []
        for j in range(-1, len(grid[0])+1):
            layer = []
            for k in range(-1, len(grid[0][0])+1):
                row = []
                for l in range(-1, len(grid[0][0][0])+1):
                    if (i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or
                        k < 0 or k >= len(grid[0][0]) or l < 0 or
                        l >= len(grid[0][0][0])):
                        cur = "."
                    else:
                        cur = grid[i][j][k][l]
                    if cur == ".":
                        if neighbors2(i, j, k, l, grid).count("#") == 3:
                            next_sym = "#"
                        else:
                            next_sym = "."
                    elif cur == "#":
                        if neighbors2(i, j, k, l, grid).count("#") in [2, 3]:
                            next_sym = "#"
                        else:
                            next_sym = "."
                    row.append(next_sym)
                    # print(cur, neighbors(i, j, k).count("#"), next_sym)
                layer.append(row)
            box.append(layer)
        new_grid.append(box)

    return new_grid

if __name__ == "__main__":
    preprocess()
    print(part2(6))
