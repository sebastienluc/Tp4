import tkinter as tk
import random


class Raquette:

    def __init__(self, canvas):

        self.canvas = canvas

        self.x = 565
        self.y = 550

        self.objet = canvas.create_rectangle( self.x, self.y, self.x + 70, self.y + 10, fill="blue", tags="raquette" )

    def deplacer(self, direction):

        if direction == "Left":
            self.x -= 10

        elif direction == "Right":
            self.x += 10

        if self.x < 0:
            self.x = 0

        if self.x > 1130:
            self.x = 1130

        self.canvas.coords( self.objet, self.x, self.y, self.x + 70, self.y + 10 )


class Balle:

    def __init__(self, canvas, raquette):
        self.canvas = canvas
        self.raquette = raquette

        self.objet = canvas.create_oval( 590, 400, 610, 420, fill="red", outline="red" )

        self.dx = random.choice([-5, 5])
        self.dy = -5

    def deplacer(self):

        self.canvas.move( self.objet, self.dx, self.dy )
        self.colision_murs()
        self.colision_raquette(self.raquette)


    def colision_murs(self):

        x1, y1, x2, y2 = self.canvas.coords( self.objet )

        if x1 <= 0:
            self.dx = 5

        if x2 >= 1200:
            self.dx = -5

        if y1 <= 0:
            self.dy = 5

        if y2 >= 600:
            self.canvas.master.destroy()

    def colision_raquette(self, raquette):

        x1, y1, x2, y2 = self.canvas.coords( self.objet )
        rx1, ry1, rx2, ry2 = self.canvas.coords( raquette.objet )

        if x2 >= rx1 and x1 <= rx2 and y2 >= ry1 and y1 <= ry2:
            self.dy = -5


class Jeu:

    def __init__(self):

        self.fenetre = tk.Tk()
        self.fenetre.title("Jeu du casse brique")
        self.fenetre.geometry("1200x700")

        self.canvas = tk.Canvas( self.fenetre, width=1200, height=600, bg="black" )

        self.canvas.pack()

        self.raquette = Raquette(self.canvas)
        self.balle = Balle(self.canvas, self.raquette)

        self.fenetre.bind( "<KeyPress>", self.deplacer_raquette )

        self.deplacer_balle()

    def deplacer_raquette(self, event):
        self.raquette.deplacer(event.keysym)

    def deplacer_balle(self):

        self.balle.deplacer()

        self.fenetre.after( 30, self.deplacer_balle )


jeu = Jeu()
jeu.fenetre.mainloop()
