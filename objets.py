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
        # Mémoriser la position avant le déplacement
        self.ancienne_coords = self.canvas.coords(self.objet)

        # Déplacer la balle
        self.canvas.move(self.objet, self.dx, self.dy)

        # Vérifier les collisions avec les murs
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
        # Coordonnées actuelles de la balle
        x1, y1, x2, y2 = self.canvas.coords(self.objet)

        # Coordonnées avant le déplacement
        ax1, ay1, ax2, ay2 = self.ancienne_coords

        # Objets touchés par la balle
        objets = self.canvas.find_overlapping(x1, y1, x2, y2)

        for brique in briques:
            if brique.objet not in objets:
                continue

            # Coordonnées de la brique
            bx1, by1, bx2, by2 = self.canvas.coords(brique.objet)

            # Déterminer si la balle a franchi un bord horizontal
            choc_horizontal = (
                (ax2 <= bx1 and x2 >= bx1)
                or (ax1 >= bx2 and x1 <= bx2)
            )

            # Déterminer si la balle a franchi un bord vertical
            choc_vertical = (
                (ay2 <= by1 and y2 >= by1)
                or (ay1 >= by2 and y1 <= by2)
            )

            # Si le côté est ambigu, utiliser la profondeur de pénétration
            largeur = min(x2, bx2) - max(x1, bx1)
            hauteur = min(y2, by2) - max(y1, by1)

            if not choc_horizontal and not choc_vertical:
                if largeur < hauteur:
                    choc_horizontal = True
                else:
                    choc_vertical = True

            # Position corrigée de la balle
            nx1, ny1, nx2, ny2 = x1, y1, x2, y2

            if choc_horizontal:
                self.dx = -self.dx

                if (ax1 + ax2) / 2 < (bx1 + bx2) / 2:
                    nx2 = bx1
                    nx1 = nx2 - (x2 - x1)
                else:
                    nx1 = bx2
                    nx2 = nx1 + (x2 - x1)

            if choc_vertical:
                self.dy = -self.dy

                if (ay1 + ay2) / 2 < (by1 + by2) / 2:
                    ny2 = by1
                    ny1 = ny2 - (y2 - y1)
                else:
                    ny1 = by2
                    ny2 = ny1 + (y2 - y1)

            # Appliquer la nouvelle position
            self.canvas.coords(
                self.objet,
                nx1, ny1, nx2, ny2
            )

            # Une brique dure devient une brique simple
            if isinstance(brique, Brique_dur):
                nouvelle_brique = Brique(
                    self.canvas,
                    brique.x,
                    brique.y
                )

                index = briques.index(brique)
                brique.detruire()
                briques[index] = nouvelle_brique

            else:
                # Une brique simple est détruite
                brique.detruire()
                briques.remove(brique)

            return True

        return False
    
class Brique:

    def __init__(self, canvas, x, y):
        self.canvas = canvas
        # 1. On stocke x et y pour pouvoir les retrouver si besoin
        self.x = x
        self.y = y
        self.objet = canvas.create_rectangle(
            x,
            y, 
            x + 90,
            y + 20,
            fill="#58B41B",
            outline="#58B41B",
            tags="brique"
        )

    # 2. On ajoute la méthode detruire ici aussi !
    def detruire(self):
        self.canvas.delete(self.objet)


class Brique_dur:

    def __init__(self, canvas, x, y):
        self.canvas = canvas
        # 1. On stocke également x et y ici
        self.x = x
        self.y = y
        self.objet = canvas.create_rectangle(
            x,
            y, 
            x + 90,
            y + 20,
            fill="#26500A", # Super choix de vert foncé !
            outline="#26500A",
            tags="brique_dur"
        )

    def detruire(self):
        self.canvas.delete(self.objet)
