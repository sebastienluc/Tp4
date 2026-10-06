'''
Sebastien Luc et Mario Courtial
Le 06/10/2026
TP4
to do : commencer le tp 
'''

import tkinter as tk
from tkinter import messagebox

class Casse_brique:
    def __init__(self):
        
        #Creer la fenêtre d'accueil avant de lancer la partie
        self.fenetre_accueil = tk.Tk()
        self.fenetre_accueil.title("Casse-brique")
        self.fenetre_accueil.geometry('1200x700')

        #titre du jeu
        label_titre = tk.Label(self.fenetre_accueil, text="Casse-brique", font=("Helvetica", 35))
        label_titre.pack(pady=100)

        #pour lancer la partie
        BoutonLancer = tk.Button(self.fenetre_accueil, text = "Start", command = self.lancer_le_jeu, font=("Helvetica", 18))
        BoutonLancer.pack(pady=100)

        #pour quitter le jeu
        BoutonQuitter = tk.Button(self.fenetre_accueil, text = "quitter", fg = 'red', command = self.fenetre_accueil.destroy, font=("Helvetica", 18))
        BoutonQuitter.pack(side = 'bottom',pady = 60)
        
        self.fenetre_accueil.mainloop()


    def lancer_le_jeu(self):
        #on ferme la fenetre d'accueil
        self.fenetre_accueil.destroy()

        #Creer la fenetre de jeu
        fenetre_jeu = tk.Tk()
        fenetre_jeu.title("Casse-brique")
        fenetre_jeu.geometry('1200x700')

        #pour quitter le jeu
        BoutonQuitter = tk.Button(self.fenetre_jeu, text = "quitter", fg = 'red', command = self.fenetre_jeu.destroy, font=("Helvetica", 18))
        BoutonQuitter.pack(side = 'bottom',pady = 20 )

        #on affiche le nombre de vies et le score 
        label_vie = tk.Label(self.fenetre_jeu, text="Vies : 3")
        label_vie.pack(pady=10)
        label_score = tk.Label(self.fenetre_jeu, text="Score : 0")
        label_score.pack(pady=10)

        self.fenetre_jeu.mainloop()



jeu = Casse_brique()


