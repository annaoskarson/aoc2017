fil = open('aoc2017-08-input.txt', 'r')
ls = fil.read().strip().split('\n')

mem = {}
ans2 = 0
for l in ls:
    reg, com, val, _, creg, cond, cval = l.split(' ')
    for r in [reg, creg]:
        if r not in mem.keys():
            mem[r] = 0
    if (cond == '>' and mem[creg] > int(cval)) or \
        (cond == '>=' and mem[creg] >= int(cval)) or \
        (cond == '<' and mem[creg] < int(cval)) or\
        (cond == '<=' and mem[creg] <= int(cval)) or \
        (cond == '==' and mem[creg] == int(cval)) or \
        (cond == '!=' and mem[creg] != int(cval)):
        if com == 'inc':
            mem[reg] += int(val)
        elif com == 'dec':
            mem[reg] -= int(val)
    ans2 = max(ans2, max(mem.values()))
ans = max(mem.values())

def partone():
    print("Advent of Code 2017, day 8, part 1.")
    print("The answer is:", ans)

def parttwo():
    print("Advent of Code 2017, day 7, part 2.")
    print("The answer is:", ans2)

partone()
parttwo()
