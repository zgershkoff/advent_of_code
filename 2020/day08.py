# day 8, 2020

from copy import copy

inFile = "d08.txt"

instr_list = [] # (inst, value)

def nop(amt, head, acc_state):
    return jmp(1, head, acc_state)

def jmp(amt, head, acc_state):
    head += amt
    return head, acc_state

def acc(amt, head, acc_state):
    acc_state += amt
    return jmp(1, head, acc_state)

d = {"nop": nop, "jmp": jmp, "acc": acc}

def preprocess():
    with open(inFile, 'r') as f:
        for line in f.readlines():
            inst, amt = line.strip().split()
            instr_list.append((inst, int(amt)))

def part1(seen = set(), head = 0, acc_state = 0):
    while head < len(instr_list):
        inst, amt = instr_list[head]
        if head in seen:
            return (acc_state, False)
        seen.add(head)
        head, acc_state = d[inst](amt, head, acc_state)
    return (acc_state, True)

def part2():
    seen = set()
    acc_state = 0
    head = 0
    prev = 0

    # just try changing every nop or jmp as it comes
    while True:
        inst, amt = instr_list[head]
        if inst in ["jmp", "nop"]:
            if inst == "jmp":
                inst2 = "nop"
            elif inst == "nop":
                inst2 = "jmp"
            instr_list[head] = (inst2, amt)
            ans, solved = part1(copy(seen), head, acc_state)
            if solved:
                return ans
            instr_list[head] = (inst, amt)
        seen.add(head)
        head, acc_state = d[inst](amt, head, acc_state)

if __name__ == "__main__":
    preprocess()
    print(part1())
    print(part2())
