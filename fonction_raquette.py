# Variables pour stocker la position de la raquette
raquette_x = 0
raquette_y = 0

# Fonction pour dessiner la raquette sur le canvas
def draw_raquette():
    canvas.create_rectangle(raquette_x, raquette_y, raquette_x+70, raquette_y+10, fill="blue")
