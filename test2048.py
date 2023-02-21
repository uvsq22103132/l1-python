
import tkinter as tk 
import random

from matplotlib.pyplot import text

h = 1000
l = 1000
grille = 100
zero_alea = 0
jeu = 0
rand = 0
centre = 200
matrice = [[0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0]]
somme = 0


def creer_matrice():
    for i in range(4):
        matrice.append([0]*4)
    return matrice


def Play():
    """La partie commence"""
    #deux tuiles apparaissent aléatoirement sur la grille
    global matrice
    rand = random.randint(0, 9)
    for i in range(2):
        if rand < 1:
            rand1 = random.randint(0, 3)
            rand2 = random.randint(0, 3)
            matrice[rand1][rand2] = 4
        else :
            rand1 = random.randint(0, 3)
            rand2 = random.randint(0, 3)
            matrice[rand1][rand2] = 2

    create_grille()
    etat_du_jeu
    return matrice



def etat_du_jeu(matrice):
    global jeu
    for i in range(4):
        for j in range(4):
            if matrice[i][j] == 2048:
                jeu = True
                return 'bravo'
    for i in range(4):
        for j in range(4):
            if matrice[i][j] == 0:
                generation_alea(matrice)
                jeu == True
                return 'ok'
    for i in range(3):
        for j in range(3):
            if matrice[i][j] == matrice[i+1][j] or matrice[i][j] == matrice[i][j+1] :
                generation_alea(matrice)
                jeu == True
                return 'ok'
    for j in range(3):
        if matrice[3][j] == matrice[3][j+1]:
            generation_alea(matrice)
            jeu ==True
            return 'ok'
    for i in range(3):
        if matrice[i][3] == matrice[i+1][3]:
            generation_alea(matrice)
            jeu == True
            return 'ok'
    if matrice[i][j] != 2048 and matrice[i][j] != 0 and matrice[i][j] != matrice[i+1][j] or matrice[i][j] != matrice[i][j+1] and matrice[3][j] != matrice[3][j+1] and matrice[i][3] != matrice[i+1][3]:
        jeu == False
    else : 
        jeu == True


def generation_alea(matrice):
    rand = random.randint(0,9)
    if rand < 1:
        rand1 = random.randint(0, 3)
        rand2 = random.randint(0, 3)
        while matrice[rand1][rand2] != 0:
            rand1 = random.randint(0, 3)
            rand2 = random.randint(0, 3)
        matrice[rand1][rand2] = 4
    elif rand > 1 :
        rand1 = random.randint(0, 3)
        rand2 = random.randint(0, 3)
        while matrice[rand1][rand2] != 0:
            rand1 = random.randint(0, 3)
            rand2 = random.randint(0, 3)
        matrice[rand1][rand2] = 2


def generation_de_text(matrice):
    for r in range(0, 4):
        for c in range(0, 4):
            if matrice[r][c] == 0 :
                canvas.create_text(centre + 200*int(r), centre + 200*int(c), anchor='center', text='')
            elif matrice[r][c] == 2 : 
                canvas.create_text(centre + 200*int(r), centre + 200*int(c), anchor='center', text=2)
            elif matrice[r][c] == 4 :
                canvas.create_text(centre + 200*int(r), centre + 200*int(c), anchor='center', text=4)
            elif matrice[r][c] == 8 :
                canvas.create_text(centre + 200*int(r), centre + 200*int(c), anchor='center', text=8)
            elif matrice[r][c] == 16 :
                canvas.create_text(centre + 200*int(r), centre + 200*int(c), anchor='center', text=16)
            elif matrice[r][c] == 32 :
                canvas.create_text(centre + 200*int(r), centre + 200*int(c), anchor='center', text=32)
            elif matrice[r][c] == 64 :
                canvas.create_text(centre + 200*int(r), centre + 200*int(c), anchor='center', text=64)
            elif matrice[r][c] == 128 :
                canvas.create_text(centre + 200*int(r), centre + 200*int(c), anchor='center', text=128)
            elif matrice[r][c] == 256 :
                canvas.create_text(centre + 200*int(r), centre + 200*int(c), anchor='center', text=256)
            elif matrice[r][c] == 512 :
                canvas.create_text(centre + 200*int(r), centre + 200*int(c), anchor='center', text=512)
            elif matrice[r][c] == 1024 :
                canvas.create_text(centre + 200*int(r), centre + 200*int(c), anchor='center', text=1024)
            elif matrice[r][c] == 2048 :
                canvas.create_text(centre + 200*int(r), centre + 200*int(c), anchor='center', text=2048)




