import tkinter as tk
import random

# Créer la fenêtre principale
root = tk.Tk()
root.title("Jeu du casse brique")

# Taille de la fenêtre
root.geometry("800x600")

# Créer le canvas
canvas = tk.Canvas(root, width=800, height=500, bg="black")
canvas.pack()

# Variables pour stocker la position de la raquette
raquette_x = 375
raquette_y = 450

# Créer un cercle rouge sur le canvas
cercle = canvas.create_oval(400, 400, 420, 420, fill="red", outline="red", width=2)

#créer les briques sur le canvas
for i in range(25, 760, 95):
    for j in range(20, 150, 30):
        canvas.create_rectangle(i, j, i + 75, j + 20, fill="green", outline="green")




# Fonction pour déplacer la balle

dx = random.choice([-5, 5])
dy = -5
def deplacer_balle():
    canvas.move(cercle, dx, dy)
    root.after(30, deplacer_balle)
deplacer_balle()


# Fonction pour dessiner la raquette sur le canvas
def draw_raquette():
    canvas.create_rectangle(
        raquette_x,
        raquette_y,
        raquette_x + 70,
        raquette_y + 10,
        fill="blue"
    )

# Fonction pour déplacer la raquette
def move_raquette(event):
    global raquette_x

    if event.keysym == "Left":
        raquette_x -= 10

    elif event.keysym == "Right":
        raquette_x += 10

    canvas.delete("all")
    draw_raquette()



# Relier le clavier à la fonction
root.bind("<KeyPress>", move_raquette)

# Dessiner la raquette au démarrage
draw_raquette()

# Garder la fenêtre ouverte
root.mainloop()