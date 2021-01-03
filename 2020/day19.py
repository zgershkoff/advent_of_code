# day 19, 2020

# make a dictionary where the keys are lists of pairs OR "a" or "b"
# then make a set of allowed strings
# check if the input strings are in the set

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
    # from collections import Counter
    # print(Counter([len(a) for a in allowed]))
    # print(Counter([len(s) for s in strings]))
    # all the allowed strings have length 24,
    # but the given strings have lengths multiples of 8
    return sum(1 for s in strings if s in allowed)

def build_allowed2():
    # idea for part 2:
    # make a memo of the suffixes for every rule except those that use 8 and 11
    # then look at the ways 8 and 11 can repeat
    # originally nothing used 8 and 11 except 0
    global d
    d[8].append([42, 8])
    d[11].append([42, 11, 31])

    memo = {}

    def helper(key, depth = 0):
        nonlocal memo
        # return type: list of strings

        if depth == 11:
            return []

        rules = d[key]
        if type(rules) == str:
            return [rules]

        suffixes = []
        for l in rules:
            parts = [""]
            for new_key in l:
                if new_key in memo:
                    end_suffixes = memo[new_key]
                else:
                    end_suffixes = helper(new_key, depth + 1)
                    memo[new_key] = end_suffixes
                parts = combine_strings_lists(parts, end_suffixes)
            suffixes.extend(parts)
        return set([suf for suf in suffixes if len(suf) <= 96])

    memo[42] = helper(42)
    memo[31] = helper(31)

    # building a set of allowed strings seems unfeasible
    return memo

def part2():
    # this time we're iterating through the given strings
    # the crucial obseration it that 0 is 8 11, and 8 11 breaks down
    # to 42 42 ... 31 where the ... is a sequence of 42s then 31s
    # must be 1 more 42 at least
    memo = build_allowed2()
    temp = list(memo[42])
    length = len(temp[0])
    fortytwo = memo[42]
    thirtyone = memo[31]

    count = 0

    for s in strings:
        start = 0
        end = length
        good = True
        num_42s = 0
        num_31s = 0
        # this could be condensed a little but I'm fine with it
        while end <= len(s) - length:
            if s[start:end] in fortytwo:
                num_42s += 1
            else:
                break
            start += length
            end += length

        if num_42s < 2:
            continue

        while end <= len(s):
            if s[start:end] in thirtyone:
                num_31s += 1
            else:
                good = False
                break
            start += length
            end += length

        if good and num_42s > num_31s:
            count += 1

    return count




if __name__ == "__main__":
    preprocess()
    print(part1())
    print(len(strings))
    print(max(len(s) for s in strings))
    print(part2())
