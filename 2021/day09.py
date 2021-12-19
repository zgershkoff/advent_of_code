class Vents():
    def __init__(self, filename='inputs/day09.txt'):
        self.grid = []
        with open(filename, 'r') as f:
            for line in f.readlines():
                self.grid.append([int(n) for n in line.strip()])

    def get_neighbor_indices(self, i, j):
        neighbors = []
        if i != 0:
            neighbors.append((i-1, j))
        if i != len(self.grid) - 1:
            neighbors.append((i+1, j))
        if j != 0:
            neighbors.append((i, j-1))
        if j != len(self.grid[0]) - 1:
            neighbors.append((i, j+1))
        return neighbors

    def check_if_low(self, i, j):
        neighbors = self.get_neighbor_indices(i, j)
        return all(self.grid[i][j] < self.grid[a][b] for a, b in neighbors)

    def get_low_points_score(self):
        total = 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.check_if_low(i, j):
                    total += 1 + self.grid[i][j]
        return total

    def union_find(self):
        roots = {(i, j): (i, j) for i in range(len(self.grid))
                 for j in range(len(self.grid[0]))}
        parts = {(i, j): [(i, j)] for i in range(len(self.grid))
                 for j in range(len(self.grid[0]))}

        def check_for_9(i, j):
            # print(i, j, (i, j) in roots)
            # print(roots[(i, j)])
            if (i, j) not in roots:
                return True
            if self.grid[i][j] == 9:
                del roots[(i, j)]
                del parts[(i, j)]
                return True
            return False

        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if check_for_9(i, j):
                    continue
                for a, b in self.get_neighbor_indices(i, j):
                    if not check_for_9(a, b):
                        if roots[(a, b)] != roots[(i, j)] and self.grid[i][j] < self.grid[a][b]:
                            old_root = roots[(a, b)]
                            for c, d in parts[roots[(a, b)]]:
                                roots[(c, d)] = roots[(i, j)]
                            parts[roots[(i, j)]].extend(parts[old_root])
                            del parts[old_root]

        # print(parts.values())
        basins = list(parts.values())
        basins.sort(key=len, reverse=True)
        return len(basins[0]) * len(basins[1]) * len(basins[2])



if __name__ == "__main__":
    V = Vents('inputs/day09.txt')
    print(V.get_low_points_score())
    # returns 575
    print(V.union_find())
