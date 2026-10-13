'''
Sebastien Luc et Mario Courtial
Le 13/10/2026
TP4
to do : avancer sur le tp 
'''

import tkinter as tk
from tkinter import messagebox
import random

class Raquette:

    def __init__(self, canvas):

        #création de la raquette et la placer sur le canvas
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

    #mise en place du système de déplacement de la raquette avec les touches gauche et droite 
    def deplacer(self, direction):

        if direction == "Left":
            self.x -= 10

        elif direction == "Right":
            self.x += 10

        #empêche la raquette de sortir du canvas
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

class Brique:

    def __init__(self, canvas, x, y):

        self.canvas = canvas
        self.objet = canvas.create_rectangle(
            x,
            y, 
            x + 90,
            y + 20,
            fill="green",
            outline="green",
            tags="brique"
        )

    def detruire(self):
        self.canvas.delete(self.objet)


class Balle:

    def __init__(self, canvas):

        #création de la balle et la placer sur le canvas
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

    #mise en place du système de déplacement de la balle
    def deplacer(self):

        self.canvas.move(
            self.objet,
            self.dx,
            self.dy
        )

        # On vérifie les collisions avec les murs à chaque déplacement
        self.collision_murs()


    #création de la physique de la balle pour qu'elle rebondisse sur les murs , la raquette et les briques 
    def collision_murs(self):

        x1, y1, x2, y2 = self.canvas.coords( self.objet )

        if x1 <= 0:
            self.dx = 5

        if x2 >= 1200:
            self.dx = -5

        if y1 <= 0:
            self.dy = 5

        if y2 >= 600:
            self.canvas.master.destroy()

    def collision_raquette(self, raquette):

        x1, y1, x2, y2 = self.canvas.coords( self.objet )
        rx1, ry1, rx2, ry2 = self.canvas.coords( raquette.objet )

        if x2 >= rx1 and x1 <= rx2 and y2 >= ry1 and y1 <= ry2:
            self.dy = -5

    def collision_briques(self, briques):

        x1, y1, x2, y2 = self.canvas.coords(self.objet)

        objets = self.canvas.find_overlapping(x1, y1, x2, y2)

        for brique in briques:

            if brique.objet in objets:

                # Détruire la brique
                brique.detruire()
                briques.remove(brique)

                # Faire rebondir la balle
                self.dy = -self.dy

                # Arrêter la recherche après une colision
                break

class Casse_brique:
    def __init__(self):
        
        #Créartion de la fenêtre d'accueil avant de lancer la partie
        self.fenetre_accueil = tk.Tk()
        self.fenetre_accueil.title("Casse-brique")
        self.fenetre_accueil.geometry('1200x700')

        #titre du jeu
        label_titre = tk.Label(self.fenetre_accueil,
            text="Casse-brique",
            font=("Helvetica", 35)
       )
        
        label_titre.pack(pady=100)

        #pour lancer la partie
        BoutonLancer = tk.Button(self.fenetre_accueil,
            text = "Start", 
            command = self.lancer_le_jeu,
            font=("Helvetica", 18)
        )
        
        BoutonLancer.pack(pady=100)

        #pour quitter le jeu
        BoutonQuitter = tk.Button(self.fenetre_accueil,
            text = "quitter", 
            fg = 'red', 
            command = self.fenetre_accueil.destroy, 
            font=("Helvetica", 18)
        )
        
        BoutonQuitter.pack(side = 'bottom',
            pady = 60
        )

        self.fenetre_accueil.mainloop()

    def lancer_le_jeu(self):

        #on ferme la fenetre d'accueil
        self.fenetre_accueil.destroy()

        #Création de la fenetre de jeu
        self.fenetre_jeu = tk.Tk()
        self.fenetre_jeu.title("Casse-brique")
        self.fenetre_jeu.geometry('1200x700')
        
        self.fenetre_jeu.focus_force()

        #pour quitter le jeu
        BoutonQuitter = tk.Button(self.fenetre_jeu,
            text = "quitter", 
            fg = 'red', 
            command = self.fenetre_jeu.destroy, 
            font=("Helvetica", 18)
        )

        BoutonQuitter.pack(
            side = 'bottom',
            pady = 20 
        )

        #on affiche le nombre de vies et le score 
        label_vie = tk.Label(self.fenetre_jeu,
            text="Vies : 3",   
            font=("Helvetica", 20)
        )

        label_vie.place(x=20,
            y=20,
            anchor="w"
        )

        label_score = tk.Label(self.fenetre_jeu, 
            text="Score : 0",
            font=("Helvetica", 20)
        )

        label_score.place(
            x=1180,
            y=20,
            anchor="e"
        )

        #mise en place du canvas sur la fenêtre de jeu
        self.canvas = tk.Canvas(
            self.fenetre_jeu,
            width=1200,
            height=600,
            bg="black"
        )

        self.canvas.pack()

        #mise en place de la raquette et de la balle sur le canvas
        self.raquette = Raquette(self.canvas)
        self.balle = Balle(self.canvas)

        self.briques = []
        # On crée 4 rangées de briques espacées proprement
        for rangee in range(4):
            for col in range(12):
                x_pos = 15 + col * 98
                y_pos = 50 + rangee * 30
                nouvelle_brique = Brique(self.canvas, x_pos, y_pos)
                self.briques.append(nouvelle_brique)


        #mise en place du système de déplacement de la raquette avec les touches gauche et droite
        self.fenetre_jeu.bind(
            "<Left>",
            lambda event: self.deplacer_raquette("Left")
        )
        self.fenetre_jeu.bind(
            "<Right>",
            lambda event: self.deplacer_raquette("Right")
        )

        self.deplacer_balle()
        self.fenetre_jeu.mainloop()


    #mise en place du système de déplacement de la raquette avec les touches gauche et droite 
    def deplacer_raquette(self, event):
        self.raquette.deplacer(event)

    def deplacer_balle(self):

        self.balle.deplacer()

        self.balle.collision_raquette(self.raquette)

        self.fenetre_jeu.after(
            30,
            self.deplacer_balle
        )

        # Si une brique est touchée, on met à jour le score
        if self.balle.collision_briques(self.briques):
            self.score += 10
            self.label_score.config(text=f"Score : {self.score}")



jeu = Casse_brique()