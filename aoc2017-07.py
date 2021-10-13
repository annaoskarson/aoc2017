fil = open('aoc2017-07-input.txt', 'r')
ls = fil.read().strip().split('\n')

ls = ['pbga (66)', 'xhth (57)', 'ebii (61)', 'havc (66)', 'ktlj (57)',
    'fwft (72) -> ktlj, cntj, xhth','qoyq (66)','padx (45) -> pbga, havc, qoyq',
    'tknk (41) -> ugml, padx, fwft','jptl (61)','ugml (68) -> gyxo, ebii, jptl',
    'gyxo (61)', 'cntj (57)']

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
        #print(name, 'end')
        return(tree[name][0])
    else:
        for n in tree[name][1]:
            #print(name, 'not end')
            return(tree[name][0] + nodeweight(n, tree))

def balanced(node, tree):
    if tree[node][1] == []:
        return(True)
    else:
        return(all(elem == tree[node][1][0] for elem in tree[node][1][1:]))

def balance(node, tree):
    if not balanced(node, tree):
        weights = [nodeweight(a, tree) for a in tree[node][1]]
        if len(tree[node][1]) > 2:
            print('weights', weights)
            print([weights.index(x) for x in weights if weights.count(x) < 2 ])
            print([x for x in tree[node][1] if tree[node][1].count(x) < 2 ])
        # Om underträden är balanserade.
        if all(balanced(n, tree) for n in tree[node][1]):
            print([nodeweight(a, tree) for a in tree[node][1]])
#        if all(tree[n][1] == [] for n in tree[node][1]):

def partone():
    print("Advent of Code 2017, day 7, part 1.")
    print("The answer is:", root(tree()))

def parttwo():
    print("Advent of Code 2017, day 7, part 2.")
    t = tree()
    #print(t)
    node = 'tknk'
    #node = 'ktlj'
    # Kolla om barnen är lika. Om de är lika behöver inget göras ...
    # Om barnen är olika, om de är två, kolla båda, om de är flera, kolla det avvikande.
    # Kan ju vara dumt att ändra i löven, om det är någon annanstans det behöver ändras ...
    print('hela vikten:', nodeweight(node, t))
    print(balanced(node, t))
    balance(node,t)
    ans = 0
    print("The answer is:", ans)

partone()
parttwo()
