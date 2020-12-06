# day 7, 2015

# This is part 1. To do part 2, I swapped out a value in the data file.

# never dealt with this before, but there are 339 wires
# and 339 lines of data. So every wire gets assigned
# to exactly once.

# So there's a digraph here but the data isn't given in order.
# I will iterate through the list of unresolvable assignments,
# just pop and push them back into a deque until they're all
# resolved.

from collections import deque

inFile = "d7.txt"


def not_wire(l):
    in1 = l[0]
    return in1 ^ 65335

def or_wire(l):
    in1, in2 = l
    return in1 | in2

def and_wire(l):
    in1, in2 = l
    return in1 & in2

def lshift_wire(l):
    in1, amount = l
    return in1 << amount

def rshift_wire(l):
    in1, amount = l
    return in1 >> amount

def is_wire(l):
    in1 = l[0]
    return in1

opers = {"NOT": not_wire, "OR": or_wire, "AND": and_wire,
         "LSHIFT": lshift_wire, "RSHIFT": rshift_wire, "IS": is_wire}
wires = {}
unresolved = deque() # [instruction, input(s), output]


def preprocess():
    with open(inFile, 'r') as f:
        for line in f.readlines():
            parts = line.strip().split()
            if len(parts) == 3: # eg "a -> b"
                unresolved.append(["IS", [parts[0]], parts[2]])
            elif len(parts) == 4: # eg "NOT a -> b"
                unresolved.append([parts[0], [parts[1]], parts[3]])
            else: # eg "a OPERATOR b -> c"
                unresolved.append(
                    [parts[1], [parts[0], parts[2]], parts[4]])

    return turn_on()

def turn_on():
    while unresolved:
        line = unresolved.popleft()
        oper, in_wires, out_wire = line
        check = lambda w: (w in wires) or (w.isnumeric())
        if all(check(w) for w in in_wires):
            input_list = []
            for i in range(len(in_wires)):
                if in_wires[i].isnumeric():
                    input_list.append(int(in_wires[i]))
                else:
                    input_list.append(wires[in_wires[i]])
            wires[out_wire] = opers[oper](input_list)
        else:
            unresolved.append(line)

    return wires["a"]

if __name__ == "__main__":
    print(preprocess())
