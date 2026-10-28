# Tp4

Ce projet a été réalisé par Mario Courtial et Sébastien Luc dans le cadre du TP4, 5 et 6.

#L'adresse du répertoire GIT 
Le code source complet, l'historique des commits ainsi que les différentes branches de développement de ce projet sont accessibles à l'adresse suivante :
https://github.com/sebastienluc/Tp4.git

#Règle du jeu
Le but de ce jeu est de détruire toutes les briques présentes à l'écran sans perdre les 3 vies.
Tout d'abord l'écran permet de choisir en 2 niveaux, et il est possible de déplacer la raquette avec les fléches gauche et droite.
Pour chaque partie le joueur possède 3 vies et un nombre de score qui augmente au fur et à mesure que le joueur casse des briques.

#Spécificité de l'implémentation
Notre implémentation repose sur le paradigme de la **Programmation Orientée Objet** et utilise la bibliothèque graphique standard **Tkinter**.
Tout d'abord, nous avons séparé l'interface utilisateur et le moteur de jeu du comportement physique des objets pour garantir un code modulaire et évolutif.
Le rafraîchissement des frames et les calculs de trajectoires sont orchestrés de manière asynchrone via la méthode `.after()` de Tkinter, évitant tout blocage de l'interface.
Le niveau 1 comporte uniquement des briques simples.
Le niveau 2 Génère de manière aléatoire (50/50) des briques normales et des briques résistantes, doublant la durabilité de certaines zones.

## Organisation de l'Archive & Structures de Données

### 1. Contenu de l'archive de rendu
L'archive contient l'arborescence complète suivante nécessaire au bon fonctionnement du jeu :
* `main.py` : Point d'entrée de l'application (exécute le cycle principal).
* `jeu.py` : Gère le moteur de jeu, les fenêtres Tkinter (accueil et jeu), les barres de statistiques et la boucle d'animation.
* `objets.py` : Contient les classes et la logique physique des entités de jeu.
* `README.md` : Le présent fichier explicatif.


### 2. Emplacement de l'implémentation des structures de données
Les structures de données modélisant les composants du jeu sont réparties de la manière suivante :

* **Dans le fichier `objets.py` :**
  * `Raquette` : Gère la structure, les coordonnées et les limites de déplacement de la raquette.
  * `Balle` : Contient les vecteurs de vitesse (`dx`, `dy`), la physique des rebonds et la gestion avancée des collisions (murs, raquette et briques).
  * `Brique` : Structure de données d'une brique standard verte.
  * `Brique_dur` : Structure de données d'une brique résistante vert foncé.
    
* **Dans le fichier `jeu.py` :**
  * `self.briques = []` : Liste dynamique (tableau) utilisée pour stocker, mettre à jour, transformer (Brique_dur -> Brique) et supprimer les briques en temps réel lors du cycle de jeu.
  * `self.raquette` : Stocke l'instance unique de la raquette pour suivre sa position X.
  * `self.balle` : Stocke l'instance unique de la balle contenant ses vecteurs de vitesse.
  * `self.briques = []` : Liste dynamique (Tableau) utilisée pour stocker, mettre à jour, transformer (Brique_dur -> Brique) et supprimer les briques en temps réel lors du cycle de jeu.

