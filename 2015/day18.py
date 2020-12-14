# day 18, 2015
# since day 11, 2020 was also cellular automata, I'm adapting from that

from collections import Counter

inFile = "d18.txt"
iterations = 100

grid = []
corners = []

def preprocess():
    with open(inFile, 'r') as f:
        grid.extend([line.strip() for line in f.readlines()])
        corners.extend([(0,0), (0, len(grid[0])-1), (len(grid)-1, 0), \
         (len(grid)-1, len(grid[0])-1)])

def neighbors(i, j):
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
            # this check is for part 2
            if (i, j) in corners:
                new_row.append("#")
                continue
            surroundings = fetch_from_grid(grid, neighbors(i, j))
            if grid[i][j] == ".":
                if surroundings["#"] == 3:
                    new_row.append("#")
                else:
                    new_row.append(".")
            elif grid[i][j] == "#":
                if surroundings["#"] in [2, 3]:
                    new_row.append("#")
                else:
                    new_row.append(".")
        new_grid.append(new_row)
    return new_grid

def do_it(grid):
    for _ in range(iterations):
        grid = automate(grid)
    return sum(row.count("#") for row in grid)


if __name__ == "__main__":
    preprocess()
    print(do_it(grid))
