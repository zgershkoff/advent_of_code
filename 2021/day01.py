from collections import deque

def p1():
    with open('inputs/day01.txt', 'r') as f:
        nums = [int(item) for item in f.readlines()]

    prev = 99999
    count = 0

    for num in nums:
        if num > prev:
            count += 1
        prev = num

    return count

def p2():
    with open('inputs/day01.txt', 'r') as f:
        nums = [int(item) for item in f.readlines()]

    count = -3
    sums = deque([0, 0, 0])

    for num in nums:
        complete_sum = sums.popleft()
        sums.append(0)
        sums = deque([partial + num for partial in sums])
        if sums[0] > complete_sum:
            count += 1

    return count

if __name__ == "__main__":
    print(p1())
    print(p2())
