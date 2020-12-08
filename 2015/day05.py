# 2015 day 5

from collections import Counter

inFile = "d05.txt"

vowels = "aeiou"
bad = {"a": "b", "c": "d", "p": "q", "x": "y"}

def rules_check1(s):
    C = Counter(s)
    check1 = sum(C[vowel] for vowel in vowels) >= 3
    check2 = False
    check3 = True
    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            check2 = True
        if s[i] in bad and s[i+1] == bad[s[i]]:
            check3 = False
    return check1 and check2 and check3

def rules_check2(s):
    check1 = False
    pairs = set([s[0:2]])
    for i in range(1, len(s) - 1):
        substr = s[i:i+2]
        if substr != s[i-1:i+1]:
            if substr in pairs:
                check1 = True
            else:
                pairs.add(substr)

    check2 = False
    for i in range(len(s) - 2):
        if s[i] == s[i+2]:
            check2 = True
    return check1 and check2

def c1():
    total = 0
    with open(inFile, 'r') as f:
        for line in f.readlines():
            total += rules_check2(line.strip())
    return total

if __name__ == "__main__":
    print(c1())
