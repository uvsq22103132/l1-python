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
    x, y = LARGEUR // 2, HAUTEUR // 2
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),
                                (x+rayon, y+rayon),
                                fill="blue")
    return [cercle, dx, dy]


def mouvement():
    """Déplace la balle et ré-appelle la fonction avec un compte-à-rebours(j'ai augmenter la vitesse c'était un peu lent"""
    global cpt
    if cpt < 30:
        rebond()
        canvas.move(ligne[0], 1, 0)
        ligne[1] = ligne[1]+1
        canvas.move(ligne2[0], 1, 0)
        ligne2[1] = ligne[1] + 1
        canvas.move(balle[0], balle[1], balle[2])
        canvas.after(5, mouvement)



def creer_ligne1():
    """dessine une ligne blanche"""
    x, y = 1, 0
    ligne = canvas.create_line(HAUTEUR, x, HAUTEUR, HAUTEUR , fill="white")
    
    return [ligne, x]


def creer_ligne2():
    """dessine une seconde ligne blanche"""
    x, y = 1, 0
    ligne = canvas.create_line(y, HAUTEUR, HAUTEUR, HAUTEUR)




def rebond():
    """Fait rebondir la balle sur les bords du canevas"""
    global balle, cpt
    x0, y0, x1, y1 = canvas.coords(balle[0])
    if cpt < 30:
        if x0 <= 0 or x1 >= 600:
            balle[1] = -balle[1]
            cpt += 1
        if y0 <= 0 or y1 >= 400:
            balle[2] = -balle[2]
            cpt =+ 1


######################
# programme principal

# création des widgets
racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=LARGEUR, height=HAUTEUR)
canvas.grid()

# initialisation de la balle avec la ligne 
balle = creer_balle()
ligne = creer_ligne1()
ligne2 = creer_ligne2()
# déplacement de la balle
mouvement()

# boucle principale
racine.mainloop()