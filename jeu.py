import tkinter as tk
import random
from objets import Raquette, Balle, Brique, Brique_dur


class Jeu:

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

        # Bouton pour lancer le niveau 1
        BoutonNiveau1 = tk.Button(
            self.fenetre_accueil,
            text="Niveau 1",
            command=lambda: self.lancer_le_jeu(1),
            font=("Helvetica", 18),
            width=15
        )
        BoutonNiveau1.pack(pady=15)

        # Bouton pour lancer le niveau 2
        BoutonNiveau2 = tk.Button(
            self.fenetre_accueil,
            text="Niveau 2",
            command=lambda: self.lancer_le_jeu(2),
            font=("Helvetica", 18),
            width=15
        )
        BoutonNiveau2.pack(pady=15)

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

    def lancer_le_jeu(self, niveau):
        self.niveau = niveau

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

        if self.niveau == 1:
            classes_briques = [Brique]  # on met que des briques normales pour le niveau 1
        else:
            classes_briques = [Brique, Brique_dur]  # 50% de chance pour chaque classe

        for rangee in range(4):
            for col in range(12):
                x_pos = 15 + col * 98
                y_pos = 50 + rangee * 30
                ClasseChoisie = random.choice(classes_briques)  # 1. On choisit une classe au hasard (50% de chance pour chaque)
                nouvelle_brique = ClasseChoisie(self.canvas, x_pos, y_pos)  # 2. On instancie la brique choisie dynamiquement
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

        # Détecter une collision avec une brique
        if self.balle.collision_briques(self.briques):
            self.score += 10
            self.label_score.config(
                text=f"Score : {self.score}"
            )

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
