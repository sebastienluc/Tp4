'''
Sebastien Luc et Mario Courtial
Le 13/10/2026
TP4
to do : avancer sur le tp 
'''

import tkinter as tk
import random

class Raquette:

    def __init__(self, canvas):

        #création de la raquette et la placer sur le canvas
        self.canvas = canvas

        self.x = 565
        self.y = 450

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
            300,
            610,
            320,
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

        return self.collision_murs()



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
            return False # la balle a touché le bas 

        return True # la balle est encore en jeu 

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
                return True 
        return False

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

        self.score = 0
        self.vies = 3
        
        self.fenetre_jeu.focus_force()

        #barre de stats
        self.frame_stats = tk.Frame(self.fenetre_jeu, bg="#eeeeee", height=50)
        self.frame_stats.pack(fill="x", side="top")

        self.label_vie = tk.Label(self.frame_stats,
            text=f"Vies : {self.vies}",   
            font=("Helvetica", 20),
            bg="#eeeeee"
        )
        self.label_vie.pack(side="left", padx=30, pady=10)

        self.label_score = tk.Label(self.frame_stats, 
            text=f"Score : {self.score}",
            font=("Helvetica", 20),
            bg="#eeeeee"
        )
        self.label_score.pack(side="right", padx=30, pady=10)


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


        #mise en place du canvas sur la fenêtre de jeu
        self.canvas = tk.Canvas(
            self.fenetre_jeu,
            width=1200,
            height=500,
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

        # On récupère le statut de la balle (True si en l'air, False si tombée)
        balle_en_jeu = self.balle.deplacer()

        if not balle_en_jeu:
            self.vies -= 1
            self.label_vie.config(text=f"Vies : {self.vies}")
            
            if self.vies <= 0:
                # Défaite s'il reste des briques
                if len(self.briques) > 0:
                    self.en_cours = False
                    self.canvas.create_text(
                        600, 250,
                        text="DÉFAITE !\nVous n'avez plus de vies.",
                        fill="red",
                        font=("Helvetica", 36, "bold"),
                        justify="center"
                    )
                return
            else:
                # Il reste des vies : On replace la balle au milieu
                self.canvas.coords(self.balle.objet, 590, 400, 610, 420)
                self.balle.dy = -5
                self.balle.dx = random.choice([-5, 5])

        self.balle.collision_raquette(self.raquette)

        # Si une brique est touchée, on met à jour le score
        if self.balle.collision_briques(self.briques):
            self.score += 10
            self.label_score.config(text=f"Score : {self.score}")

        #Détection des briques placées au bon endroit 
        if self.balle.collision_briques(self.briques):
            self.score += 10
            self.label_score.config(text=f"Score : {self.score}")

        # S'il reste des vies et toutes les briques sont détruites, on affiche "victoire"
        if len(self.briques) == 0:
                self.en_cours = False
                self.canvas.create_text(
                    600, 250,
                    text=f"VICTOIRE !\nScore final : {self.score}",
                    fill="yellow",
                    font=("Helvetica", 36, "bold"),
                    justify="center"
                )
                return
        
        self.fenetre_jeu.after(
            30,
            self.deplacer_balle
        )

jeu = Casse_brique()