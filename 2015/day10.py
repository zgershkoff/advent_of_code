# day 10, 2015

start = "3113322113"

def look_and_say(s):
    cur = None
    count = 0
    i = 0
    ans = ""
    while i < len(s):
        cur = s[i]
        count += 1
        while i+1 < len(s) and s[i+1] == cur:
            i += 1
            count += 1
        ans += str(count) + cur
        count = 0
        i += 1

    return ans

def solve(n):
    num = start
    for _ in range(n):
        num = look_and_say(num)
    return num

if __name__ == "__main__":
    print(look_and_say(start))
    print(132123222113)
    print(len(solve(40))) # 329356 digits!
    print(len(solve(50)))
