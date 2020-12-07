# day 12, 2015

import re

inFile = "d12.txt"

def do_it():
    total = 0
    with open(inFile, 'r') as f:
        for line in f.readlines():
            parts = re.split(',| |\[|\]|\{|\}|"|\'|:', line.strip())
            print(parts)
            for p in parts:
                if p.lstrip("-").isnumeric():
                    total += int(p)
    return total
    # 111754

# looks like I need to actually use json for part 2
import json

def use_json():
    with open(inFile, 'r') as f:
        data = json.load(f)
    total = unpack_dict(data)
    return total

def unpack_dict(data, total = 0):
    if "red" in data.values():
        return total
    return unpack(data.values(), total)

def unpack_list(data, total = 0):
    return unpack(data, total)

def unpack(data, total = 0):
    for thing in data:
        if type(thing) == dict:
            total += unpack_dict(thing)
        elif type(thing) == list:
            total += unpack_list(thing)
        elif type(thing) == int:
            total += thing
    return total

if __name__ == "__main__":
    print(use_json())
