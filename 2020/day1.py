# advent of code, day 1, challenges 1 and 2

inFile = "c1.txt"
target = 2020

def c1():
    winners = set()
    with open(inFile, 'r') as f:
        for line in f.readlines():
            item = int(line.strip())
            complement = target - item
            if item in winners:
                return item * complement
            else:
                winners.add(complement)

def c2():
    items = []
    with open(inFile, 'r') as f:
        for line in f.readlines():
            item = int(line.strip())
            items.append(item)
    items.sort() # put items increasing order so we can break
    item_set = set(items) # for faster lookup

    for i, item1 in enumerate(items):
        for item2 in items[i+1:]:
            remaining = target - (item1 + item2)
            if remaining in item_set:
                return (item1 * item2 * remaining)
            if remaining <= 0:
                break


if __name__ == "__main__":
    print(c2())
