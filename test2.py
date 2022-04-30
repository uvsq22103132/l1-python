import tkinter as tk

##################
# Constantes

LARGEUR = 600
HAUTEUR = 400
cpt = 0

###################
# Fonctions

def creer_balle():
    """Dessine un disque bleu et retourne son identifiant
     et les valeurs de déplacements dans une liste"""
    global cercle
    dx, dy = 3, 5
    return [cercle, dx, dy]


def mouvement():
    """Déplace la balle et ré-appelle la fonction avec un compte-à-rebours(j'ai augmenter la vitesse c'était un peu lent"""
    global cpt
    if cpt < 30:
        rebond()
        canvas.move(balle[0], balle[1], balle[2])
        canvas.after(10, mouvement)


def rebond():
    """Fait rebondir la balle sur les bords du canevas et change de couleur la balle"""
    global balle, cpt, cercle
    x0, y0, x1, y1 = canvas.coords(balle[0])
    if x0 <= 0:
        balle[1] = -balle[1]
        canvas.itemconfig(cercle, fill="yellow")
        cpt += 1
    elif x1 >= 600:
        balle[1] = -balle[1]
        canvas.itemconfig(cercle, fill="green")
        cpt += 1
    elif y0 <= 0:
        balle[2] = -balle[2]
        canvas.itemconfig(cercle, fill="red")
        cpt += 1
    elif y1 >= 400:
        balle[2] = -balle[2]
        canvas.itemconfig(cercle, fill="blue")
        cpt += 1

######################
# programme principal

# création des widgets
racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=LARGEUR, height=HAUTEUR)
canvas.grid()

""""décidé de définir cercle ici sinon ça marche pas D;"""
x, y = LARGEUR // 2, HAUTEUR // 2
rayon = 20
cercle = canvas.create_oval((x-rayon, y-rayon),
                                (x+rayon, y+rayon),
                                fill="blue")
"""création des bandes de couleurs sur les rebords pour indiquer de quelle couleur la balle change"""
canvas.create_rectangle(0, 395, 600, 400, fill="blue")
canvas.create_rectangle(0, 0, 600, 5, fill="red")
canvas.create_rectangle(0, 400, 5, 0, fill="yellow")
canvas.create_rectangle(595, 0, 600, 400, fill="green")

# initialisation de la balle
balle = creer_balle()

# déplacement de la balle
mouvement()

# boucle principale
racine.mainloop()
