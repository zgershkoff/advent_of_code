# day 16, 2015

inFile = "d16.txt"

dna = {"children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3,
       "akitas": 0, "vizslas": 0, "goldfish": 5, "trees": 3,
       "cars": 2, "perfumes": 1}

def sue_finder():
    sues = [] # indices are offset by 1
    with open(inFile, 'r') as f:
        for line in f.readlines():
            d = {}
            parts = line.strip().split()
            for i in range(1, 4):
                i *= 2
                key = parts[i].strip(":")
                value = int(parts[i+1].strip(","))
                d[key] = value
            sues.append(d)
    part_1(sues)
    part_2(sues)

def part_1(sues):
    for i, d in enumerate(sues):
        if all(d[thing] == dna[thing] for thing in d):
            print(i+1)

def part_2(sues):
    for i, d in enumerate(sues):
        for thing in d:
            if thing == "cats" or thing == "trees":
                if d[thing] <= dna[thing]:
                    break
            elif thing == "pomeranians" or thing == "goldfish":
                if d[thing] >= dna[thing]:
                    break
            else:
                if d[thing] != dna[thing]:
                    break
        else: # behold the rare for/else flow pattern
            print(i+1)


if __name__ == "__main__":
    sue_finder()
