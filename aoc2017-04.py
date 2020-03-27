fil = open('aoc2017-04-input.txt', 'r')

raw = fil.read().split('\n')[:-1]
phrases = []
for row in raw:
    newrow = row.split(' ')
    phrases = phrases + [newrow]

def partone():
    print("Advent of Code 2017, day 4, part 1.")
    ans = 0
    for row in phrases:
        if len(row) == len(set(row)):
            ans = ans + 1                       
    print("The answer is:", ans)

def parttwo():
    print("Advent of Code 2017, day 4, part 2.")
    def nogram(item):
        s_item = []
        for word in item:
            sword = ''.join(sorted(word))
#            print(word, sword)
            s_item = s_item + [sword]
        return(len(s_item) == len(set(s_item)))
    ans = 0
    for row in phrases:
        if len(row) == len(set(row)) and nogram(row):
            ans = ans + 1
    print("The answer is:", ans)

partone()
parttwo()
