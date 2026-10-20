import tkinter as tk
import random

largeur_ecran = 1200
hauteur_ecran = 600

largeur_raquette = 70
hauteur_raquette = 10
vitesse_raquette = 10

rayon_balle = 10
vitesse_balle = 5

largeur_brique = 90
hauteur_brique = 20

class Raquette:

    def __init__(self, canvas):

        #création de la raquette et la placer sur le canvas
        self.canvas = canvas

        self.x = (largeur_ecran - largeur_raquette) // 2
        self.y = hauteur_ecran - 150

        self.objet = canvas.create_rectangle(
            self.x,
            self.y,
            self.x + largeur_raquette,
            self.y + hauteur_raquette,
            fill="blue",
            tags="raquette"
        )

    #mise en place du système de déplacement de la raquette avec les touches gauche et droite 
    def deplacer(self, direction):

        if direction == "Left":
            self.x -= vitesse_raquette

        elif direction == "Right":
            self.x += vitesse_raquette

        #empêche la raquette de sortir du canvas
        limite_droite = largeur_ecran - largeur_raquette
        if self.x < 0:
            self.x = 0

        if self.x > limite_droite:
            self.x = limite_droite

        self.canvas.coords(
            self.objet,
            self.x,
            self.y,
            self.x + largeur_raquette,
            self.y + hauteur_raquette
        )

class Balle:

    def __init__(self, canvas):

        #création de la balle et la placer sur le canvas
        self.canvas = canvas

        self.objet = canvas.create_oval(
            largeur_ecran // 2 - rayon_balle,
            hauteur_ecran // 2 - rayon_balle,
            largeur_ecran // 2 + rayon_balle,
            hauteur_ecran // 2 + rayon_balle,
            fill="red",
            outline="red"
        )

        self.dx = random.choice([- vitesse_balle, vitesse_balle])
        self.dy = -vitesse_balle

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
            self.dx = vitesse_balle

        if x2 >= largeur_ecran:
            self.dx = - vitesse_balle

        if y1 <= 0:
            self.dy = vitesse_balle

        if y2 >= hauteur_ecran:
            return False # la balle a touché le bas 

        return True # la balle est encore en jeu 

    def collision_raquette(self, raquette):

        x1, y1, x2, y2 = self.canvas.coords( self.objet )
        rx1, ry1, rx2, ry2 = self.canvas.coords( raquette.objet )

        if x2 >= rx1 and x1 <= rx2 and y2 >= ry1 and y1 <= ry2:
            self.dy = - vitesse_balle


    def collision_briques(self, briques):
        # Coordonnées actuelles de la balle
        x1, y1, x2, y2 = self.canvas.coords(self.objet)

        # Coordonnées précédentes de la balle
        ancien_x1 = x1 - self.dx
        ancien_y1 = y1 - self.dy
        ancien_x2 = x2 - self.dx
        ancien_y2 = y2 - self.dy

        # Objets touchés par la balle
        objets = self.canvas.find_overlapping(x1, y1, x2, y2)

        for brique in briques:
            if brique.objet in objets:
                # Coordonnées de la brique
                bx1, by1, bx2, by2 = self.canvas.coords(brique.objet)

                # Déterminer le côté de collision
                choc_horizontal = (
                    ancien_x2 <= bx1 or ancien_x1 >= bx2
                )

                choc_vertical = (
                    ancien_y2 <= by1 or ancien_y1 >= by2
                )

                if choc_horizontal and not choc_vertical:
                    # Collision sur un côté gauche ou droit
                    self.dx = -self.dx

                elif choc_vertical and not choc_horizontal:
                    # Collision sur le dessus ou le dessous
                    self.dy = -self.dy

                else:
                    # Collision sur un coin
                    self.dx = -self.dx
                    self.dy = -self.dy

                # Détruire la brique touchée
                brique.detruire()
                briques.remove(brique)

                return True
        return False

    
class Brique:

    def __init__(self, canvas, x, y):

        self.canvas = canvas
        self.objet = canvas.create_rectangle(
            x,
            y, 
            x + largeur_brique,
            y + hauteur_brique,
            fill="green",
            outline="green",
            tags="brique"
        )

    def detruire(self):
        self.canvas.delete(self.objet)
