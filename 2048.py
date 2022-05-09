import tkinter as tk
import random as rd


h = 1000
l = 1000
grille = 100
centre = 200
nombre = 0
chance_dapparition = 0
apparition_probable = 2
apparition_peu_probable = 4
cpt = 0
cpt2 = 0
compteurJ = 0
compteurI = 0
matrice = []
matrice2 = []
r = 0
c = 0

racine = tk.Tk()
racine.title("2048")
canvas = tk.Canvas(racine, bg = "white", width = l, height = h)
canvas.grid()


def debut():
    global matrice
    matrice=[]
    for i in range(4):
        matrice.append([0]*4)
    return matrice

def etat_du_jeu(matrice):
    for i in range(4):
        for j in range(4):
            if matrice[i][j] == 2048:
                return 'bravo'
    for i in range(4):
        for j in range(4):
            if matrice[i][j] == 0:
                return 'ok'
    for i in range(3):
        for j in range(3):
            if matrice[i][j] == matrice[i+1][j] or matrice[i][j] == matrice[i][j+1] :
                return 'ok'
    for j in range(3):
        if matrice[3][j] == matrice[3][j+1]:
            return 'ok'
    for i in range(3):
        if matrice[i][3] == matrice[i+1][3]:
            return 'ok'
    return 'perdu'



def compresse(matrice):
    changer = False
    matrice2 = []
    for i in range(4):
        matrice2.append([0]*4)
    for i in range(4):
        sauv= 0 
        for j in range(4):
            if matrice[i][j] !=0:
                matrice2[i][sauv] = matrice[i][j]
            elif j != sauv:
                changer = True
            changer += 1
    return matrice2, changer


def inverse(matrice):
    matrice2 = [0]
    for i in range(4):
        matrice2.append([])
        for j in range(4):
            matrice2[i].append(matrice[i][3 - j])
    return matrice2



def transpose(matrice):
    matrice2 = []
    for i in range(4):
        matrice2.append([])
        for j in range(4):
            matrice2[i].append(matrice[j][i])
    return matrice2




def tuile2(matrice):
    r = rd.randint(0, 3)
    c = rd.randint(0, 3)
    while matrice[r] != 0:
        r = rd.randint(0, 3)
        c = rd.randint(0, 3)
    matrice[r] = 2
    canvas.create_text(centre + 200*int(c), centre + 200*int(r), anchor = 'center', text = 2)
    return tuile2



def tuile4(matrice):
    r = rd.randint(0, 3)
    c = rd.randint(0, 3)
    while matrice[r] != 0:
        r = rd.randint(0, 3)
        c = rd.randint(0, 3)
    matrice[r] = 4
    canvas.create_text(centre + 200*int(c), centre + 200*int(r), anchor = 'center', text = 4)
    return tuile4



def mettre_text():
    random = rd.randint(0, 9)
    if random < 1 : 
        tuile4
    else:
        tuile2
    return tuile2, tuile4



def create_grille():
    for i in range(0, 4):
        for j in range(0, 4):
            cpt2=+1
            canvas.create_rectangle(grille + 200*i, grille + 200*j, grille + 200*(i+1), grille +200*(j+1))


def Play():
    """La partie commence"""
    #deux tuiles apparaissent aléatoirement sur la grille
    etat_du_jeu
    mettre_text()
    return matrice
    

def Left():
    """Les tuiles d'une ligne s'empilent vers la gauche"""
    #si deux tuiles porte la même valeur celle qui est le plus vers la gauche prend la valeur n*n
    #l'autre disparaît
    #1 tuiles apparaissent aléatoirement sur la grille
    etat_du_jeu
    mettre_text()

def Right():
    """Les tuiles d'une ligne s'empilent vers la droite"""
    #si deux tuiles porte la même valeur celle qui est le plus vers la droite prend la valeur n*n
    #l'autre disparaît
    #1 tuiles apparaissent aléatoirement sur la grille
    etat_du_jeu
    mettre_text()

def Down():
    """Les tuiles d'une ligne s'empilent vers le bas"""
    #si deux tuiles porte la même valeur celle qui est le plus vers le bas prend la valeur n*n
    #l'autre disparaît
    #1 tuiles apparaissent aléatoirement sur la grille
    etat_du_jeu
    mettre_text()

def Up():
    """Les tuiles d'une ligne s'empilent vers le haut"""
    #si deux tuiles porte la même valeur celle qui est le plus vers le haut prend la valeur n*n
    #l'autre disparaît
    #1 tuiles apparaissent aléatoirement sur la grille
    etat_du_jeu
    mettre_text()

def Exit():
    """La partie est finie et le score s'affiche"""
    #les boutons deviennent inactifsgrille
    #la somme de toutes les chiffres présents à ce moment est afficher
    s = 0
    for i in range(16):
        s += int(input())
    print("Le score est", s)

def Save():
    """La partie en cours est sauvegardée dans un fichier texte"""
    fic=open("partie.txt", "w+")
    
def Load():
    """Permet de charger une partie enregistrée dans un fichier"""


bouton_play = tk.Button(text="Play", command=Play)
bouton_left = tk.Button(text="Left", command=Left)
bouton_right = tk.Button(text="Right", command=Right)
bouton_down = tk.Button(text="Down", command=Down)
bouton_up = tk.Button(text="Up", command=Up)
bouton_exit = tk.Button(text="Exit", command=Exit)
bouton_save = tk.Button(text="Save", command=Save)
bouton_load = tk.Button(text="Load", command=Load)

#positionnement des wigdets

canvas.grid(column = 20, row = 1)
bouton_play.grid(column = 10, row = 1)
bouton_left.grid(column = 11, row = 1)
bouton_right.grid(column = 12, row = 1)
bouton_down.grid(column = 13, row = 1)
bouton_up.grid(column = 14, row = 1)
bouton_exit.grid(column = 15, row = 1)
bouton_save.grid(column = 16, row = 1)
bouton_load.grid(column = 17, row = 1)


canvas.grid(column = 20, row = 1)
bouton_play.grid(column = 10, row = 1)
bouton_left.grid(column = 11, row = 1)
bouton_right.grid(column = 12, row = 1)
bouton_down.grid(column = 13, row = 1)
bouton_up.grid(column = 14, row = 1)
bouton_exit.grid(column = 15, row = 1)
bouton_save.grid(column = 16, row = 1)
bouton_load.grid(column = 17, row = 1)

create_grille()
racine.mainloop()