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

    def deplacer(self, briques):

        self.canvas.move(self.objet, self.dx, self.dy)

        self.colision_murs()
        self.colision_raquette(self.raquette)
        self.collision_briques(briques)


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

                # Arrêter la boucle après une collision
                break


class Brique:

    def __init__(self, canvas, x, y):

        self.canvas = canvas
        self.objet = canvas.create_rectangle( x, y, x + 90, y + 20, fill="green", outline="green", tags="brique" )

    def detruire(self):
        self.canvas.delete(self.objet)