import random
import tkinter as tk


ordonnés = []
abscisse = []
nombre_de_point = 0
L = 600
H = 600
racine = tk.Tk()
racine.title("graphique")
canvas = tk.Canvas(racine, bg="white", width=L, height=H)
canvas.pack()
canvas.grid()


def cree_fichier_alea(nb, nomfichier):
    with open(nomfichier, 'w')as f:
        for i in range(nb):
            x = random.uniform(0, 500)
            y = random.uniform(0, 500)
            f.write(f"{x} {y}\n")


def lit_fichier(nomfic):
    abscisse = []
    ordonnés = []
    with open(nomfic, 'r') as f:
        ligne = f.readline()
        while ligne:
            x, y = ligne.split(' ')
            abscisse.append(float(x))
            ordonnés.append(float(y))
            ligne = f.readline()
    return abscisse, ordonnés


def trace_Nuage(nomf):
    abscisse, ordonnés = lit_fichier(nomf)
    nombre_de_point = len(abscisse)
    for i in range(len(abscisse)):
        canvas.create_oval(abscisse[i] - 1, ordonnés[i] - 1, abscisse[i] + 1, ordonnés[i] + 1, fill='black')
    print(nombre_de_point)



cree_fichier_alea(5, 'teststat')
lit_fichier('teststat')
trace_Nuage('teststat')
racine.mainloop()
