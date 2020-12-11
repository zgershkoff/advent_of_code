# day 11, 2020

from collections import Counter

inFile = "d11.txt"

grid = []
# for part 1, too_many is 4
too_many = 5

def preprocess():
    with open(inFile, 'r') as f:
        grid.extend([line.strip() for line in f.readlines()])

def neighbors1(i, j):
    return [(a, b) for a in range(i-1, i+2) for b in range(j-1, j+2)
            if (0 <= a < len(grid)) and (0 <= b < len(grid[0]))
            and (a != i or b != j)]

def fetch_from_grid(grid, l):
    return Counter([grid[a][b] for a, b in l])

def automate(grid):
    new_grid = []
    for i, row in enumerate(grid):
        new_row = []
        for j in range(len(row)):
            surroundings = fetch_from_grid(grid, neighbors(i, j))
            if grid[i][j] == ".":
                new_row.append(".")
            elif grid[i][j] == "#":
                if surroundings["#"] >= too_many:
                    new_row.append("L")
                else:
                    new_row.append("#")
            elif grid[i][j] == "L":
                if surroundings["#"] > 0:
                    new_row.append("L")
                else:
                    new_row.append("#")
        new_grid.append(new_row)
    return new_grid

def do_it(grid):
    while True:
        new_grid = automate(grid)
        if new_grid == grid:
            break
        grid = new_grid
        print(sum(row.count("#") for row in grid))
    return sum(row.count("#") for row in grid)

# for part 2, too_many becomes 5, and I need a new neighbors function
def neighbors(i, j):
    return neighbors2(i, j)

def neighbors2(i, j):
    def move(i, j, hor, vert):
        # hor and vert are in [-1, 0, 1]
        if (vert == -1 and i == 0) or (vert == 1 and i == len(grid) - 1):
            return None
        if (hor == -1 and j == 0) or (hor == 1 and j == len(grid[0]) - 1):
            return None
        i += vert
        j += hor
        if grid[i][j] == ".":
            return move(i, j, hor, vert)
        return (i, j)

    ans = [move(i, j, hor, vert) for hor in [-1,0,1] for vert in [-1,0,1]
           if hor != 0 or vert != 0]
    return [item for item in ans if item]

if __name__ == "__main__":
    preprocess()
    print(do_it(grid))
