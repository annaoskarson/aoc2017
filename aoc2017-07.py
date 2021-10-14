fil = open('aoc2017-07-input.txt', 'r')
ls = fil.read().strip().split('\n')

#ls = ['pbga (66)', 'xhth (57)', 'ebii (61)', 'havc (66)', 'ktlj (57)',
#    'fwft (72) -> ktlj, cntj, xhth','qoyq (66)','padx (45) -> pbga, havc, qoyq',
#    'tknk (41) -> ugml, padx, fwft','jptl (61)','ugml (68) -> gyxo, ebii, jptl',
#    'gyxo (61)', 'cntj (57)']

def tree():
    discs = {}
    for l in ls:
        name = l.split(' ')[0]
        weight = int(l.split(' ')[1].strip('()'))
        nlist = []
        if '->' in l:
            nlist = [n.strip() for n in l.split('->')[1].split(',')]
        discs[name] = (weight, nlist)
    return(discs)

def root(tree):
    for b in tree.keys():
        allchildren = [item for sublist in tree.values() for item in sublist[1]]
        if tree[b][1] != [] and b not in allchildren:
            return(b)

def nodeweight(name, tree):
    if tree[name][1] == []:
        return(tree[name][0])
    else:
        return(tree[name][0] + sum([nodeweight(n, tree) for n in tree[name][1]]))

def balanced(node, tree):
    if tree[node][1] == []:
        return(True)
    else:
        subs = tree[node][1]
        return(all(nodeweight(subs[i], tree) == nodeweight(subs[i+1], tree) for i in range(len(subs) -1)))

def balance(node, tree, odd, amount):
    if not balanced(node, tree):
        weights = [nodeweight(a, tree) for a in tree[node][1]]
        if len(tree[node][1]) > 2:
            [odd] = [(tree[node][1][weights.index(x)]) for x in weights if weights.count(x) < 2]
            oddweight = weights[tree[node][1].index(odd)]
            weights.remove(oddweight)
            amount = weights[0] - oddweight
            # Om underträden är balanserade.
            if all(balanced(n, tree) for n in tree[node][1]):
                return(tree[odd][0] + amount)
            else:
                #om underträden inte är balanserade
                for n in tree[node][1]:
                    if not balanced(n, tree): #hitta vilket
                        return(balance(n, tree, odd, amount))
    else:
        return(tree[odd][0] + amount)



def partone():
    print("Advent of Code 2017, day 7, part 1.")
    print("The answer is:", root(tree()))

def parttwo():
    print("Advent of Code 2017, day 7, part 2.")
    t = tree()
    node = root(t)
    ans = balance(node,t, '', 0)
    print("The answer is:", ans)

partone()
parttwo()
