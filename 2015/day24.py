# year 2015 day 24

from copy import copy

inFile = 'd24.txt'
num_groups = 4

class d24():
    def __init__(self):
        self.soln = []
        self.best = float('inf')
        self.target = 0

    def preprocess(self):
        l = []
        with open(inFile, 'r') as f:
            for line in f.readlines():
                l.append(int(line))
        l.reverse()

        self.soln = l
        self.target = sum(l) // num_groups
        self.brute_recursion(l)
        return self.best

    def prod(self, l):
        ans = 1
        for e in l:
            ans *= e
        return ans

    def brute_recursion(self, l, sofar=[], idx = 0):
        if len(sofar) > len(self.soln):
            return
        if sum(sofar) == self.target:
            if len(sofar) < len(self.soln) or self.prod(sofar) < self.best:
                self.soln = sofar
                self.best = self.prod(sofar)
        if sum(sofar) >= self.target:
            return

        new_sofar = copy(sofar)
        while idx < len(l):
            new_sofar.append(l[idx])
            self.brute_recursion(l, new_sofar, idx + 1)
            idx += 1
            new_sofar.pop()

if __name__ == "__main__":
    solver = d24()
    print(solver.preprocess())
