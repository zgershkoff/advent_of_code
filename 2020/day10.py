# day 10, 2020

inFile = "d10.txt"

l = [0]

def preprocess():
    with open(inFile, 'r') as f:
        # print(type([int(line) for line in f.readlines]))
        l.extend([int(line) for line in f.readlines()])
    l.sort()
    l.append(l[-1] + 3)

def part1():
    jumps = [0, 0, 0]
    for i in range(1, len(l)):
        jumps[l[i] - l[i-1] - 1] += 1
    return jumps

def part2():
    poss = [0] * len(l)
    poss[-1] = 1

    def recurse(idx):
        if poss[idx]:
            return poss[idx]
        if idx >= len(l):
            return 0
        start = l[idx]
        total = recurse(idx + 1)
        if (idx + 2) < len(l) and l[idx+2] - start <= 3:
            total += recurse(idx + 2)
            if (idx + 3) < len(l) and l[idx+3] - start <= 3:
                total += recurse(idx + 3)
        poss[idx] = total
        return total


    ans = recurse(0)
    return(ans)

if __name__ == "__main__":
    preprocess()
    jumps = part1()
    print(jumps[0] * jumps[2])
    print(part2())
