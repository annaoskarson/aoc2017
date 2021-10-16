fil = open('aoc2017-09-input.txt', 'r')
ls = fil.read()

i, score, sum, garb = 0, 0, 0, 0
while i < len(ls):
    if ls[i] =='<': # Skräp börjar, ta bort allt skräp.
        while ls[i] != '>':
            if ls[i] == '!':
                i += 1
                garb -= 1 # Räkna inte nästa tecken
            i += 1
            garb += 1
        garb -= 1 # Räkna inte avslutande >
    if ls[i] == '{': # Ny grupp börjar, öka score
        score += 1
    if ls[i] == '}': # Grupp slutar, räkna poäng, hoppa ner en score
        sum += score
        score -= 1
    i += 1


def partone():
    print("Advent of Code 2017, day 9, part 1.")
    print("The answer is:", sum)

def parttwo():
    print("Advent of Code 2017, day 9, part 2.")
    print("The answer is:", garb)

partone()
parttwo()
