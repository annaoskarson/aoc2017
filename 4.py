fil = open('4-input.txt', 'r')
#line = fil.readline()

#line = line.replace('\t', ',')
#line = line.replace('\n', '')
#line = [line]
#print(line)

#raw = fil.read()

#print(raw)
#print(type(raw))

raw = fil.read().split('\n')[:-1]
phrases = []
for row in raw:
    newrow = row.split(' ')
    phrases = phrases + [newrow]
    
#print(phrases)

##numbers = []
##raw = fil.read().split('\n')[:-1]
##for row in raw:
##    row = row.replace('\t', ',')
##    row = row.split(',')
##    newrow = []
##    for item in row:
##        item = int(item)
##        newrow = newrow + [item]
##    numbers = numbers + [newrow]
##
#print(numbers)

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
