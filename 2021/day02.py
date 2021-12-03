def parse_input():
    with open('inputs/day02.txt', 'r') as f:
        tuples = [line.split() for line in f.readlines()]
    return [(direction, int(amount)) for direction, amount in tuples]

def p1():
    tuples = parse_input()
    distance = 0
    depth = 0
    for direction, amount in tuples:
        if direction == 'forward':
            distance += amount
        elif direction == 'down':
            depth += amount
        elif direction == 'up':
            depth -= amount

    return distance * depth

def p2():
    tuples = parse_input()
    distance = 0
    depth = 0
    aim = 0
    for direction, amount in tuples:
        if direction == 'forward':
            distance += amount
            depth += aim * amount
        elif direction == 'down':
            aim += amount
        elif direction == 'up':
            aim -= amount

    return distance * depth

if __name__ == "__main__":
    print(p2())
