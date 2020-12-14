# day 14, 2020

inFile = "d14.txt"

instructions = [] # mixed list of mask strings and tuples (address, val)
# thoughts: convert the mem values to binary with zfill(36)
# then insert from the binary string into the mask, then convert to int

def preprocess():
    with open(inFile, 'r') as f:
        for line in f.readlines():
            parts = line.split()
            if parts[0] == "mask":
                instructions.append(parts[2])
            else:
                address = int(parts[0].strip("]").lstrip("mem["))
                val = int(parts[2])
                instructions.append((address, val))

def part1():
    mem = {}
    mask = []
    for item in instructions:
        if len(item) == 2:
            address, val = item
            val_bin = bin(val).lstrip('0b').zfill(36)
            bits = []
            for i in range(len(mask)):
                if mask[i] == 'X':
                    bits.append(val_bin[i])
                else:
                    bits.append(mask[i])
            masked_val = int("".join(bits), 2)
            mem[address] = masked_val
        else:
            mask = list(item)

    return sum(mem.values())

def part2():
    mem = {}
    def recurse(mask, address, sofar = []):
        if len(sofar) == len(mask):
            addresses.append(int("".join(sofar), 2))
            return
        idx = len(sofar)
        if mask[idx] == "0":
            recurse(mask, address, sofar + [address[idx]])
        elif mask[idx] == "1":
            recurse(mask, address, sofar + ["1"])
        elif mask[idx] == "X":
            recurse(mask, address, sofar + ["0"])
            recurse(mask, address, sofar + ["1"])

    mask = []
    for item in instructions:
        if len(item) == 2:
            address, val = item
            address_bin = bin(address).lstrip('0b').zfill(36)
            addresses = []
            recurse(mask, address_bin, [])
            for a in addresses:
                mem[a] = val
        else:
            mask = list(item)

    return sum(mem.values())

if __name__ == "__main__":
    preprocess()
    print(part2())
