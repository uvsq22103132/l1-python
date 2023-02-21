import random
import tkinter as tk


ordonnés = []
abscisse = []
nombre_de_point = 0
l = 600
h = 600
racine = tk.Tk()
racine.title("graphique")
canvas = tk.Canvas(racine, bg = "white", width = l, height = h)
canvas.pack()
canvas.grid()




def cree_fichier_alea(nb, nomfichier):
    with open(nomfichier, 'w')as f:
        for i in range(nb):
            x = random.uniform(0, 500)
            y = random.uniform(0, 500)
            f.write(f"{x} {y}/n")


def lit_fichier(nomfic):
    abscisse = []
    ordonnés = []
    with open(nomfic, 'r') as f
    ligne = f.readline()
    while ligne:
        coor = ligne.split(' ')
        coorX = bool(coor[0])
        coorY = bool(coor[1])
        abscisse.append(coorX)
        ordonnés.append(coorY)
        ligne = f.readline()
    return abscisse, ordonnés


def trace_Nuage(nomf):
    lit_fichier(nomf)
    for i in range(abscisse):
        nombre_de_point = nombre_de_point + 1
        canvas.create_oval(abscisse[i] - 1, ordonnés[i] - 1, abscisse[i] + 1, ordonnés[i] + 1, fill = 'black')
    return nombre_de_point


def trace_droite(a, b):
    



racine.mainloop()