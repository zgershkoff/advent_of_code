class DumboOctopi():
    def __init__(self, filename='inputs/day11.txt'):
        self.grid = []
        with open(filename, 'r') as f:
            for line in f.readlines():
                self.grid.append([int(n) for n in line.strip()])

        self.spent = [[False for _ in range(len(self.grid[0]))]
                      for _ in range(len(self.grid))]

    def get_neighbor_indices(self, i, j):
        return [(a, b) for a in range(i-1, i+2) for b in range(j-1, j+2)
                if 0 <= a < len(self.grid) and 0 <= b < len(self.grid[0])
                and (a, b) != (i, j)]

    def simulate_step(self):
        '''Modifies grid by side effects. Returns number of flashes'''
        flashes = 0
        # first increment everything by 1
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                self.grid[i][j] += 1

        # then scan the entire grid for things over 9
        # and increment their neighbors
        scan_again = True
        while scan_again:
            scan_again = False
            for i in range(len(self.grid)):
                for j in range(len(self.grid[0])):
                    if self.grid[i][j] > 9 and not self.spent[i][j]:
                        self.spent[i][j] = True
                        scan_again = True
                        flashes += 1
                        for a, b in self.get_neighbor_indices(i, j):
                            self.grid[a][b] += 1

        # reset grid to within parameters
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] > 9:
                    self.grid[i][j] = 0
                    self.spent[i][j] = False

        return flashes

    def part1(self):
        flashes = 0
        for _ in range(100):
            flashes += self.simulate_step()

        return flashes

    def part2(self):
        grid_entries = set(n for l in self.grid for n in l)
        counter = 0
        while grid_entries != set([0]):
            counter += 1
            self.simulate_step()
            grid_entries = set(n for l in self.grid for n in l)
        return counter



if __name__ == "__main__":
    do = DumboOctopi('inputs/day11.txt')
    # print(do.part1())
    # grid = do.grid
    # for line in grid:
    #     print("".join([str(n) for n in line]))
    # gives 1691
    print(do.part2())
