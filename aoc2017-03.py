input = 312051

def partone(x):
    print("Advent of Code 2017, day 3, part 1.")
    layer = 0
    highest = pow(2*layer, 2)

    while highest < x:
        layer += 1
        highest = pow(2*layer+1, 2)
    side = 2 * layer
    south = highest - layer
    dist = layer + min([abs(south - n*side - x) for n in range(0, 4)])
    print("The answer is:", dist)

def parttwo(num):
    print("Advent of Code 2017, day 3, part 2.")
    x, y, layer = 0, 0, 0
    numbers = {(x,y): 1}
    while num >= numbers[(x,y)]:
        if (y == -layer) and (-layer <= x <= layer):
            # one right
            x += 1
            if (x > layer):
                # new layer
                layer += 1
        elif (x == layer) and (-layer <= y < layer):
            # one up
            y += 1
        elif (y == layer) and (-layer < x <= layer):
            # one left
            x -= 1
        elif (x == -layer) and (-layer < y <= layer):
            # one down
            y -= 1
        # save sum of neighbors on the new coordinate
        numbers[(x,y)] = sum([numbers.get((a,b), 0) for a in [x-1, x, x+1] for b in[y-1, y, y+1] if (a,b) != (x,y)])

    print("The answer is:", numbers[(x,y)])

partone(input)
parttwo(input)
