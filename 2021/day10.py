class Brackets():
    def __init__(self, filename='inputs/day10.txt'):
        self.strings = []
        with open(filename, 'r') as f:
            for line in f.readlines():
                self.strings.append(line.strip())

        self.ends = {')': '(', ']': '[', '}': '{', '>': '<'}
        self.scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
        self.inc_scores = {'(': 1, '[': 2, '{': 3, '<': 4}
        # using open symbols here

    def score_corrupted(self):
        score = 0
        for string in self.strings:
            open_symbols = []
            for c in string:
                if c in '([{<':
                    open_symbols.append(c)
                elif c in ')]}>':
                    last_open = open_symbols.pop()
                    if self.ends[c] != last_open:
                        score += self.scores[c]
                        break
        return score

    def score_incomplete(self):
        scores = []
        for string in self.strings:
            open_symbols = []
            for c in string:
                if c in '([{<':
                    open_symbols.append(c)
                elif c in ')]}>':
                    last_open = open_symbols.pop()
                    if self.ends[c] != last_open:
                        break
            else:
                this_score = 0
                for c in open_symbols[::-1]:
                    this_score *= 5
                    this_score += self.inc_scores[c]
                scores.append(this_score)
        return sorted(scores)[len(scores)//2]

if __name__ == "__main__":
    B = Brackets()
    print(B.score_corrupted())
    # returns 311949
    print(B.score_incomplete())

