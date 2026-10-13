import tkinter as tk

from objets import Raquette, Balle, Brique


class Jeu:

    def __init__(self):

        self.fenetre = tk.Tk()
        self.fenetre.title("Jeu du casse brique")
        self.fenetre.geometry("1200x700")

        self.canvas = tk.Canvas( self.fenetre, width=1200, height=600, bg="black" )

        self.canvas.pack()

        self.raquette = Raquette(self.canvas)
        self.balle = Balle(self.canvas, self.raquette)

        self.briques = []
        for j in range(30, 160, 40):
            for i in range(25, 1150, 115):
                brique = Brique(self.canvas, i, j)
                self.briques.append(brique)

        self.fenetre.bind( "<KeyPress>", self.deplacer_raquette )

        self.deplacer_balle()

    def deplacer_raquette(self, event):
        self.raquette.deplacer(event.keysym)

    def deplacer_balle(self):

        self.balle.deplacer(self.briques)

        self.fenetre.after( 30, self.deplacer_balle )
