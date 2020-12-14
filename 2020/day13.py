# day 13, 2020

inFile = "d13.txt"
earliest = 0
periods = []

def preprocess():
    global earliest
    global periods
    with open(inFile, 'r') as f:
        r = f.readlines()
        earliest = int(r[0])
        periods.extend(r[1].strip().split(','))

def part1():
    best = float('inf')
    bus_id = 0

    for p in periods:
        if not p.isnumeric():
            continue
        p = int(p)
        wait_time = -earliest % p # - because we want to know time left
        if wait_time < best:
            print(wait_time, best)
            best = wait_time
            bus_id = p
    return  best * bus_id

def part2():
    # this is solved by the chinese remainder theorem.
    # I'll write methods to get the moduli and remainders but I don't
    # want to code the crt right now.
    mods = []
    rems = []
    inc = 0

    for p in periods:
        if p.isnumeric():
            p = int(p)
            mods.append(p)
            rems.append(-inc)
        inc += 1

    return crt(mods, rems)

### copied from geeksforgeeks
# Python 2.x program to combine modular equations
# using Chinese Remainder Theorem

# function that implements Extended euclidean
# algorithm
def extended_euclidean(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_euclidean(b % a, a)
        return (g, x - (b // a) * y, y)

# modular inverse driver function
def modinv(a, m):
    g, x, y = extended_euclidean(a, m)
    return x % m

# function implementing Chinese remainder theorem
# list m contains all the modulii
# list x contains the remainders of the equations
def crt(m, x):

    # We run this loop while the list of
    # remainders has length greater than 1
    while True:

        # temp1 will contain the new value
        # of A. which is calculated according
        # to the equation m1' * m1 * x0 + m0'
        # * m0 * x1
        temp1 = modinv(m[1],m[0]) * x[0] * m[1] + \
                modinv(m[0],m[1]) * x[1] * m[0]

        # temp2 contains the value of the modulus
        # in the new equation, which will be the
        # product of the modulii of the two
        # equations that we are combining
        temp2 = m[0] * m[1]

        # we then remove the first two elements
        # from the list of remainders, and replace
        # it with the remainder value, which will
        # be temp1 % temp2
        x.remove(x[0])
        x.remove(x[0])
        x = [temp1 % temp2] + x

        # we then remove the first two values from
        # the list of modulii as we no longer require
        # them and simply replace them with the new
        # modulii that we calculated
        m.remove(m[0])
        m.remove(m[0])
        m = [temp2] + m

        # once the list has only one element left,
        # we can break as it will only contain
        # the value of our final remainder
        if len(x) == 1:
            break

    # returns the remainder of the final equation
    return x[0]


if __name__ == "__main__":
    preprocess()
    print(part1())
    print(part2())
