fil = open('5-input.txt', 'r')
code = list(map(int, fil.read().split('\n')[:-1]))

#code = [0,3,0,1,-3]

def partone():
    print("Advent of Code 2017, day 5, part 1.")
    steps = 0
    i=0
    while i >=0 and i < len(code):
        code[i] = code[i] + 1
        i = i + code[i] - 1
        steps = steps + 1
    print("The answer is:", steps)
#    print(code)

def parttwo():
    print("Advent of Code 2017, day 5, part 2.")
    steps = 0
    i=0
    while i >=0 and i < len(code):
        instr = code[i]
        if instr >= 3:
            code[i] = code[i] - 1
        else:
            code[i] = code[i] + 1
        i = i + instr
        steps = steps + 1

    print("The answer is:", steps)
#    print(code)


#partone()
parttwo()
