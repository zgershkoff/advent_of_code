# day 7, 2020

inFile = "d7.txt"

from collections import defaultdict

# build a digraph
# g is a dictionary name: dictionary of in edges
# solve it by following all the in edges back
g = defaultdict(dict)

def preprocess():
    with open(inFile, 'r') as f:
        for line in f.readlines():
            parts = line.split()
            source = parts[0] + " " + parts[1]
            contains = parts[4:]
            for i in range(len(contains) // 4):
                i *= 4
                num = int(contains[i])
                destination = contains[i+1] + " " + contains[i+2]
                g[destination][source] = num

# for going backwards, the number of y bags that must be in x
# is irrelevant
def count_bags(goal = "shiny gold"):
    containers = set()
    stack = list(g[goal].keys())
    while stack:
        color = stack.pop()
        if color not in containers:
            containers.add(color)
            stack.extend(list(g[color].keys()))
    return len(containers)

# for part 2, we have to go the other way, so I change the preprocessing
# the only change is destination and source get swapped at the end of the loop
def preprocess2():
    with open(inFile, 'r') as f:
        for line in f.readlines():
            parts = line.split()
            source = parts[0] + " " + parts[1]
            contains = parts[4:]
            if len(contains) < 4: # eg. "no other bags."
                continue
            for i in range(len(contains) // 4):
                i *= 4
                num = int(contains[i])
                destination = contains[i+1] + " " + contains[i+2]
                g[source][destination] = num

def count_bags2(outer = "shiny gold"):
    # memoize to avoid redundant calculations
    contains = {}
    def count(bag):
        if bag in contains:
            return contains[bag]
        total = 0
        for content in g[bag]:
            total += g[bag][content] * (1 + count(content))
        contains[bag] = total
        return total

    total = count(outer)
    return total

if __name__ == "__main__":
    preprocess()
    print(count_bags())
