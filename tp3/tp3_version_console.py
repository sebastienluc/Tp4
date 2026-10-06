'''
Sebastien Luc
Le 29/09/2026
TP3
to do : 2e version avec les améliorations
'''
import random
import fichier_mots

def pendu(l):
    nombre_vie = 8

    #prend un mot au hasard
    mot = random.choice(l)

    #on affiche le debut du jeu"_" * (len(mot) - 1)
    lettres_trouvees = [mot[0]] + ["_"] * (len(mot) - 1)

    #on regarde dans le mot si il a plusieurs fois sa premiere lettre dans lui meme
    for j in range(len(mot)):
        if mot[0] == mot[j]:
            lettres_trouvees[j] = mot[0]

    #tant qu'il reste des vies et des lettres a trouvé
    while nombre_vie > 0 and "_" in lettres_trouvees :

        #on montre l'etat actuel du jeu 
        print("\nMot actuel :", " ".join(lettres_trouvees))
        print("Vies restantes :" ,nombre_vie,)
        
        #on demande une lettre
        propose = input("Proposez une lettre : ")
       
       #si la lettre n'est pas dans le mot
        if propose not in mot:
            print("la lettre", propose, "n'est pas dans le mot")
            print("il vous reste",nombre_vie, "vies")
            nombre_vie = nombre_vie - 1
        else :
        #si la lettre donnée appartient au mot
            for k in range(len(mot)):
                if propose == mot[k]:
                    lettres_trouvees[k] = propose

    #message de fin 
    if "_" not in lettres_trouvees:
        print("vous avez gagné")
    else:
        print("vous avez perdu, le mot était" ,mot,)

    return lettres_trouvees


pendu(fichier_mots.liste_mots)
