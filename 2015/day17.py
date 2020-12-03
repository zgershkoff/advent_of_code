# day 17, year 2015

from copy import copy

inFile = "d17.txt"

def preprocess():
    data = []
    with open(inFile, 'r') as f:
        for line in f.readlines():
            data.append(int(line))
    data.sort()
    return data

class d17():
    def __init__(self, data):
        self.data = data
        self.count = 0
        self.target = 150

        # for part 2
        self.min_len = float('inf')

    def recursion_helper(self, sofar = [], idx = 0):
        new_sofar = copy(sofar)
        while idx < len(self.data):
            new_sofar.append(self.data[idx])
            if sum(new_sofar) >= self.target:
                if sum(new_sofar) == self.target:
                    # this logic is for part 2
                    # remove these two if statements for part 1
                    if len(new_sofar) > self.min_len:
                        continue
                    if len(new_sofar) < self.min_len:
                        self.count = 0
                        self.min_len = len(new_sofar)
                    self.count += 1
                else:
                    break
            idx += 1
            self.recursion_helper(new_sofar, idx)
            new_sofar.pop()

    def solve(self):
        self.recursion_helper()
        return self.count

if __name__ == "__main__":
    data = preprocess()
    solver = d17(data)
    print(solver.solve())
