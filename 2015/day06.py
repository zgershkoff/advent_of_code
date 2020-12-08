# day 6, year 2015

import re

inFile = "d06.txt"

data = []
grid = [[0 for _ in range(1000)] for _ in range(1000)]

def preprocess():
    with open(inFile, 'r') as f:
        for line in f.readlines():
            data.append(line[:4] + "_" + line[5:])

    action = {"turn_on": turn_on, "turn_off": turn_off, "togg_e": toggle}
    for line in data:
        instr = re.split(' |,', line)
        fn = action[instr[0]]
        x1, y1, x2, y2 = int(instr[1]), int(instr[2]), int(instr[4]), int(instr[5])
        act(x1, y1, x2, y2, fn)

    count = sum(light for line in grid for light in line)
    return count

def act(x1, y1, x2, y2, fn):
    for j in range(y1, y2+1):
        for i in range(x1, x2+1):
            fn(j, i)

def turn_on(j, i):
    grid[j][i] += 1

def turn_off(j, i):
    grid[j][i] = max(0, grid[j][i] - 1)

def toggle(j, i):
    grid[j][i] += 2

# these are the functions for part 1
# def turn_on(j, i):
#     grid[j][i] = 1

# def turn_off(j, i):
#     grid[j][i] = 0

# def toggle(j, i):
#     grid[j][i] = (grid[j][i] + 1) % 2

if __name__ == "__main__":
    print(preprocess())
