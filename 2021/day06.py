from collections import Counter, deque

def preprocess(filename='inputs/day06.txt'):
    with open(filename, 'r') as f:
        lines = f.readlines()
        line = lines[0].strip()
        fish = [int(n) for n in line.split(',')]
        C = Counter(fish)
        fish_deque = deque([0] * 9)
        for age in C:
            fish_deque[age] += C[age]
        return fish_deque

def thing_doer(days):
    fish_deque = preprocess()
    for _ in range(days):
        birthing = fish_deque.popleft()
        fish_deque.append(birthing)
        fish_deque[6] += birthing
    return sum(fish_deque)

def p1():
    return thing_doer(80)

def p2():
    return thing_doer(256)

if __name__ == "__main__":
    print(p1())
