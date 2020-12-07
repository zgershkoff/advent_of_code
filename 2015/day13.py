# day 13, 2015
# another TSP

from collections import defaultdict
from itertools import permutations

inFile = "d13.txt"

g = {}

def preprocess():
    with open(inFile, 'r') as f:
        for line in f.readlines():
            parts = line.strip('.\n').split()
            name1 = parts[0]
            sign = 1 if parts[2] == "gain" else -1
            qty = int(parts[3]) * sign
            name2 = parts[-1]

            for n1, n2 in [(name1, name2), (name2, name1)]:
                if n1 not in g:
                    g[n1] = defaultdict(int)
                g[n1][n2] += qty

    # for part 2:
    g["me"] = defaultdict(int)
    # because everything not in the dictionaries will default
    # to a value of 0, this small change happens to work perfectly

    return tsp()

def tsp():
    best = -float('inf')
    for p in permutations(g):
        score = 0
        for i in range(8):
            score += g[p[i]][p[i-1]]
        best = max(best, score)

    return best

if __name__ == "__main__":
    print(preprocess())
