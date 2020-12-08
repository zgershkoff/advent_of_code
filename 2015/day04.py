# 2015 day 4

from hashlib import md5

key = "yzbqklnj"
target = "000000"

def c1():
    i = 0
    while True:
        key2 = str(i)
        whole_key = key + key2
        encoded = bytearray(whole_key, 'utf-8')
        if md5(encoded).hexdigest()[:len(target)] == target:
            return i
        i += 1

if __name__ == "__main__":
    print(c1())
