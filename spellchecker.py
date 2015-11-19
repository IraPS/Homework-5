__author__ = 'IrinaPavlova'


def typod(w1, w2):
    k = [['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
         ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
         ['z', 'x', 'c', 'v', 'b', 'n', 'm']]
    typo = 0
    if len(w1) == len(w2):
        for u in range(len(w1)):
            if w1[u] != w2[u]:
                l1 = w1[u]
                l2 = w2[u]
                for i in k:
                    if l1 in i:
                        l1i = str(k.index(i)) + str(i.index(l1))
                    if l2 in i:
                        l2i = str(k.index(i)) + str(i.index(l2))
                if l1i[0] == l2i[0]:
                    if abs(int(l1i[1])-int(l2i[1])) == 1:
                        typo += 1
                elif l1i[1] == l2i[1]:
                    typo += 1
                elif abs(int(l1i[0])-int(l2i[0])) == 1:
                    if abs(int(l1i[1])-int(l2i[1])) == 1:
                        typo += 1
    return typo


def dist(w1, w2):
    l1 = len(w1)
    l2 = len(w2)
    if l1 > 0 and l2 > 0:
        if w1[-1] == w2[-1]:
            c = dist(w1[:l1-1], w2[:l2-1])
        else:
            c = min(dist(w1, w2[:l2-1])+1, dist(w1[:l1-1], w2)+1, dist(w1[:l1-1], w2[:l2-1])+1)
    else:
        c = max(l1, l2)
    return c


def tot():
    d = {}
    word = input('Type the word, please ')
    file = input('Type the name of the file, please ')
    f = open(file, 'r', encoding='utf-8')
    f = f.read().split()
    for w in f:
        v = dist(word, w) - typod(word, w)*0,5
        d[w] = v
    d = sorted(d.items(), key=lambda x: x[1])
    ind = min(len(d), 3)
    for i in range(ind):
        yield d[i][0]


for el in tot():
    print(el)


