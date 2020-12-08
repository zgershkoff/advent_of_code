# TSP on 8 vertices can be brute forced

from itertools import permutations

inFile = "d09.txt"
# model graph as dictionary of dictionaries
g = {}

def preprocess():
    with open(inFile, 'r') as f:
        for line in f.readlines():
            parts = line.split()
            for p1, p2 in [(parts[0], parts[2]), (parts[2], parts[0])]:
                if p1 not in g:
                    g[p1] = {}
                g[p1][p2] = int(parts[-1])

def tsp():
    best = float('inf')
    for p in permutations(g):
        distances = []
        for i in range(8): # len(p) = 8
            distances.append(g[p[i]][p[(i+1)%8]])
        distances.remove(max(distances))
        best = min(best, sum(distances))
    return best

def max_tsp():
    best = 0
    for p in permutations(g):
        distances = []
        for i in range(8): # len(p) = 8
            distances.append(g[p[i]][p[(i+1)%8]])
        distances.remove(min(distances))
        best = max(best, sum(distances))
    return best

if __name__ == "__main__":
    preprocess()
    print(tsp())
    print(max_tsp())
