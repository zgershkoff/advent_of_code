# day 8, 2015

inFile = "d8.txt"

def count(s):
    loss = 2
    i = 0
    while i < len(s):
        if s[i] == "\\":
            loss += 1
            i += 1
            if s[i] == "x":
                loss += 2
                i += 2
        i += 1
    return loss

def count2(s):
    gain = 2
    for c in s:
        if c == '\"' or c == "\\":
            gain += 1
    return gain

def read():
    total = 0
    with open(inFile, 'r') as f:
        for line in f.readlines():
            total += count2(line)
    return total

if __name__ == "__main__":
    print(read())
