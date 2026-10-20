'''
Sebastien Luc
Le 29/09/2026
TP3
to do : version tkinter
'''
import random
import fichier_mots
from tkinter import *
from tkinter import messagebox

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

#jouer_au_pendu(fichier_mots.liste_mots)


def proposer():
    #récuperer la lettre
    lettre = zone_saisie.get()
    
    #vérifier que l'utilisateur a tapé une seule lettre
    if len(lettre) != 1:
        messagebox.showwarning("Attention", "Veuillez entrer une seule lettre !")
        return

    #La lettre a déjà été dite
    if lettre in lettres_deja_dites:
        messagebox.showinfo("Info", f"La lettre '{lettre}' a déjà été dite.")
        return

    lettres_deja_dites.append(lettre)

    #La lettre n'est pas dans le mot
    if lettre not in mot:
        nombre_vie = nombre_vie - 1

    #La lettre est dans le mot
    else:
        for k in range(len(mot)):
            if lettre == mot[k]:
                lettres_trouvees[k] = lettre

    #Actualise le mot affiché avec les nouvelles lettres trouvées
    label_mot.config(text=" ".join(lettres_trouvees))

    if "_" not in lettres_trouvees:
        messagebox.showinfo("Le mot était bien : {mot}")
        mw.destroy() # Ferme le jeu
    elif vies <= 0:
        messagebox.showerror("Le mot était : {mot}")
        mw.destroy()


mw = Tk()
mw.title("Jeu_du_pendu")
mw.geometry('900x500+500+200')

BoutonQuitter = Button (mw, text = "quitter", fg = 'red', command = mw.destroy)
BoutonQuitter.pack(side = 'right', padx = 5 , pady = 5 )

label1=Label(mw, text = "Entrez une lettre")
label1.pack(side = 'left', padx = 5 , pady = 5 )

lettre = StringVar()
champ = Entry(mw, textvariable = "entrezunelettre" )
champ.pack(side = 'left', padx = 5 , pady = 5 )

BoutonLancer = Button(mw, text = "proposer", command = 'proposer')
BoutonLancer.pack(side = 'left', padx = 5 , pady = 5 )

mw.mainloop()
