class DisplayFixer():
    def __init__(self, filename='inputs/day08.txt'):
        def list_of_sets_maker(string):
            words = string.split()
            return [set(word) for word in words]

        self.patterns = [] # list of list of sets?
        self.outputs = []
        with open(filename, 'r') as f:
            lines = f.readlines()
            for line in lines:
                pattern_string, output_string = line.strip().split(" | ")
                self.patterns.append(list_of_sets_maker(pattern_string))
                self.outputs.append(list_of_sets_maker(output_string))

        self.canonicals = {
            frozenset('abcefg'): 0,
            frozenset('cf'): 1,
            frozenset('acdeg'): 2,
            frozenset('acdfg'): 3,
            frozenset('bcdf'): 4,
            frozenset('abdfg'): 5,
            frozenset('abdefg'): 6,
            frozenset('acf'): 7,
            frozenset('abcdefg'): 8,
            frozenset('abcdfg'): 9
        }

    def count_easy_outputs(self):
        total = 0
        for four_outputs in self.outputs:
            for output in four_outputs:
                if len(output) in [2, 3, 4, 7]:
                    total += 1
        return total

    def solve_display(self, i):
        patterns = self.patterns[i]
        outputs = self.outputs[i]
        connections = {} # the thing that should go to x actually goes to y
        patterns.sort(key=len) # 1, 7, 4, {2, 3, 5}, {0, 6, 9}, 8
        # for pattern in patterns:
        #     print(pattern)
        # print('')
        len5s = patterns[3:6]
        len6s = patterns[6:9]
        # 'a' is used in 7 but not 1
        connections['a'] = (patterns[1] - patterns[0]).pop()

        b_and_d = patterns[2] - patterns[0]
        for thing in b_and_d:
            if all(thing in pattern for pattern in len5s):
                connections['d'] = thing
            else:
                connections['b'] = thing


        g_set = set([c for c in patterns[-1]]) # need a copy
        for s in len5s:
            g_set.intersection_update(s)
        g_set -= set([connections['a'], connections['d']])
        connections['g'] = g_set.pop()

        b_and_e = set()
        c_d_and_e = set()
        # print(patterns[-1])
        for symbol in patterns[-1]:
            count = 0
            for pattern in len5s:
                # print(symbol, pattern)
                if symbol in pattern:
                    count += 1
            if count == 1:
                b_and_e.add(symbol)
            count = 0
            for pattern in len6s:
                if symbol in pattern:
                    count += 1
            if count == 2:
                c_d_and_e.add(symbol)

        for thing in b_and_e:
            # print(thing, patterns[1])
            if thing not in patterns[2]:
                connections['e'] = thing

        # print(len6s)
        # print(connections)
        # print("c_d_and_e", c_d_and_e)
        for thing in c_d_and_e:
            if thing not in connections.values():
                connections['c'] = thing

        for symbol in patterns[0]:
            if symbol != connections['c']:
                connections['f'] = symbol

        decrypt = {v: k for k, v in connections.items()}

        ans = []
        for output in outputs:
            ans.append(self.decrypt_output(decrypt, output))
        return int("".join([str(n) for n in ans]))

    def decrypt_output(self, decrypt, output):
        # print(decrypt)
        decrypted_set = set()
        for symbol in output:
            decrypted_set.add(decrypt[symbol])
        return self.canonicals[frozenset(decrypted_set)]

    def total_outputs(self):
        total = 0
        for i in range(len(self.outputs)):
            total += self.solve_display(i)
        return total

if __name__ == "__main__":
    df = DisplayFixer('inputs/day08.txt')
    print(df.count_easy_outputs())
    # returns 365
    print(df.total_outputs())
