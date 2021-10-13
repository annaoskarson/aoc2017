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
        #print(name, 'end', tree[name][0])
        #print(tree[name][0])
        return(tree[name][0])
        #return(0)
    else:
        #print(name, 'not end', tree[name][0], tree[name][1])
        return(tree[name][0] + sum([nodeweight(n, tree) for n in tree[name][1]]))
#        for n in tree[name][1]:
#            print(tree[name][0])
            #print(name, 'not end')
#            return(tree[name][0] + nodeweight(n, tree))

def balanced(node, tree):
    if tree[node][1] == []:
        return(True)
    else:
        subs = tree[node][1]
        #print(subs)
        #print(subs, [nodeweight(s, tree) for s in subs])
        return(all(nodeweight(subs[i], tree) == nodeweight(subs[i+1], tree) for i in range(len(subs) -1)))
        #return(all(tree[node][1][i+1] == tree[node][1][i] for i in range(len(tree[node][1])-1)))
        #return(all(nodeweight(elem,tree) for elem in tree[node][1]))
        #return(all(elem == tree[node][1][0] for elem in tree[node][1][1:]))

def balance(node, tree, odd, amount):
    print('checking:', node, tree[node])
    if not balanced(node, tree):
        weights = [nodeweight(a, tree) for a in tree[node][1]]
        print('unbalanced', node, weights, tree[node][1])
        if len(tree[node][1]) > 2:
            [odd] = [(tree[node][1][weights.index(x)]) for x in weights if weights.count(x) < 2]
            oddweight = weights[tree[node][1].index(odd)]

#            print(oddweight)
#            print(len(weights))
            weights.remove(oddweight)
#            print(len(weights), weights)
#            print(oddweight - weights[0])
            amount = weights[0] - oddweight
#            print([x for x in [weights[i+1]-weights[i] for i in range(len(weights)-1)] if x != 0 ])
#            [amount] = [x for x in [weights[i+1]-weights[i] for i in range(len(weights)-1)] if x != 0 ]
            #print('odd:', odd, amount)

            #print('underträd:', [balanced(n, tree) for n in tree[node][1]], tree[node][1])
            #print(odd, )
            # Om underträden är balanserade.
            if all(balanced(n, tree) for n in tree[node][1]):
                print('OK')
                return(tree[odd][0] + amount)
            else:
                #om underträden inte är balanserade
                print('else', tree[node][1])
                for n in tree[node][1]:
                    return(balance(n, tree, odd, amount))
                #return([balance(n, tree) for n in tree[node][1]])
    else:
        print('yes', odd, tree[odd][0], amount)
        return(tree[odd][0] + amount)



def partone():
    print("Advent of Code 2017, day 7, part 1.")
    print("The answer is:", root(tree()))

def parttwo():
    print("Advent of Code 2017, day 7, part 2.")
    t = tree()
    #print(t)
    node = root(t)
    #print('hela vikten:', nodeweight(node, t))
    #print(balanced(node, t))
    ans = balance(node,t, '', 0)
    # 47829 too high
    # 47811 too high
    #ans = 0
    print("The answer is:", ans)

partone()
parttwo()
