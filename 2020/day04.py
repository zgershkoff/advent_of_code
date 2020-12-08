# day 4, 2020

inFile = "d04.txt"

eye_colors = set(["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])

def preprocess():
    passport_list = []
    with open(inFile, 'r') as f:
        d = {}
        for line in f.readlines():
            if line.strip() == "":
                passport_list.append(d)
                d = {}
            pairs = line.strip().split()
            for pair in pairs:
                key, val = pair.split(":")
                d[key] = val

    return c2(passport_list)

def c1(passport_list):
    count = 0
    for d in passport_list:
        if len(d) == 8 or (len(d) == 7 and "cid" not in d):
            count += 1

    return count

def c2(passport_list):
    count = 0
    for d in passport_list:
        if len(d) == 8 or (len(d) == 7 and "cid" not in d):
            check = []
            check.append("1920" <= d["byr"] <= "2002")
            check.append("2010" <= d["iyr"] <= "2020")
            check.append("2020" <= d["eyr"] <= "2030")
            if len(d["hgt"]) <= 2:
                check.append(False)
            else:
                num = int(d["hgt"][:-2])
                if d["hgt"][-2:] == "cm":
                    check.append(150 <= num <= 193)
                elif d["hgt"][-2:] == "in":
                    check.append(59 <= num <= 76)
                else:
                    check.append(False)
            valid_ch = all(c in "0123456789abcdef" for c in d["hcl"][1:])
            check.append(d["hcl"][0] == "#" and valid_ch and len(d["hcl"]) == 7)
            check.append(d["ecl"] in eye_colors)
            check.append(d["pid"].isnumeric() and len(d["pid"]) == 9)


            if all(c for c in check):
                count += 1

    return count

if __name__ == "__main__":
    print(preprocess())
