fil = open('aoc2017-06-input.txt', 'r')
bank = [int(x) for x in fil.read().strip().split('\t')]

def deal(b):
    c = b[:]
    # Pick largest value.
    block = c.index(max(c))
    amount = c[block]
    c[block] = 0
    for n in range(amount):
        next = (block+1+n)%len(c)
        c[next] += 1
    return(c)

def loop(l):
    all = [l]
    l2 = deal(l)
    while l2 not in all:
        all.append(l2)
        l2 = deal(l2)
    return(len(all), l2)

def partone(b1):
    print("Advent of Code 2017, day 6, part 1.")
    (ans, l) = loop(b1)
    print("The answer is:", ans)
    return(l)

def parttwo(c1):
    print("Advent of Code 2017, day 6, part 2.")
    (ans, l) = loop(c1)
    print("The answer is:", ans)

two = partone(bank)
parttwo(two)
