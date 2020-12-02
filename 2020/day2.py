# advent of code, day 2, challenges 1 and 2

from collections import Counter

inFile = "d2.txt"

def preprocess():
    total = 0
    with open(inFile, 'r') as f:
        for line in f.readlines():
            parts = line.split()
            lb, ub = [int(p) for p in parts[0].split('-')]
            target = parts[1][0]
            pw = parts[2].strip()

            total += challenge1(lb, ub, target, pw)
    return total

def challenge1(lb, ub, target, pw):
    C = Counter(pw)
    if lb <= C[target] <= ub:
        return 1
    return 0

def challenge2(lb, ub, target, pw):
    if (pw[lb-1] == target) != (pw[ub-1] == target):
        return 1
    return 0

if __name__ == "__main__":
    print(preprocess())
