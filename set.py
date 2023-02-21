import random as rd
liste = [3,5,1,1,7,8,7,1,2,3,0,7,8,9]
liste2 = [3,2,1,8]


def effectifs(liste):
    effectifs = []
    for i in range(10):
        effectifs.append(liste.count(i))
    return effectifs




def somme_entier(n):
    listepremier = []
    s = 0
    for i in range(1, n + 1):
        s += i
        listepremier.append(s)
    return listepremier





def impairs(liste):
    listeimpaire = []
    listepaire = []
    for i in range(len(liste)):
        if liste[i] % 2 != 0:
            listeimpaire.append(liste[i])
        else:
            listepaire.append(liste[i])
    return listeimpaire





def produit_liste(liste):
    p = 1
    for i in range(len(liste)):
        p *= liste[i]

    return p




matrice1 = [[2, 3],[4, 8]]


def produit_matrice(matrice):
    p = 1
    for i in range(len(matrice1[0])):
        for j in range(len(matrice1[0])):
            p *= matrice[i][j]
    return p





def creermatrice():
    matrice2 = []
    place = rd.randint(0,3)
    place1 = rd.randint(0,4)
    place2 = place + 1
    for i in range(5):
        matrice2.append([0,0,0,0,0])
    matrice2[place][place1] = 1
    matrice2[place2][place1] = 1
    return matrice2


def triangle(n):
    for i in range(1 , n+1):
        print(' ' * i - 1 ,'X' , ' ' * i - 1)
    return triangle



def liste_entier(liste, entier):
    listegrande = []
    for i in range(len(liste)):
        if liste[i] > entier:
            listegrande.append(liste[i])
    return listegrande




def contage_de_lettre(phrase):
    liste_contage = []
    se = set(phrase)
    for i in se:
        liste_contage.append(i)
        liste_contage.append(phrase.count(i))
    return liste_contage

phrase = 'qlkjfgqmfdljbdfonjiqrtnîjrnsfjnlogj'
print(contage_de_lettre(phrase))