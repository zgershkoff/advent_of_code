# day 6, 2020

inFile = "d6.txt"

def preprocess1():
    answers = []
    with open(inFile, 'r') as f:
        yeses = set()
        for line in f.readlines():
            if line.strip() == "":
                answers.append(yeses)
                yeses = set()
            yeses.update(line.strip())

    return count(answers)

def count(answers):
    return sum(len(yeses) for yeses in answers)

# same thing, but start with all possibilities and intersect down
def preprocess2():
    answers = []
    with open(inFile, 'r') as f:
        yeses = set("abcdefghijklmnopqrstuvwxyz")
        for line in f.readlines():
            if line.strip() == "":
                answers.append(yeses)
                yeses = set("abcdefghijklmnopqrstuvwxyz")
            else:
                yeses.intersection_update(line.strip())

    return count(answers)

if __name__ == "__main__":
    print(preprocess2())
