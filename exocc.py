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




racine = tk.Tk()
racine.title("2048")
canvas = tk.Canvas(racine, bg = "white", width = l, height = h)
canvas.grid()

def tuile():
    random = rd.randint(0,9)
    cpt =+ 1
    if random < 1 :
        canvas.create_text(centre + 200*rd.randint(0,3), centre + 200*rd.randint(0,3), anchor ='center', text = 4)
    else:
        canvas.create_text(centre + 200*rd.randint(0,3), centre + 200*rd.randint(0,3), anchor ='center', text = 2)







def create_grille():
    for i in range(0, 4):
        for j in range(0, 4):
            cpt2=+1
            canvas.create_rectangle(grille + 200*i, grille + 200*j, grille + 200*(i+1), grille +200*(j+1))





canvas.bind('p', tuile)






create_grille()
racine.mainloop()