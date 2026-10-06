import tkinter as tk
import random

# Créer la fenêtre principale
fenetre_jeu = tk.Tk()
fenetre_jeu.title("Jeu du casse brique")

# Taille de la fenêtre
fenetre_jeu.geometry("1200x700")

# Créer le canvas
canvas = tk.Canvas(fenetre_jeu, width=1200, height=600, bg="black")
canvas.pack()


# Créer un cercle rouge sur le canvas
cercle = canvas.create_oval(590, 400, 610, 420, fill="red", outline="red", width=2)

#créer les briques sur le canvas
for i in range(25, 1150, 115):
    for j in range(30, 180, 30):
        canvas.create_rectangle(i, j, i + 90, j + 20, fill="green", outline="green")




# Fonction pour déplacer la balle

dx = random.choice([-5, 5])
dy = -5

def deplacer_balle():
    global dx, dy

    # Déplacer la balle
    canvas.move(cercle, dx, dy)

    # Récupérer les coordonnées
    x1, y1, x2, y2 = canvas.coords(cercle)

    # Collision avec les murs
    if x1 <= 0:     #gauche
        dx = 5
    if x2 >= 1200:  #droit
        dx = -5
    if y1 <= 0:     #haut 
        dy = 5
    if y2 >= 600:    #bas
        fenetre_jeu.destroy()

    #colision avec la raquette


    fenetre_jeu.after(30, deplacer_balle)
deplacer_balle()


# Variables pour stocker la position de la raquette
raquette_x = 565
raquette_y = 550

# Fonction pour dessiner la raquette sur le canvas
def draw_raquette():
    canvas.create_rectangle(raquette_x, raquette_y, raquette_x + 70, raquette_y + 10, fill="blue", tags="raquette")

# Fonction pour déplacer la raquette
def move_raquette(event):
    global raquette_x

    if event.keysym == "Left":
        if raquette_x < 0:
            raquette_x = 0
        else:
            raquette_x -= 10


    elif event.keysym == "Right":
        if raquette_x > 1130:
            raquette_x = 1130
        else:
            raquette_x += 10

    canvas.delete("raquette")
    draw_raquette()



# Relier le clavier à la fonction
fenetre_jeu.bind("<KeyPress>", move_raquette)

# Dessiner la raquette au démarrage
draw_raquette()

# Garder la fenêtre ouverte
fenetre_jeu.mainloop()