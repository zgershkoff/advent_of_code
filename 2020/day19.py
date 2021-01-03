# day 19, 2020

# make a dictionary where the keys are lists of pairs OR "a" or "b"
# then make a set of allowed strings
# check if the input strings are in the set

from copy import copy

inFile = "d19.txt"

d = {}
strings = []

def preprocess():
    with open(inFile, 'r') as f:
        reader = f.readlines()
        rules_end = reader.index('\n')
        for line in reader[:rules_end]:
            line = line.strip()
            key, rules_string = line.split(":")
            key = int(key)
            # check if the rule is a single character
            for c in "ab":
                if c in rules_string:
                    d[key] = c
                    break
            else:
                rules = rules_string.split("|")
                rules_list = []
                for l in rules:
                    l = l.strip().rstrip()
                    rules_list.append([int(r) for r in l.split()])
                d[key] = rules_list

        strings.extend([s.strip() for s in reader[rules_end + 1:]])

def build_allowed_strings():

    def helper(key):
        # return type: list of strings
        rules = d[key]
        if type(rules) == str:
            return [rules]

        suffixes = []
        for l in rules:
            parts = [""]
            for new_key in l:
                end_suffixes = helper(new_key)
                parts = combine_strings_lists(parts, end_suffixes)
            suffixes.extend(parts)
        return suffixes

    allowed = set(helper(0))
    return allowed

def combine_strings_lists(first, last):
    ans = []
    for f in first:
        for l in last:
            ans.append(f + l)
    return ans

def part1():
    allowed = build_allowed_strings()
    return sum(1 for s in strings if s in allowed)

def part2():
    allowed = build_allowed2()
    return sum(1 for s in strings if s in allowed)

if __name__ == "__main__":
    preprocess()
    print(part1())
    print(max(len(s) for s in strings))
