# 2015 day 3

inFile = 'd3.txt'

def get_input():
    with open(inFile, 'r') as f:
        for line in f.readlines():
            # only one line
            return line.strip()

def c1():
    visited = set([(0, 0)])
    coords = [0, 0]
    steps = {'>': (1, 0), '<': (-1, 0), '^': (0, 1), 'v': (0, -1)}
    dirs = get_input()

    for c in dirs:
        for i, val in enumerate(steps[c]):
            coords[i] += val
        visited.add(tuple(coords))
    return len(visited)

def c2():
    visited = set([(0, 0)])
    coords_list = [[0, 0], [0, 0]]
    switcher = 0
    steps = {'>': (1, 0), '<': (-1, 0), '^': (0, 1), 'v': (0, -1)}
    dirs = get_input()

    for c in dirs:
        for i, val in enumerate(steps[c]):
            coords_list[switcher][i] += val
        visited.add(tuple(coords_list[switcher]))
        switcher = (switcher + 1) % 2

    return len(visited)

if __name__ == "__main__":
    print(c2())
