'''
Sébastien Luc et Mario Courtial
le 22/09/2026
TP2
'''

#Types
entrees = ('article', 'adjectif', 'nom', 'nom_propre', 'verbe', 'point')
etat = ('attente_article', 'article_reconnu', 'attente_nom', 'attente_adjectif', 'attente_verbe', 'attente_nom_propre', 'attente_point')
sorties = ('phrase_correcte', 'phrase_incorrecte')


#variable
'''
table_de_transitions : Tableau [ États, Entrées ] d'états
table_de_sorties : Tableau [ États ] de Sorties
entree_act : Entrées
etat_act : États
sortie_act : Sorties'''



#table de transition avec l'état 8
table_de_transitions = {
            0: {'article': 1, 'nom_propre': 4, 'verbe': 8, 'nom': 8, 'adjectif': 8, 'point': 8},
            1: {'article': 8, 'nom_propre': 8, 'verbe': 8, 'nom': 2, 'adjectif': 1, 'point': 8},
            2: {'article': 8, 'nom_propre': 8, 'verbe': 3, 'nom': 8, 'adjectif': 2, 'point': 8},
            3: {'article': 5, 'nom_propre': 7, 'verbe': 8, 'nom': 8, 'adjectif': 8, 'point': 9},
            4: {'article': 8, 'nom_propre': 8, 'verbe': 3, 'nom': 8, 'adjectif': 8, 'point': 8},
            5: {'article': 8, 'nom_propre': 8, 'verbe': 8, 'nom': 6, 'adjectif': 5, 'point': 8},
            6: {'article': 8, 'nom_propre': 8, 'verbe': 8, 'nom': 8, 'adjectif': 6, 'point': 9},
            7: {'article': 8, 'nom_propre': 8, 'verbe': 8, 'nom': 8, 'adjectif': 8, 'point': 9},
            8: {'article': 8, 'nom_propre': 8, 'verbe': 8, 'nom': 8, 'adjectif': 8, 'point': 8},
            9: {'article': 8, 'nom_propre': 8, 'verbe': 8, 'nom': 8, 'adjectif': 8, 'point': 8}
        }



dictionnaire = {
    "le": "article", "la": "article", "un": "article",
    "chat": "nom", "souris": "nom", 
    "martin": "nom_propre", "julie": "nom_propre", "jean": "nom_propre", 
    "mange": "verbe", "dort": "verbe", 
    "petite": "adjectif", "joli": "adjectif", "grosse": "adjectif", "bleu": "adjectif", "verte": "adjectif", 
    ".": "point"
}

def reecriture(phrase):
    phrase = phrase.replace(",", " ").replace(";", " ")
    phrase = phrase.replace(".", " .")
    return phrase.split()

def validite_phrase(phrase):
    morceaux = reecriture(phrase)
    etat = 0
    if morceaux == []:
        return False
    for mot in morceaux:
        if mot not in dictionnaire:
            return False
        categorie = dictionnaire[mot]
        transitions = table_de_transitions.get(etat, {})
        if categorie in transitions:
            etat = transitions[categorie]
        else:
            etat = 8    
        if etat == 8:
            return False     
    return etat == 9


#a corriger les majuscules
