################### Les Extensions ################################

Finalement comme extensions pour l'étape 3 nous avons implémenté un menu totalement fonctionnel,
qui permet à l'utilisateur de faire des choix concernant la partie ou consulter les touches.

Nous avons aussi crée un éditeur de map qui permet au joueur de créer ses propres maps ou alors de modifier une existante. 
Comme troisième extension nous avons choisi de créer un système de chemin réponse,
cette fonction permet au joueur de créer un chemin qui représente la solution d'une map et peut ensuite l'activer pour faire
automatiquement bouger le gardien.




################### L'organisation du programme ###################

Pour l'organisation du travail, les fonctions concernant l'editeur de map et les chemins réponses on été faites par Lucas et le menu par Alexandre. 
Quant aux fonctions du main, elles ont toutes été faites en groupe.



################### Les choix techniques ##########################

Nous avons conservé notre choix de map sous forme d'une liste lorsque nous lisons la map.

Comme modules nous avons utilisé UpemTk pour la partie graphique,
et la fonction randint du module random pour le mode debug. Ainsi que le module os pour pouvoir importer les noms des maps présents dans le répertoire maps.

Nous avons aussi ajouté un module que nous avons créé et qui permet de redimensionner des images à l'aide de Tkinter.




################### Problèmes rencontrés ##########################


Concernant l'éditeur on a rencontré des problèmes par rapport au positionnement des images après un clique du joueur. 
De plus nous avons eu des dificultés concernant le bon affichage des maps dans le menu.

Pour conclure on a aussi eu un problème par rapport au module de l'éditeur qui faisait planter le programme dès qu'on l'appelait une deuxième fois, 
pour cette raison on c'est vus contraints à incorporer ce module dans le programme principal.

