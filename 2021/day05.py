class Hydrothermal():
    def __init__(self, file='inputs/day05.txt'):
        with open(file, 'r') as f:
            lines = f.readlines()
            self.pairs = []
            for line in lines:
                start_string, end_string = line.strip().split(' -> ')
                start = [int(n) for n in start_string.split(',')]
                end = [int(n) for n in end_string.split(',')]
                if start == end:
                    print(start)
                    print('line of length 1')
                    exit()
                self.pairs.append(tuple(sorted([start, end])))
        self.grid = [[0 for _ in range(1000)] for _ in range(1000)]

    def vent_horizontal(self):
        for start, end in self.pairs:
            if start[1] == end[1]:
                value = start[1]
                for i in range(start[0], end[0] + 1):
                    self.grid[i][value] += 1

    def vent_vertical(self):
        for start, end in self.pairs:
            if start[0] == end[0]:
                value = start[0]
                for i in range(start[1], end[1] + 1):
                    self.grid[value][i] += 1

    def count_multiples(self):
        total = 0
        for row in self.grid:
            for item in row:
                if item >= 2:
                    total += 1
        return total

    def problem_1(self):
        self.vent_horizontal()
        self.vent_vertical()
        return self.count_multiples()

    def vent_diagonal(self):
        for start, end in self.pairs:
            if start[0] != end[0] and start[1] != end[1]:
                dif = end[0] - start[0] + 1
                xcoord = start[0]
                ycoord = start[1]
                for i in range(dif):
                    self.grid[xcoord][ycoord] += 1
                    xcoord += 1
                    if start[1] < end[1]:
                        ycoord += 1
                    else:
                        ycoord -= 1

    def problem_2(self):
        self.vent_horizontal()
        self.vent_vertical()
        self.vent_diagonal()
        return self.count_multiples()


if __name__ == "__main__":
    H = Hydrothermal()
    print(H.problem_2())
