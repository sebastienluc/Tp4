'''
Sebastien Luc
Le 29/09/2026
TP3
to do : 
'''
import random
import fichier_mots

def pendu2(l):
    nombre_vie = 8
    lettres_deja_dites = []

    #prend un mot au hasard
    mot = random.choice(l)

    #on stocke la première lettre dans une liste 
    lettres_deja_dites.append(mot[0])

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
        propose = input("Proposez une lettre: ")

       
       #si la lettre à déjà été dite
        if propose in lettres_deja_dites:
            print("la lettre", propose, "a déjà été dite")
        else:
            lettres_deja_dites.append(propose)


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

    return nombre_vie

#pendu2(fichier_mots.liste_mots)

def jouer_au_pendu(l):
    meilleur_score = 0
    rejouer = "y"
    while rejouer == "y":

        #nombre de vie à la fin de la dernière partie
        vies_finales = pendu2(l)
        if vies_finales > meilleur_score:
            meilleur_score = vies_finales
            print("Nouveaux record :" , vies_finales, "vies restantes")
        else:
            print("Meilleur score:",meilleur_score, "vies restantes" )

        #demande de rejouer
        rejouer = input("\nVoulez vous rejouer ?(y/n):" )

    print("merci d'avoir joué")

jouer_au_pendu(fichier_mots.liste_mots)