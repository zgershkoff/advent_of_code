# 2020 day 3

inFile = "d3.txt"

def c1():
    # by inspection, there are 31 columns
    cols = 31
    idx = 0
    count = 0

    with open(inFile, 'r') as f:
        for line in f.readlines():
            line = line.strip()

            if line[idx] == "#":
                count += 1
            idx = (idx + 3) % 31

    return count

def tree_counter(right_inc, down_inc):
    # by inspection, there are 31 columns
    cols = 31
    vertical_idx = 0
    idx = 0
    count = 0

    with open(inFile, 'r') as f:
        for line in f.readlines():
            line = line.strip()

            if vertical_idx == 0:
                if line[idx] == "#":
                    count += 1
                idx = (idx + right_inc) % 31
            vertical_idx = (vertical_idx + 1) % down_inc

    return count

def c2():
    ans = 1
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    for right_inc, down_inc in slopes:
        ans *= tree_counter(right_inc, down_inc)
    return ans

if __name__ == "__main__":
    print(c2())




