# day 15, 2020

start = [15,12,0,14,3,1]
# keep a dictionary {number: last index seen}
d = {}
iters = 30000000

def preprocess():
    for i, num in enumerate(start[:-1]):
        d[num] = i + 1

def part1():
    on_deck = start[-1]

    for i in range(len(d), iters - 1):
        # -1 because the last value is not committed into d
        i += 1
        if on_deck not in d:
            new_val = 0
        else:
            new_val = i - d[on_deck]
        d[on_deck] = i
        on_deck = new_val

    return on_deck

if __name__ == "__main__":
    preprocess()
    print(part1())
