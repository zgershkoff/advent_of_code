# 2015 day 2

inFile = 'd02.txt'

def c1():
    total = 0
    with open(inFile, 'r') as f:
        for line in f.readlines():
            dims = [int(d) for d in line.strip().split('x')]
            total += helper1(dims)
    return total

def helper1(dims):
    a, b, c = dims
    side1 = a * b
    side2 = a * c
    side3 = b * c
    slack = min([side1, side2, side3])
    return (2 * side1 + 2 * side2 + 2 * side3 + slack)

def c2():
    total = 0
    with open(inFile, 'r') as f:
        for line in f.readlines():
            dims = [int(d) for d in line.strip().split('x')]
            total += helper2(dims)
    return total

def helper2(dims):
    dims.sort()
    perim = 2 * sum(dims[:2])
    ribbon = 1
    for i in range(3):
        ribbon *= dims[i]
    return perim + ribbon

if __name__ == "__main__":
    print(c2())