def Left():
    global matrice, canvas
    canvas.delete(generation_de_text)
    for r in range(4):
        while 0 in matrice[r]:
            matrice[r].remove(0)
        while len(matrice[r]) != 4:
            matrice[r].append(0)
    for r in range(4):
        for c in range(3):
            if matrice[r][c] == matrice[r][c + 1] and matrice[r][c] != 0:
                matrice[r][c] = 2 * matrice[r][c]
                matrice[r][c + 1] = 0
    etat_du_jeu(matrice)
    generation_de_text(matrice)
    print(matrice)
        



def Right():
    global matrice, canvas
    canvas.delete(generation_de_text)
    for r in range(4):
        while 0 in matrice[r]:
            matrice[r].remove(0)
        while len(matrice[r]) != 4:
            matrice[r].insert(-1, 0)
    for r in range(4):
        for c in range(3):
            if matrice[r][c] == matrice[r][c - 1] and matrice[r][c] != 0:
                matrice[r][c] = 2 * matrice[r][c]
                matrice[r][c - 1] = 0
    etat_du_jeu(matrice)
    generation_de_text(matrice)
    print(matrice)


def Up():
    global matrice, canvas
    for c in range(4):
        for r in range(4):
            while 0 in matrice[c]:
                matrice[c].remove(0)
            while len(matrice[c]) !=4:
                matrice[c].insert(r, 0)
    for c in range(4):
        for r in range(3):
            if matrice[r][c] == matrice[r + 1][c] and matrice[r][c] != 0:
                matrice[r][c] = 2 * matrice[r][c]
                matrice[r + 1][c] = 0
    etat_du_jeu(matrice) 
    generation_de_text(matrice)
    print(matrice)


def Down():
    global matrice, canvas
    for c in range(4): 
        for r in range(4):
            while 0 in matrice[c]:
                matrice[c].remove(0)
            while len(matrice[c]) != 4:
                matrice[c].insert(r, 0)
    for c in range(4):
        for r in range(3):
            if matrice[r][c] == matrice[r - 1][c] and matrice[r][c] != 0:
                matrice[r][c] = 2 * matrice[r][c]
                matrice[r - 1][c] = 0
    etat_du_jeu(matrice)
    generation_de_text(matrice)
    print(matrice)


def Exit():
    global somme
    """La partie est finie et le score s'affiche"""
    #les boutons deviennent inactifsgrille
    #la somme de toutes les chiffres présents à ce moment est afficher
    for r in range(0, 3):
        for c in range(0, 3):
            somme += matrice[r][c]
    
    print("Le score est", somme)


def Save():
    """La partie en cours est sauvegardée dans un fichier texte"""
    fic=open("partie.txt", "w+")


def Load():
    """Permet de charger une partie enregistrée dans un fichier"""


def create_grille():
    for i in range(0, 4):
        for j in range(0, 4):
            canvas.create_rectangle(grille + 200*i, grille + 200*j, grille + 200*(i+1), grille +200*(j+1))
            




racine = tk.Tk()
racine.title("2048")
canvas = tk.Canvas(racine, bg = "white", width = l, height = h)
canvas.grid()

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


racine.mainloop()
print(matrice)