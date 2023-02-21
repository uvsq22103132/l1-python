from copy import deepcopy




carre_mag = [[4,14,15,1],
             [9,7,6,12],
             [5,11,10,8],
             [16,2,3,13]]
carre_pas_mag = [[4,14,15,1],
                 [9,7,6,12],
                 [5,11,10,8],
                 [16,2,7,13]]


def affichecarre(carre):
    for ligne in carre:
        print('\t'.join([str(x) for x in ligne]))
    





def testligneegale(carre):
    somme = sum(carre[0])
    resulta = 0
    for l in range(4):
            if sum(carre[l]) != somme:
                 resulta = -1
            else:
                resulta = somme
    return resulta





def testcolonneegale(carre):
    somme_cols = 0
    for l in carre:
        for c in range(4):
            somme_cols[c] += l[c]
    s = somme_cols[0]
    if somme_cols == [s,s,s,s]:
        return s
    else:
        return -1





def testdiagoegale(carre):
    l = carre[0][0] + carre[1][1] + carre[2][2] + carre[3][3]
    c = carre[3][0] + carre[2][1] + carre[1][2] + carre[0][3]
    if c != l:
        return -1
    else:
        return l


def estNormal(carre):
    s = []
    n = len(carre)
    for i in range(n):
        for j in range(n):
            x = carre[i][j]
            if not 1 <= x <= n**2
                return False
            s.append(x)




