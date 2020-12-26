# advent of code 2020, day 18
# looks like every number is one-digit

inFile = "d18.txt"

expressions = []

mult = lambda a, b: a * b
plus = lambda a, b: a + b
ops = {"+": plus, "*": mult}

def preprocess():
    with open(inFile, 'r') as f:
        for line in f.readlines():
            exp = []
            for c in line.strip():
                if c.isnumeric():
                    exp.append(int(c))
                elif c == " ":
                    continue
                else:
                    exp.append(c)
            expressions.append(exp)

def find_close_paren(exp):
    opens = 0
    for i, c in enumerate(exp):
        if c == "(":
            opens += 1
        elif c == ")":
            opens -= 1
        if opens == 0:
            return i

def do_line1(exp):
    running = 0
    cur_operation = plus
    idx = 0
    while idx < len(exp):
        if type(exp[idx]) == int:
            running = cur_operation(running, exp[idx])
        elif exp[idx] in "+*":
            cur_operation = ops[exp[idx]]
        elif exp[idx] == "(":
            close_idx = find_close_paren(exp[idx:]) + idx
            running = cur_operation(running, do_line1(exp[idx+1: close_idx]))
            idx = close_idx
        idx += 1

    return running

def part1():
    return sum(do_line1(exp) for exp in expressions)

def do_line2(exp):
    # idea: make two passes
    # first pass for addition and parens
    # then do the remaining multiplying
    adding_now = False
    pass1 = []
    idx = 0

    while idx < len(exp):
        if type(exp[idx]) == int or exp[idx] == "(":
            if type(exp[idx]) == int:
                new_num = exp[idx]
            else:
                close_idx = find_close_paren(exp[idx:]) + idx
                new_num = do_line2(exp[idx+1: close_idx])
                idx = close_idx
            if adding_now:
                pass1[-1] += new_num
                adding_now = False
            else:
                pass1.append(new_num)
        elif exp[idx] == "+":
            adding_now = True
        idx += 1

    return prod(pass1)

def prod(l):
    ans = 1
    for n in l:
        ans *= n
    return ans

def part2():
    return sum(do_line2(exp) for exp in expressions)


if __name__ == "__main__":
    preprocess()
    print(part1())
    print(part2())
