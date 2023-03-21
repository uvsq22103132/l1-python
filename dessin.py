import tkinter as tk


H = 500
L = 500


racine = tk.Tk()
racine.title('fenetre')
b1 = tk.Button(racine)
b2 = tk.Button(racine)
b3 = tk.Button(racine)
b4 = tk.Button(racine)
canvas = tk.Canvas(racine,height = H, width = L, bg = 'black')
canvas.grid()
racine.mainloop()