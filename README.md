# Tp4

Ce projet a été réalisé par Mario Courtial et Sébastien Luc dans le cadre du TP4, 5 et 6.

#L'adresse du répertoire GIT 
Le code source complet, l'historique des commits ainsi que les différentes branches de développement de ce projet sont accessibles à l'adresse suivante :
https://github.com/sebastienluc/Tp4.git

#Règle du jeu
Le but de ce jeu est de détruire toutes les briques présentent à l'écran sans perdre les 3 vies.
Tout d'abord l'écran permet de choisir en 2 niveaux, et il est possible de déplacer la raquette avec les fléches gauche et droite.
Pour chaque partie le joueur possède 3vies et un nombre de score qui augmente au fur et à mesure que le joueur casse des briques.

#Spécificité de l'implémentation
Notre implémentation repose sur le paradigme de la **Programmation Orientée Objet** et utilise la bibliothèque graphique standard **Tkinter**.
Tout d'abord, nous avons séparé l'interface utilisateur et le moteur de jeu du comportement physique des objets pour garantir un code modulaire et évolutif.
Le rafraîchissement des frames et les calculs de trajectoires sont orchestrés de manière asynchrone via la méthode `.after()` de Tkinter, évitant tout blocage de l'interface.
Le niveau 1 comporte uniquement des briques simples.
Le niveau 2 Génère de manière aléatoire (50/50) des briques normales et des briques résistantes, doublant la durabilité de certaines zones.




