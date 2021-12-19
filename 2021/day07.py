class CrabAligner():
    def __init__(self, filename='inputs/day07.txt'):
        with open(filename, 'r') as f:
            lines = f.readlines()
            self.crab_list = [int(n) for n in lines[0].strip().split(',')]
            self.crab_list.sort()

    def calculate_score(self, idx):
        return sum([abs(position - idx) for position in self.crab_list])

    def check_guess(self, idx):
        # just don't call this on the ends
        left_score = self.calculate_score(idx-1)
        middle_score = self.calculate_score(idx)
        right_score = self.calculate_score(idx+1)
        # print(left_score, middle_score, right_score)
        if left_score < middle_score:
            return -1
        elif right_score < middle_score:
            return 1
        else:
            return 0

    def bisect(self):
        left_end = self.crab_list[0]
        right_end = self.crab_list[-1]
        while True:
            # print(left_end, right_end)
            guess = (left_end + right_end) // 2
            result = self.check_guess(guess)
            if result == -1:
                right_end = guess
            elif result == 1:
                left_end = guess + 1
            else:
                return self.calculate_score(guess)

    def check_score_part2(self, idx):
        return sum([self.gauss(abs(position - idx)) for position in self.crab_list])

    def gauss(self, n):
        return n * (n + 1) // 2

    def linear_scan(self):
        left_end = self.crab_list[0]
        right_end = self.crab_list[-1]
        best = float('inf')
        for n in range(left_end, right_end + 1):
            best = min(best, self.check_score_part2(n))
        return best


if __name__ == "__main__":
    C = CrabAligner(filename='inputs/day07.txt')
    print(C.bisect())
    # returns 323
    print(C.linear_scan())
