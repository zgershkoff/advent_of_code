# year 2015, day 14

inFile = "d14.txt"
time = 2503

def preprocess():
    data = []
    with open(inFile, 'r') as f:
        for line in f.readlines():
            nums = [int(n) for n in line.split() if n.isnumeric()]
            data.append(nums)
    return c2(data)

def c1(data):
    best = 0
    for l in data:
        period = l[1] + l[2]
        complete_cycles = time // period
        distance = l[0] * l[1] * complete_cycles
        time_left = min(l[1], time - (complete_cycles * period))
        distance += l[0] * time_left
        best = max(best, distance)
    return best

def c2(data):
    moving = lambda cur, l: cur < l[1]
    distances = [0] * len(data)
    scores = [0] * len(data)
    for t in range(time):
        for i, l in enumerate(data):
            period = l[1] + l[2]
            if t % period < l[1]:
                distances[i] += l[0]
        leader = max(range(len(distances)), key = distances.__getitem__)
        scores[leader] += 1
    return max(scores)



if __name__ == "__main__":
    print(preprocess())
