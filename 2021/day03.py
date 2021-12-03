"""
Postmortem: For problem 1, I chose to do all the counts of zeroes and
ones first, and then calculated gamma and epsilon. An alternative would
have been to count the zeroes and ones one place at a time, modifying
gamma and epsilon with each step. There's no clear advantage to that
alternative method for problem 1, but for problem 2, that's the correct
way to do it, since the counts change with each iteration. As it is now,
there are some extra calculations done that I would refactor out if it
mattered.
"""

def parse_input():
    with open('inputs/day03.txt', 'r') as f:
        return [line.strip() for line in f.readlines()]

def p1():
    strings = parse_input()
    xormask = 2**len(strings[0]) - 1
    zeroes = [0 for _ in range(len(strings[0]))]
    ones = [0 for _ in range(len(strings[0]))]

    for string in strings:
        for i, digit in enumerate(string):
            if digit == "0":
                zeroes[i] += 1
            elif digit == "1":
                ones[i] += 1

    gamma = 0
    for i in range(len(zeroes)):
        gamma = gamma << 1
        if ones[i] > zeroes[i]:
            gamma += 1

    epsilon = gamma ^ xormask

    return gamma * epsilon

def count_bits(strings):
    zeroes = [0 for _ in range(len(strings[0]))]
    ones = [0 for _ in range(len(strings[0]))]

    for string in strings:
        for i, digit in enumerate(string):
            if digit == "0":
                zeroes[i] += 1
            elif digit == "1":
                ones[i] += 1

    return zeroes, ones


def p2():
    strings = parse_input()
    xormask = 2**len(strings[0]) - 1
    # these lists are unnessary here
    # rework to only count ith bit
    zeroes, ones = count_bits(strings)

    def air_search(strings, zeroes, ones, least=False):
        least = int(least)
        length = len(zeroes)
        for i in range(length):
            print("zero", zeroes)
            print("ones", ones)
            sublist = []
            if zeroes[i] > ones[i]:
                search_bit = 0
            elif zeroes[i] <= ones[i]:
                search_bit = 1
            search_bit = str(search_bit ^ least)
            for string in strings:
                if string[i] == search_bit:
                    sublist.append(string)
            if len(sublist) == 1:
                return sublist[0]
            strings = sublist
            zeroes, ones = count_bits(strings)
            print(i, strings)


    o2 = air_search(strings, zeroes, ones)
    co2 = air_search(strings, zeroes, ones, True)
    print(o2, co2)
    return int(o2, 2) * int(co2, 2)

if __name__ == "__main__":
    print(p2())
