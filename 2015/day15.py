# day 15, 2020

# honestly I don't know the theory behind this. It feels like integer
# programming but not quite. I'll solve it with a greedy approach and
# read about it later.

sugar =     [ 3,  0,  0, -3,  2]
sprinkles = [-3,  3,  0,  0,  9]
candy =     [-1,  0,  4,  0,  1]
chocolate = [ 0,  0, -2,  2,  8]

vectors = [sugar, sprinkles, candy, chocolate]

# call these vectors w, x, y, z
# by inspection, the smallest scalars we can have in order to have a
# positive product of the first four columns sums is
# 2w + 1x + 2y + 3z

def my_prod(l):
    ans = 1
    for item in l:
        ans *= max(item, 0)
    return ans

def get_score(scalars, vectors = vectors):
    colsums = []
    for i in range(4):
        colsum = 0
        for j in range(len(scalars)):
            colsum += scalars[j] * vectors[j][i]
        colsums.append(colsum)
    # print(colsums)
    return my_prod(colsums)

def get_100_tsps(vectors, scalars = [2, 1, 3, 4]):

    def one_more_tsp():
        candidates = []
        for i in range(len(scalars)):
            scalars[i] += 1
            candidates.append(get_score(scalars, vectors))
            scalars[i] -= 1
        scalars[candidates.index(max(candidates))] += 1
        print(candidates, scalars)

    start = sum(scalars)
    counter = start
    for _ in range(start, 100):
        counter += 1
        print(counter)
        one_more_tsp()

    print(scalars)
    return get_score(scalars, vectors)

# this approach gives [21, 5, 32, 42], which is not even locally best
# what I will do instead is take [21, 5, 32, 42], which is positive
# but not locally best, and try to take steps to a locally best solution
# there should be a unique local maximum

from copy import copy

def move_to_max(scalars = [21, 5, 32, 42]):
    score = get_score(scalars)
    exit_loop = False
    for i in range(len(scalars)):
        for j in range(len(scalars)):
            if i == j:
                continue
            new_scalars = copy(scalars)
            new_scalars[i] -= 1
            new_scalars[j] += 1
            if get_score(new_scalars) > score:
                return move_to_max(new_scalars)

    return scalars

# That works for part 1. For part 2:
# maybe nonlinear programming is the way to go
"""
maximize a*b*c*d
subject to:
 3a - 3b -  c       > 0
      3b            > 0
           4c - 2d  > 0
-3a           + 2d  > 0
 2a + 9b +  c + 8d  = 500
"""
# I tried scipy and the solvers failed me. Below is an absolute brute
# force solution, which maybe I should have done for part 1.

cals = [2, 9, 1, 8]
def get_cals(v):
    a, b, c, d = v
    return 2*a + 9*b + 1*c + 8*d

def hack():
    best = 0
    for h in range(1, 100):
        print(h)
        for i in range(1, 100):
            for j in range(1, 100):
                for k in range(1, 100):
                    v = [h, i, j, k]
                    if sum(v) == 100 and get_cals(v) == 500:
                        best = max(best, get_score(v))
    return best


if __name__ == "__main__":
    # print(get_100_tsps(vectors))
    # print("")
    # print(get_score([16, 15, 44, 21], vectors))
    # print(get_score([21, 5, 32, 42], vectors))
    # print(get_score([22, 5, 31, 42], vectors))
    # print(get_score([21, 6, 31, 42], vectors))
    # print(get_score([21, 5, 31, 43], vectors))
    scalars = move_to_max()
    print(scalars)
    print(get_score(scalars))

    print(get_score([28, 15, 21, 36], vectors))
    print(get_score([24, 19, 25, 32], vectors))
    print(hack())
