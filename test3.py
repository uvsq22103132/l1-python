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
    """Déplace la balle et ré-appelle la fonction avec un compte-à-rebours"""
    global cpt
    if cpt < 30:
        rebond()
        canvas.move(balle[0], balle[1], balle[2])
        canvas.after(10, mouvement)


def rebond():
    """Fait rebondir la balle sur les bords du canevas"""
    global balle, cpt, cercle
    x0, y0, x1, y1 = canvas.coords(balle[0])
    if x0 <= 0 or x1 >= 600:
        balle[1] = -balle[1]
        cpt += 1
    elif y0 <= 0 or y1 >= 400:
        balle[2] = -balle[2]
        cpt += 1
    elif x1 <= 150 and x0 >= 0 and y1 <= 50:
        canvas.itemconfig(cercle, fill="red")
    elif x1 <= 300 and x0 >= 150 and y1 <= 50:
        canvas.itemconfig(cercle, fill="green")
    elif x1 <= 450 and x0 >= 300 and y1 <= 50:
        canvas.itemconfig(cercle, fill="blue")
    elif x1 <= 600 and x0 >= 450 and y1 <= 50:
        canvas.itemconfig(cercle, fill="yellow")
    elif y1 >= 400:
        canvas.itemconfig(cercle, fill="white")
        """"la ligne du dessus sert a reset la couleur de la balle en blanc"""

######################
# programme principal

# création des widgets
racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=LARGEUR, height=HAUTEUR)
canvas.grid()

x, y = LARGEUR // 2, HAUTEUR // 2
rayon = 20
cercle = canvas.create_oval((x-rayon, y-rayon),
                                (x+rayon, y+rayon),
                                fill="blue")
""""sert a indiqué la couleur de la balle quand elle rentre dans le rectangle collé au plafon"""
canvas.create_rectangle(0, 0, 150, 50, fill="red")
canvas.create_rectangle(150, 0, 300, 50, fill="green")
canvas.create_rectangle(300, 0, 450, 50, fill="blue")
canvas.create_rectangle(450, 0, 600, 50, fill="yellow")
# initialisation de la balle
balle = creer_balle()
# déplacement de la balle
mouvement()
# boucle principale
racine.mainloop()