# year 2015 day 25

row = 2981
column = 3075
seed = 20151125
mult = 252533
mod = 33554393

def find_index(row, column):
    diag = row + column - 1
    top = (diag + 1) * diag // 2
    idx = top - row + 1
    return idx

def get_next_code(n):
    return (n * mult) % mod

def c1():
    n = seed
    for _ in range(find_index(row, column) - 1):
        n = get_next_code(n)
    return n

if __name__ == "__main__":
    print(c1())
