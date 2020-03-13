fil = open('2-input.txt', 'r')

numbers = []
raw = fil.read().split('\n')[:-1]
for row in raw:
    row = row.replace('\t', ',')
    row = row.split(',')
    newrow = []
    for item in row:
        item = int(item)
        newrow = newrow + [item]
    numbers = numbers + [newrow]

def partone():
    print("Advent of Code 2017, day 2, part 1.")
    ans = 0
    for row in numbers:
        rval = max(row) - min(row)
        ans = ans + rval
    print("The answer is:", ans)

def parttwo():
    print("Advent of Code 2017, day 2, part 2.")
    ans = 0
    for row in numbers:
        for a in row:
            for b in row:
                if a != b and a%b == 0:
                    rval = a//b
                    ans = ans + rval
    print("The answer is:", ans)

partone()
parttwo()
