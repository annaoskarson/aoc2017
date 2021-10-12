fil = open('aoc2017-07-input.txt', 'r')
l = fil.read().strip().split('\n')

def root():
    discs = {}
    for a in l:
        a = (a.split('->'))
        if len(a) > 1:
            discs[a[0].split(' ')[0]] = [x.strip() for x in a[1].split(',')]
        else:
            discs[a[0].split(' ')[0]] = ['']

    for b in discs.keys():
        if discs[b] != [''] and b not in [item for sublist in discs.values() for item in sublist]:
            return(b)

def partone():
    print("Advent of Code 2017, day 7, part 1.")
    print("The answer is:", root())
    return(l)

def parttwo():
    print("Advent of Code 2017, day 7, part 2.")
#    (ans, l) = loop(c1)
    print("The answer is:", ans)

partone()
#parttwo(two)
