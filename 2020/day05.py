# day 5, 2020

inFile = "d05.txt"

d = {"L": "0", "R": "1", "F": "0", "B": "1"}

def preprocess():
    best = 0
    seats = set()
    with open(inFile, 'r') as f:
        for line in f.readlines():
            row, col = get_numbers(line.strip())
            seat = get_seat_id(row, col)
            seats.add(seat)
            best = max(best, seat)

    # for part 1:
    # return best

    # my preference for taking in a data stream and maintaining
    # a sorted list would be to sort it inplace using bisect.insort()
    # but the size of this data was small and I wanted to write it quick
    seat_list = sorted(list(seats))
    for seat in seat_list:
        if seat + 1 not in seats:
            return seat + 1


def get_numbers(s):
    s_b = ""
    for c in s:
        s_b += d[c]

    row_string_b, col_string_b = s_b[:7], s_b[7:]

    return int(row_string_b, 2), int(col_string_b, 2)

def get_seat_id(row, col):
    return row * 8 + col


if __name__ == "__main__":
    print(preprocess())
