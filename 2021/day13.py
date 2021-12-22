class OrigamiDots():
    def __init__(self, filename='inputs/day13.txt'):
        self.coords = set()
        self.folds = []
        with open(filename, 'r') as f:
            for line in f:
                if not line.strip():
                    break
                x, y = [int(n) for n in line.strip().split(',')]
                self.coords.add((x, y))
            # f should be an iterator of lines. Picking up where it left off
            # after the blank line:
            for line in f:
                _, _, equation = line.strip().split()
                direction, value = equation.split('=')
                self.folds.append((direction, int(value)))

    def one_fold(self, direction, value):
        dirs = {'x': 0, 'y': 1}
        active_dir = dirs[direction]
        new_coords = set()
        for pair in self.coords:
            if pair[active_dir] < value:
                new_coords.add(pair)
            else:
                new_pair = [0, 0]
                new_pair[active_dir ^ 1] = pair[active_dir ^ 1]
                new_pair[active_dir] = 2 * value - pair[active_dir]
                new_coords.add(tuple(new_pair))
        self.coords = new_coords

    def p1(self):
        first_dir, first_value = self.folds[0]
        self.one_fold(first_dir, first_value)
        return len(self.coords)

    def coords_to_grid(self):
        num_rows = max(x for x, y in self.coords) + 1
        num_cols = max(y for x, y in self.coords) + 1
        # doing the transpose by switching rows and cols
        grid = [['.' for _ in range(num_rows)] for _ in range(num_cols)]
        for x, y in self.coords:
            grid[y][x] = '#'
        for row in grid:
            print("".join(row))

    def p2(self):
        for direction, value in self.folds:
            self.one_fold(direction, value)
        self.coords_to_grid()

if __name__ == "__main__":
    OD = OrigamiDots()
    print(OD.p2())





