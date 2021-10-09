input = 312051

#input = 1 # answer is 1
#input = 12 # answer is 3
#input = 23 # answer is 2
#input = 1024 # answer is 31

#input = 11

def partone(x):
    print("Advent of Code 2017, day 3, part 1.")
    layer = 1
    upper = pow(2*layer-1, 2)
    while upper < x:
        layer += 1
        upper = pow(2*layer-1, 2)
    out = layer-1
    side = 2 * out
    s = upper - out
    sideways = min(abs(s-x), abs(s-side-x), abs(s-2*side-x), abs(s-3*side-x))
    ans = out + sideways
    print("The answer is:", ans)

def parttwo(num):
    print("Advent of Code 2017, day 3, part 2.")

    def sumneighbours(c,di):
        (a,b) = c
        neighbours = []
        # Make a list with the coordinates of the neighbours.
        for i in range(-1,2):
            for j in range(-1,2):
                if (a+i, b+j) != (a,b):
                    neighbours.append((a+i, b+j))
        s = 0
        for (coord) in neighbours:
            s += di.get(coord, 0)
        return(s)

    numbers = {}
    current, x, y, layer, counter = 1, 0, 0, 0, 1
    numbers[(x,y)] = current
    while num >= current:
        if (x,y) == (layer, -layer):
            # one right, new layer
            x += 1
            layer += 1
        elif (x == layer) and (y < layer) and (y >= -layer):
            # one up
            y += 1
        elif (y == layer) and (x <= layer) and (x > -layer):
            # one left
            x -= 1
        elif (x == -layer) and (y <= layer) and (y > -layer):
            # one down
            y -= 1
        elif (y == -layer) and (x < layer) and (x >= -layer):
            # one right
            x += 1
        current = sumneighbours((x,y), numbers)
        numbers[(x, y)] = current

    ans=current
    print("The answer is:", ans)

partone(input)
parttwo(input)
