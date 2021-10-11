fil = open('aoc2017-06-input.txt', 'r')

bank = [int(x) for x in fil.read().strip().split('\t')]

#print(bank)

def deal(block, b):
    amount = b[block]
    b[block] = 0
    for n in range(amount):
        next = (block+1+n)%len(b)
        b[next] = b[next] + 1
        print(next, b)
#    print(block, amount)
    return(b)

def partone(b1):
    print("Advent of Code 2017, day 6, part 1.")
    all = [b1]
    print(all)
    i = 0
    b2 = deal(i, b1)
    print(all)
    while b2 not in all:
        all.append(b2)
        print(b1, b2)
        i = (i+1)%len(b)
        b2 = deal(i, b2)

    print(b2)
    ans = 0
    print("The answer is:", ans)

def parttwo():
    print("Advent of Code 2017, day 6, part 2.")

    ans = 0
    print("The answer is:", ans)

partone(bank)
#parttwo()
