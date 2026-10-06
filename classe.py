import tkinter as tk
import random


class Raquette:

    def __init__(self, canvas):

        self.canvas = canvas

        self.x = 565
        self.y = 550

        self.objet = canvas.create_rectangle(
            self.x,
            self.y,
            self.x + 70,
            self.y + 10,
            fill="blue",
            tags="raquette"
        )

    def deplacer(self, direction):

        if direction == "Left":
            self.x -= 10

        elif direction == "Right":
            self.x += 10

        if self.x < 0:
            self.x = 0

        if self.x > 1130:
            self.x = 1130

        self.canvas.coords(
            self.objet,
            self.x,
            self.y,
            self.x + 70,
            self.y + 10
        )


class Balle:

    def __init__(self, canvas):

        self.canvas = canvas

        self.objet = canvas.create_oval(
            590,
            400,
            610,
            420,
            fill="red",
            outline="red"
        )

        self.dx = random.choice([-5, 5])
        self.dy = -5

    def deplacer(self):

        self.canvas.move(
            self.objet,
            self.dx,
            self.dy
        )


class Jeu:

    def __init__(self):

        self.fenetre = tk.Tk()
        self.fenetre.title("Jeu du casse brique")
        self.fenetre.geometry("1200x700")

        self.canvas = tk.Canvas(
            self.fenetre,
            width=1200,
            height=600,
            bg="black"
        )

        self.canvas.pack()

        self.raquette = Raquette(self.canvas)
        self.balle = Balle(self.canvas)

        self.fenetre.bind(
            "<KeyPress>",
            self.deplacer_raquette
        )

        self.deplacer_balle()

    def deplacer_raquette(self, event):
        self.raquette.deplacer(event.keysym)

    def deplacer_balle(self):

        self.balle.deplacer()

        self.fenetre.after(
            30,
            self.deplacer_balle
        )


jeu = Jeu()
jeu.fenetre.mainloop()
