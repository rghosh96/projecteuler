doc = open('poker_hands.txt')
doc = doc.read()
doc = doc.replace('\n','')
doc = doc.replace(' ','')
hands = [doc[i:i+20] for i in range(0,19981,20)]

Values = {
    '1':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    'A':10,
    'B':11,
    'C':12,
    'D':13,
    'E':14
}
V = {
    'T':'A',
    'J':'B',
    'Q':'C',
    'K':'D',
    'A':'E'
}

def ptokens(lst):
    global Values
    tokens = []
    lst = [x[::2] for x in lst]
    for index, i in enumerate(lst):
        lst[index] = ''.join([V[x] if x in V else x for x in i])
    lst = [(''.join(sorted(x[:5])),''.join(sorted(x[5:]))) for x in lst]
    for i in lst:
        temp = []
        for k in i:
            if len(set(k))==len(k):
                temp.append(tuple(k))
            else:
                stack = []
                tu = []
                prev = k[0]
                for r in k:
                    if r == prev:
                        stack.append(r)
                    else:
                        prev = r
                        tu.append(''.join(stack))
                        stack.clear()
                        stack.append(r)
                else:
                    tu.append(''.join(stack))
                tu = tuple(tu)
                temp.append(tu)
        tokens.append(temp)
    return tokens

def counts(lst):
    def flsh(lst):
        Flushes = {}
        for index, i in enumerate(lst):
            if len(set(i[:10][1::2])) == 1:
                Flushes[index] = 1,0
            if len(set(i[10:][1::2])) == 1:
                try:
                    y = Flushes[index]
                    Flushes[index] = 1,1
                except KeyError:
                    Flushes[index] = 0,1
        return Flushes
    D = flsh(lst)
    a = ptokens(lst)
    def ranks(token,index,pos):
        def high(tok):
            tok = list(tok)
            h = []
            q = [x for x in range(1,5)][::-1]
            p2 = []
            for i in q:
                if i == 1:
                    for r in p2[::-1]:
                        tok.pop(tok.index(r))
                        h.append(r[0])
                if i == 1:
                    for p in tok[::-1]:
                        h.append(p[0])
                    h = [Values[x] for x in h]
                    return h
                for k in tok:
                    if i == 2 and len(k) == 2:
                        p2.append(k)
                        continue
                    if len(k) == i:
                        h.append(k[0])
                        tok.pop(tok.index(k))
        rank = 0
        for i in token:
            if len(set(token)) == 2:
                if len(i) == 1:
                    rank = 7
                    break
                elif len(i) == 2:
                    rank = 6
                    break
            elif len(set(token)) == 3:
                if len(i)==3:
                    rank = 3
                    break
                elif len(i)==2:
                    rank = 2
                    break
            elif len(set(token)) == 4:
                rank = 1
                break
            elif len(set(token)) == 5:
                if Values[token[4]]==Values[token[0]]+4:
                    if index in D:
                        if D[index][pos] == 1:
                            if token[4]=='E':
                                rank = 9
                                break
                            rank = 8
                            break
                    rank = 4
                    break
                else:
                    if token[4] == 'E':
                        if token[3] == '5':
                            rank = 4
                            break
                    rank = 0
                    break
        if index in D:
            if D[index][pos] == 1:
                if 5 > rank:
                    rank = 5
        return (rank,high(token))
    count1, count2 = 0,0
    for index, i in enumerate(a):
        if ranks(i[0], index, 0)[0] > ranks(i[1],index,1)[0]:
            count1 += 1
        elif ranks(i[0],index,0)[0]==ranks(i[1],index,1)[0]:
            k = True
            p = 0
            while k:
                for ind,j in enumerate(ranks(i[0],index,0)[1]):
                    if j > ranks(i[1],index,1)[1][ind]:
                        count1 +=1
                        k = False
                        break
                    elif j == ranks(i[1],index,1)[1][ind]:
                        p += 1
                        if p > 5:
                            k = False
                            break
                        continue
                    else:
                        count2+=1
                        k = False
                        break
        else:
            count2+=1
    return 'Player one wins {} games. Player two wins {} games.'.format(count1,count2)


a = ptokens(hands)
#counts(hands[:5])
counts(hands)
#ranks(a[6][0],0,0)
