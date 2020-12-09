# day 9, 2020

inFile = "d09.txt"
nums = []

def preprocess():
    with open(inFile, 'r') as f:
        nums.extend([int(line) for line in f.readlines()])

def check_if_sum(last25, cur):
    # brute force is viable but let's try to do better
    last25.sort()
    for i, num1 in enumerate(last25):
        if num1 > cur:
            break
        for num2 in last25[i+1:]:
            if num1 + num2 == cur:
                return True
            elif num1 + num2 > cur:
                break
    return False
    # still O(n^2) but better nonetheless

def part1():
    for i in range(len(nums)):
        if not check_if_sum(nums[i:25+i], nums[25+i]):
            return nums[25+i]

def part2(soln):
    # I'm definitely brute forcing this
    for i in range(len(nums)):
        j = i + 1
        while sum(nums[i:j]) < soln:
            j += 1
            if sum(nums[i:j]) == soln:
                return max(nums[i:j]) + min(nums[i:j])

if __name__ == "__main__":
    preprocess()
    print(part1())
    soln = part1()
    print(part2(soln))
