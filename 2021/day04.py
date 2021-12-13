class Bingo():
    def __init__(self, file='inputs/day04.txt'):
        with open(file, 'r') as f:
            lines = f.readlines()
            self.numbers = [int(n) for n in lines[0].strip().split(',')]
            self.cards = []
            card = []
            for line in lines[1:]:
                line = line.strip()
                if not line:
                    card = []
                else:
                    row = [int(n) for n in line.split()]
                    card.append(row)
                    if len(card) == 5:
                        self.cards.append(card)

            # no way to get bingo in 4 numbers, so treat the first 4 as called
            self.called_index = 4
            self.called_set = set(self.numbers[0:4])

    def has_won(self, card):
        won_on_rows = any(set(row).issubset(self.called_set) for row in card)
        col_sets = [set(card[i][j] for i in range(5)) for j in range(5)]
        # for i, c in enumerate(col_sets):
        #     print(i, c)
        won_on_cols = any(col.issubset(self.called_set) for col in col_sets)
        return won_on_rows or won_on_cols

    def calculate_score(self, card):
        total = 0
        for row in card:
            for num in row:
                if num not in self.called_set:
                    total += num
        return total * self.numbers[self.called_index]

    def play_bingo(self):
        while True:
            self.called_set.add(self.numbers[self.called_index])
            for card in self.cards:
                if self.has_won(card):
                    return self.calculate_score(card)
            self.called_index += 1

    def play_to_lose(self):
        card_indices = set(range(len(self.cards)))
        while card_indices:
            self.called_set.add(self.numbers[self.called_index])
            for idx in list(card_indices):
                if self.has_won(self.cards[idx]):
                    card_indices.remove(idx)
                    score = self.calculate_score(self.cards[idx])
            self.called_index += 1
        return score



if __name__ == "__main__":
    Machine = Bingo()#'inputs/day04test.txt')
    print(Machine.play_to_lose())
