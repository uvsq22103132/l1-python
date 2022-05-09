from audioop import reverse
import tkinter as tk
import random

from numpy import true_divide

def start_game():
    grille=[]
    for i in range(4):
        grille.append([0]*4)
    return grille


def tuile2(grille):
    r = random.randint(0, 3)
    c = random.randint(0, 3)
    while grille[r] != 0:
        r = random.randint(0, 3)
        c = random.randint(0, 3)
    grille[r] = 2


def tuile4(grille):
    r = random.randint(0, 3)
    c = random.randint(0, 3)
    while grille[r] != 0:
        r = random.randint(0, 3)
        c = random.randint(0, 3)
    grille[r] = 4



def resultat(grille):
    for i in range(4):
        for j in range(4):
            if grille[i][j] == 2048:
                return 'bravo'
    for i in range(4):
        for j in range(4):
            if grille[i][j] == 0:
                return 'ok'
    for i in range(3):
        for j in range(3):
            if grille[i][j] == grille[i+1][j] or grille[i][j] == grille[i][j+1] :
                return 'ok'
    for j in range(3):
        if grille[3][j] == grille[3][j+1]:
            return 'ok'
    for i in range(3):
        if grille[i][3] == grille[i+1][3]:
            return 'ok'
    return 'perdu'


def compresser(matrice):
    changer = False
    matrice2 = []
    for i in range(4):
        matrice2.append([0]*4)
    for i in range(4):
        sauv= 0 
        for j in range(4):
            if matrice[i][j] !=0:
                matrice2[i][sauv] = matrice[i][j]
            if j != sauv:
                changer = True
            changer += 1
    return matrice2, changer


def fusion(grille):
    changer = False
    for i in range(4):
        for j in range(3):
            if grille[i][j] == grille[i][j+1] and grille[i][j] != 0:
                grille[i][j] = grille[i][j]*2
                grille[i][j + 1] = 0
                changer = True
    return grille, changer


def inverse(grille):
    grille2 = [0]
    for i in range(4):
        grille2.append([])
        for j in range(4):
            grille2[i].append(grille[i][3 - j])
    return grille


def transpose(grille):
    grille2 = []
    for i in range(4):
        grille2.append([])
        for j in range(4):
            grille2[i].append(grille[j][i])


def left(grid):
    grid2, changer2 = compresser(grid)
    grid2, changer3 = fusion(grid2)
    changer = changer2 or changer3
    grid2, temp = compresser(grid2)
    return grid2, changer


def right(grid):
    grid2 = inverse(grid)
    grid2, changer = left(grid2)
    grid2 = inverse(grid2)
    return grid2, changer


def up(grid):
    grid2 = transpose(grid)
    grid2 , changer = left(grid2)
    grid2 = transpose(grid2)
    return grid2, changer


def down(grid):
    grid2 = transpose(grid)
    grid2 , changer = right(grid2)
    grid2 = transpose(grid2)
    return grid2, changer