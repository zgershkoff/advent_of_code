# day 12, 2020

inFile = "d12.txt"

inst = [] # (instruction type, amount)
directions = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}
#             N          E          S           W
dir_to_int = {"N": 0, "E": 1, "S": 2, "W": 3}
mults = {"R": 1, "L": -1}

def preprocess():
    with open(inFile, 'r') as f:
        inst.extend([(line[0], int(line[1:].strip())) \
                     for line in f.readlines()])

def part1():
    coords = [0, 0]
    cur = 1 # starts facing east

    for inst_type, amt in inst:
        if inst_type in "NESW":
            t = directions[dir_to_int[inst_type]]
            move = [coord * amt for coord in t]
            for i in range(len(move)):
                coords[i] += move[i]
        elif inst_type in "RL":
            rotation = mults[inst_type] * (amt // 90)
            cur = (cur + rotation) % 4
        elif inst_type == "F":
            t = directions[cur]
            move = [coord * amt for coord in t]
            for i in range(len(move)):
                coords[i] += move[i]

    return sum(abs(coord) for coord in coords)

def part2():
    coords = [0, 0]
    wp_coords = [10, 1] # 10 east, 1 north
    # inst = [("F", 10), ("N", 3), ("F", 7), ("R", 90), ("F", 11)]

    for inst_type, amt in inst:
        if inst_type in "NESW":
            t = directions[dir_to_int[inst_type]]
            move = [coord * amt for coord in t]
            for i in range(len(move)):
                wp_coords[i] += move[i]
        elif inst_type in "RL":
            rotation = (mults[inst_type] * (amt // 90)) % 4
            if rotation == 1:
                wp_coords[0], wp_coords[1] = wp_coords[1], -wp_coords[0]
            elif rotation == 2:
                wp_coords[0], wp_coords[1] = -wp_coords[0], -wp_coords[1]
            elif rotation == 3:
                wp_coords[0], wp_coords[1] = -wp_coords[1], wp_coords[0]
        elif inst_type == "F":
            for i in range(len(wp_coords)):
                coords[i] += amt * wp_coords[i]

    return sum(abs(coord) for coord in coords)

if __name__ == "__main__":
    preprocess()
    print(part1())
    print(part2())
