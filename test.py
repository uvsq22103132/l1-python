import tkinter as tk

LARGEUR = 600
HAUTEUR = 400
cpt = 0
def creer_balle(cercle=0,dx=3,dy=5,x=300,y=200):
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),
                                (x+rayon, y+rayon),
                                fill="red")
    return [cercle, dx, dy, x, y]

def creer_carré(carré, dx, dy, x, y):
    coté = 20
    carré = canvas.create_rectangle((x-coté, y-coté),
                                (x+coté, y+coté),
                                fill="orange")
    return [carré, dx, dy, x, y]


def mouvement():
    move = [creer_balle, creer_carré]
    global balle
    global cpt
    rebond()
    if cpt <= 4:
        canvas.move(balle[0], balle[1], balle[2])
        balle[3] += balle[1]
        balle[4] += balle[2]
        canvas.after(10, mouvement)
    elif 5 <= cpt <30:
        if cpt%5 == 0:
            canvas.delete(balle[0])
            balle = move[(cpt//5)%2]( balle[0], balle[1], balle[2], balle[3], balle[4])
        canvas.move(balle[0], balle[1], balle[2])
        balle[3] += balle[1]
        balle[4] += balle[2]
        canvas.after(10, mouvement)

def rebond():
    global cpt
    global balle
    x0, y0, x1, y1 = canvas.coords(balle[0])
    if x0 <= 0 or x1 >= LARGEUR:
        balle[1] = -balle[1]
        cpt += 1
    elif  y0 <= 0 or y1 >= HAUTEUR:
        balle[2] = -balle[2]
        cpt += 1

racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=LARGEUR, height=HAUTEUR)
canvas.grid()

balle = creer_balle()


mouvement()

racine.mainloop()