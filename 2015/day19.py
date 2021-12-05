# day 19, 2015

from collections import defaultdict
import re
from copy import copy

inFile = "d19.txt"
d = defaultdict(list) # element: [things it maps to]
subject = ""

expression = "[A-Z][a-z]*"

def preprocess():
    global subject
    with open(inFile, 'r') as f:
        read = f.readlines()
        for line in read:
            if not line.strip():
                break
            parts = line.strip().split()
            d[parts[0]].append(parts[-1])
        subject = read[-1].strip()

def to_list(s):
    # use regular expression for splitting on capitals
    ## It's curious that 'e' has replacements but doesn't show up
    ## in the subject string. Part 2, perhaps?
    return re.findall(expression, s)

def p1():
    preprocess()
    return len(build_step(subject))

def build_step(molecule):
    if molecule == 'e':
        formula = ['e']
    else:
        formula = to_list(molecule)
    possibilities = set()
    for elt in d:
        for i, part in enumerate(formula):
            # print(elt, part)
            # print(elt, type(elt), part, type(part))
            if part == elt:
                for replacement in d[elt]:
                    result = copy(formula)
                    result[i] = replacement
                    # print(result)
                    possibilities.add("".join(result))
    return possibilities

### This is the wrong approach. Start with the subject and work backwards
### Means reversing the dict from part 1
# def p2():
#     preprocess()
#     # print(d['e'])
#     # print(subject)
#     # manufactured = {e: 0} # molecule: smallest number of steps
#     manufactured = set(['e'])
#     # idea: keep the above dictionary of molecules and first time seen
#     # every iteration, keep a list of new molecules and build from it
#     # prune the tree in some intelligent way? no.
#     mols = set(['e'])
#     counter = 0
#     while subject not in mols:
#         # print(mols)
#         print(max(len(mol) for mol in mols))
#         # print(len(manufactured))
#         # if len(mols) > 5:
#         #     exit()
#         counter += 1
#         new_mols = set()
#         for mol in mols:
#             next_mols = build_step(mol)
#             # print(next_mols)
#             for next_mol in next_mols:
#                 if next_mol not in manufactured:
#                     new_mols.add(next_mol)
#         mols = new_mols
#         manufactured.update(mols)

#     return counter

# def count_caps(s):
#     return sum(1 for c in s if c.isupper())

# def preprocess2():
#     # on inspection, each molecule in the range is unique
#     d = {} # molecule: element that maps to it
#     with open(inFile, 'r') as f:
#         read = f.readlines()
#         for line in read:
#             if not line.strip():
#                 break
#             parts = line.strip().split()
#             d[parts[-1]] = parts[0]
#         subject = read[-1].strip()
#     return d, subject

### Turns out bfs from the other direction is also the wrong approach!
# def p2():
#     # idea: sort preimages according to length, try greedy dfs
#     preimages, subject = preprocess2()
#     pretuples = [(compound, preimages[compound]) for compound in preimages]
#     pretuples.sort(key = lambda x: count_caps(x[0]), reverse=True)
#     print(pretuples)
#     counter = 0
#     seen = set([subject])
#     new_mols = set([subject])
#     while 'e' not in new_mols:
#         print(new_mols)
#         counter += 1
#         next_mols = set()
#         for mol in new_mols:
#             for compound, element in pretuples:
#                 matches = re.finditer(compound, mol)
#                 broken = False
#                 for match in matches:
#                     candidate = (mol[:match.start()] + element +
#                                 mol[match.end():])
#                     if 'e' in candidate and candidate != 'e':
#                         break
#                     if candidate not in seen:
#                         # print(counter, compound, len(candidate))
#                         next_mols.add(candidate)
#                         broken = True
#                         break
#                 if broken:
#                     break

#         new_mols = next_mols
#         seen.update(new_mols)
#         if not new_mols:
#             exit()

#     return counter

'''
Disappointing problem because solving the example is not good preparation
for solving the real problem.
'''
def smarter_not_harder():
    preprocess()
    # subject = 'CRnFYFYFArPMg'
    num_parens = subject.count('Ar')
    num_extras = subject.count('Y')
    num_elts = count_caps(subject)
    num_lost_from_reductions = 4 * num_parens + 2 * num_extras
    num_reductions = num_parens
    num_after_reductions = num_elts - num_lost_from_reductions + num_reductions
    return num_reductions + (num_after_reductions - 1)

if __name__ == "__main__":
    print(smarter_not_harder())



