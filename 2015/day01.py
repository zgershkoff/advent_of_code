# 2015 day1

inFile = "d01.txt"

def c1():
    ans = 0
    with open(inFile, 'r') as f:
        for line in f.readlines():
            for c in line:
                if c == '(':
                    ans += 1
                elif c == ')':
                    ans -= 1
                # there shouldn't be other characters, except for \n
    return ans

def c2():
    ans = 0
    counter = 0
    with open(inFile, 'r') as f:
        for line in f.readlines():
            for c in line:
                if c == '(':
                    ans += 1
                elif c == ')':
                    ans -= 1

                counter += 1
                if ans == -1:
                    return counter

if __name__ == "__main__":
    print(c2())

