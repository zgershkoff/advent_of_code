# day 16, 2020

inFile = "d16.txt"
range_dict = {} # name: list of two tuples
my_ticket = []
tickets = []

def preprocess():
    f = open(inFile, 'r')
    line = next(f).strip()
    while line:
        name, nums = line.split(": ")
        # ranges = nums.split(" or ")
        # print([r.split("-") for r in ranges])
        # range_dict[name] = [(int(a), int(b)) for r in ranges for a, b in r.split("-")]
        ranges = [r.split("-") for r in nums.split(" or ")]
        range_dict[name] =[[int(n) for n in r] for r in ranges]
        line = next(f).strip()

    line = next(f) # your ticket:
    line = next(f).strip()
    my_ticket.extend([int(n) for n in line.split(",")])

    line = next(f) # blank
    line = next(f) # other tickets:
    line = next(f).strip()
    while line: # added a blank line at the end of the data so this will work
        tickets.append([int(n) for n in line.split(",")])
        line = next(f).strip()

def interval_union(l):
    start, end = 0, 1
    starts = [sublist[0] for sublist in l]
    ends = [sublist[1] for sublist in l]
    pts = [(s, start) for s in starts] + [(t, end) for t in ends]
    # flagging ends with 1 so they get seen last, if a start and end
    # is at the same point

    pts.sort()
    ans = []
    counter = 0

    for pt, kind in pts:
        if counter == 0:
            start_val = pt
        if kind == start:
            counter += 1
        else:
            counter -= 1
        if counter == 0:
            ans.append([start_val, pt])

    return ans

def get_valid_intervals():
    intervals = [l for field in range_dict.values() for l in field]
    return interval_union(intervals)

def is_in_intervals(intervals, val):
    for s, t in intervals:
        if val >= s and val <= t:
            return True
    return False

# ok, at this point I get a single interval [25, 974]
# just going to work with that

def part1():
    errors = []
    for ticket in tickets:
        for val in ticket:
            if val < 25 or val > 974:
                errors.append(val)
    return sum(errors)

def part2():
    valid_tix = [t for t in tickets if all((v >= 25 and v <= 974) for v in t)]
    d = {i: set(range_dict.keys()) for i in range(len(my_ticket))}

    for ticket in valid_tix:
        for i, val in enumerate(ticket):
            for field in range_dict:
                if not is_in_intervals(range_dict[field], val):
                    d[i].discard(field)

    ans = []
    while d:
        for i in d:
            if len(d[i]) == 1:
                key = list(d[i])[0]
                if is_departure(key):
                    ans.append(my_ticket[i])
                for j in d:
                    d[j].remove(key)
                del d[i]
                break

    return prod(ans)

def prod(l):
    ans = 1
    for n in l:
        ans *= n
    return ans


def is_departure(s):
    return s[:9] == "departure"

    for i in d:
        print(i, d[i])
        print()



if __name__ == "__main__":
    preprocess()
    get_valid_intervals()
    print(part2())

