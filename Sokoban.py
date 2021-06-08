from upemtk import *
from random import randint
from Redim_img import *
import os
from time import sleep


############################ EDITEUR  ################################################
def read_map_edit(Editeur=None):
    '''
    On lit la map pour l'instaurer dans notre liste
    '''

    global map_game

    name_map = Editeur

    map_txt = open('maps/' + name_map, "r")

    map_choose = map_txt.readline()
    map_game = []

    for ligne in map_txt:
        if ligne[0] not in "BTS.KWD" and ligne[0] != '':
            continue
        lst_ligne = list(ligne[:-1])

        map_game += lst_ligne
        col = len(lst_ligne)
    lig = len(map_game) // col
    map_txt.close()
    return col, lig
    
def parametre_img_edit(col, lig):
    '''
    Même fonction que parametre mais cette fois avec des valeurs adaptées à l'éditeur
    '''

    global taille_img, case_size, box_gif, floor_gif, floor_gif, key_gif, door_gif, target_gif, wall_gif, right_gif, left_gif, up_gif, down_gif
    cree_fenetre(500, 500)
    taille_img = 50
    tuple_img = ("box.gif", "floor.gif", "key.gif", "door.gif", "target.gif",
                 "wall.gif", "player_r.gif", "player_l.gif", "player_u.gif", "player_d.gif")
    width_case = round(((500 // col - 1) / taille_img), 1)
    height_case = round(((500 // lig - 1 // col - 1) / taille_img), 1)
    texte1 = texte(250, 250, "En Chargement ...",
                   ancrage='center', police='Purisa', taille=20)
    mise_a_jour()
    if height_case >= width_case and width_case < 1:

        case_size = taille_img * width_case
        for element in (tuple_img):
            img = create(element, int(width_case * 10), 10)

        box_gif = "box_redim.gif"
        floor_gif = "floor_redim.gif"
        key_gif = "key_redim.gif"
        door_gif = "door_redim.gif"
        target_gif = "target_redim.gif"
        wall_gif = "wall_redim.gif"
        right_gif = "player_r_redim.gif"
        left_gif = "player_l_redim.gif"
        up_gif = "player_u_redim.gif"
        down_gif = "player_d_redim.gif"

    elif width_case > height_case and height_case < 1:
        case_size = taille_img * height_case
        for element in (tuple_img):
            img = create(element, int(height_case * 10), 10)

        box_gif = "box_redim.gif"
        floor_gif = "floor_redim.gif"
        key_gif = "key_redim.gif"
        door_gif = "door_redim.gif"
        target_gif = "target_redim.gif"
        wall_gif = "wall_redim.gif"
        right_gif = "player_r_redim.gif"
        left_gif = "player_l_redim.gif"
        up_gif = "player_u_redim.gif"
        down_gif = "player_d_redim.gif"

    else:
        case_size = taille_img
        box_gif = "box.gif"
        floor_gif = "floor.gif"
        key_gif = "key.gif"
        door_gif = "door.gif"
        target_gif = "target.gif"
        wall_gif = "wall.gif"
        right_gif = "player_r.gif"
        left_gif = "player_l.gif"
        up_gif = "player_u.gif"
        down_gif = "player_d.gif"

    efface(texte1)
    texte(250, 230, "Chargement fini, vous pouvez",
          ancrage='center', police='Purisa', taille=20)
    texte(250, 270,  "Cliquez pour créer votre propre carte",
          ancrage='center', police='Purisa', taille=20)
    attente_clic()
    mise_a_jour()
    ferme_fenetre()


def fen_edit(col,lig):

    '''
    Permet de mettre en place la fenêtre d'édition avec les icones
    '''

    width_edit=175
    height_edit=case_size*lig
    left_x,right_x=25,100
    y_1,y_2,y_3,y_4,y_5=25,125,225,325,425
    cree_fenetre(width_edit+case_size*col,500)
    rectangle(0,0,(width_edit+case_size*col),500,remplissage='black')
    image(left_x,y_1,"wall.gif", ancrage='nw')
    image(left_x,y_2,"target.gif", ancrage='nw')
    image(left_x,y_3,"door.gif", ancrage='nw')
    image(left_x,y_4,"gomme.png", ancrage='nw')
    image(right_x,y_1, "box.gif", ancrage='nw')
    image(right_x,y_2,"player_d.gif", ancrage='nw')
    image(right_x,y_3,"key.gif", ancrage='nw')
    image(right_x,y_4,"play.png", ancrage='nw')
    image(left_x,y_5,"save.gif", ancrage='nw')
    draw_case_edit(width_edit,height_edit,col,lig)
    return width_edit+case_size*col,height_edit,left_x,right_x,y_1,y_2,y_3,y_4,y_5

def draw_case_edit(width_edit,height_edit,col,lig):

    '''
    Dessine la carte à éditer
    '''

    up_draw=250-(lig*case_size)//2

    for i in range(len(map_game)):
        if map_game[i]=='.':
            img=floor_gif
        elif map_game[i]=='W':
            img=wall_gif
        elif map_game[i]=='B':
            img=box_gif
        elif map_game[i]=='T':
            img=target_gif
        elif map_game[i]=='S':
            img=down_gif
        elif map_game[i]=='K':
            img=key_gif
        elif map_game[i]=='D':
            img=door_gif

        image(width_edit+(i%col)*case_size,case_size*(i//col)+up_draw,img, ancrage='nw')

def take_img_edit(x,y,name_map,col,lig):

    '''
    Permet de savoir quelle icone à était activé
    '''

    taille_pol=int(width_wid//38)#Pour adaptrer la taille de la police à la fenêtre
    taille_img_present=50

    if left_x<x<left_x+taille_img_present:

        if y_1<=y<=y_1+taille_img_present:
            return wall_gif,'W',name_map

        elif y_2<=y<=y_2+taille_img_present:
            return target_gif,'T',name_map

        elif y_3<=y<=y_3+taille_img_present:
            return door_gif,'D',name_map

        elif y_4<=y<=y_4+taille_img_present:
            return  floor_gif,'.',name_map

        elif y_5<=y<=y_5+taille_img_present:

            verif_var=verif_edit()#On vérifie que les paramètres de la map soient valides
            if verif_var==True:
                name_map=save_edit(col,lig)#Et si oui on sauvegarde

            return  None,None,name_map
        else:
            return None,None,name_map#Dans tout les cas on ne renvoie pas d'image

    elif right_x<=x<=right_x+taille_img_present:
        if y_1<=y<=y_1+taille_img_present:
            return box_gif,'B',name_map
        elif y_2<=y<=y_2+taille_img_present:
            return down_gif, 'S',name_map
        elif y_3<=y<=y_3+taille_img_present:
            return key_gif,'K',name_map
        elif y_4<=y<=y_4+taille_img_present:

            if name_map != None:
                ferme_fenetre()

                L=["box_redim.gif","floor_redim.gif","key_redim.gif","door_redim.gif","target_redim.gif","wall_redim.gif","player_r_redim.gif","player_l_redim.gif","player_u_redim.gif","player_d_redim.gif"]

                if L[0] == box_gif:
                    for el in L:
                        supprime(el)#On supprime toutes les image redimensionner
                editeur(name_map)#Et on joue
            else:
                texte1=texte(200,230,"Vous devez sauvegarder votre fichier",ancrage='nw',police='Purisa',taille=taille_pol)
                mise_a_jour()
                sleep(1)
                efface(texte1)
                mise_a_jour()

            return  None,None,name_map
        else:
            return None,None,name_map
    else:
        return None,None,name_map

def put_img_edit(img_choose,letter,x,y,col,lig):

    '''
    Définir les coorodonées de mise en place de l'image
    '''

    taille_pol=int(width_wid//38)
    if img_choose is None:
        return

    up_draw=250-(lig*case_size)//2
    width_edit=175
    x_pos=((x-width_edit)//case_size)#On définit en fonction du clique où doit se placer l'image dans notre liste
    y_pos=(y-up_draw)//case_size
    x_img=(x_pos*case_size)+width_edit#On définit les coordonées pour placer l'image
    y_img=y_pos*case_size+up_draw


    if img_choose == down_gif:#On vérifie qu'on ne peut pas avoir deux joueurs
        if 'S' in map_game:
            texte1=texte(40,475,"Vous ne pouvez placer que un seul joueur",ancrage='nw',police='Purisa',taille=taille_pol,couleur='white')
            mise_a_jour()
            sleep(1)
            efface(texte1)
            mise_a_jour()
            return
    image(x_img,y_img,img_choose,ancrage='nw')#on affiche l'image
    liste_pos=(col*y_pos)+x_pos
    map_game[int(liste_pos)]=letter#on modifie la liste avec la lettre correspondate

def verif_edit():

    '''
    On vérifie si les conditions pour valider la carte sont corrects
    '''

    dico=dict()
    verif_var=True
    taille_pol=int(width_wid//38)
    for el in map_game:
        if el not in dico:
            dico[el]=1
        else:
            dico[el]+=1

    if 'T' not in map_game:#il doit y avoir au moins une cible
        texte1=texte(40,475,"Il doit y avoir au minimum une cible",ancrage='nw',police='Purisa',taille=taille_pol,couleur='white')
        mise_a_jour()
        sleep(1)
        efface(texte1)
        mise_a_jour()
        verif_var=False

    if 'S' not in map_game:#il doit y avoir un joueur
        texte1=texte(40,475,"Vous n'avez pas placer votre joueur",ancrage='nw',police='Purisa',taille=taille_pol,couleur='white')
        mise_a_jour()
        sleep(1)
        efface(texte1)
        mise_a_jour()
        verif_var=False


    if 'D' in map_game:#On verifie qu'il y est assez de clés pour le nombre de porte
        if 'K' not in dico:
            dico['K']=0
        if dico['K']<dico['D']:
            verif_var=False
            texte1=texte(40,475,"Il n'y a pas assez de clé",ancrage='nw',police='Purisa',taille=taille_pol,couleur='white')
            mise_a_jour()
            sleep(1)
            efface(texte1)
            mise_a_jour()

    if 'T' in map_game:#On verifie qu'il y est assez de boites pour le nombre de cible
        if'B' not in dico:
            dico['B']=0
        if dico['T']>dico['B']:
            verif_var=False
            texte1=texte(40,475,"Il n'y a pas assez de boite",ancrage='nw',police='Purisa',taille=taille_pol,couleur='white')
            mise_a_jour()
            sleep(1)
            efface(texte1)

    return verif_var


def save_edit(col,lig):

    '''
    Sauvegarde de la map à partir de la liste qui a été modifié au cours de l'édition
    '''

    name_map=input("Quel nom de fichier voulez-vous lui donner ? ")

    while name_map == '':
        name_map=input("Vous devez nommer votre map avant la sauvegarde!" + '\n' + "Quel nom de fichier voulez-vous lui donner ? ")

    with open('maps/'+name_map,'w') as save_file:
        save_file.write('Titre: '+name_map)
        save_file.write('\n')
        x=1
        for i in range(len(map_game)):
            if i == (col*x)-1:
                save_file.write(map_game[i])
                save_file.write('\n')
                x+=1
            else:
                save_file.write(map_game[i])

        print("Votre map a été sauvegardé avec le nom "+name_map)
    return name_map

def edit_map(name_map=None,lig=None,col=None):

    '''
    Il s'agit du main de l'éditeur
    '''

    global width_wid,height_wid,left_x,right_x,y_1,y_2,y_3,y_4,y_5,map_game

    if name_map!=None:#Si on lance l'éditeur avec un map prédefini
        col,lig=read_map_edit(name_map)
    else:#Sinon l'éditeur est une map vide
        map_game=['.']*(col*lig)

    parametre_img_edit(col,lig)#On iniatlise les image à utiliser
    width_wid,height_wid,left_x,right_x,y_1,y_2,y_3,y_4,y_5=fen_edit(col,lig)#Ouvrir et dessiner la carte
    img_choose= floor_gif
    letter="."#On commence en mettant le sol comme paramètre de base

    up_draw=250-(lig*case_size)//2#Pour le centrage vertical de l'éditeur
    while True:
        mise_a_jour()
        event = donne_evenement()
        type_event = type_evenement(event)
        if type_event == 'Touche':
            nom_touche=touche(event)
            if nom_touche == 'm' or nom_touche == 'M':#Si on appuie sur M on va au menu
                ferme_fenetre()
                menu()

        elif type_event == 'ClicDroit' or type_event == 'ClicGauche':
            x,y = clic_x(event), clic_y(event)#On récupère les coordonées de clic
            if 25<=x<175:
                if 0<=y<=500:
                    img_choose,letter,name_map=take_img_edit(x,y,name_map,col,lig)#Si on clique sur les icone on choisi l'icone


            if 175<=x<=width_wid:#sinon on pose un objet
                if up_draw<=y<=height_wid+up_draw:
                    put_img_edit(img_choose,letter,x,y,col,lig)



###################################  FONCTIONS DE MOUVEMENT  #############################################################


def up(player_coord,player_img,wall_coord,box_coord,box_img,door_coord,door_img,key,height_window,width_window):

    '''
    Fonction permettant de déplacer le joueur vers le haut
    '''

    x1 = player_coord[0]
    y1 = player_coord[1]

    if colision_wall(x1,y1-case_size,wall_coord) == None:#On regarde si on bouge vers un mur
        return(player_coord,player_img,box_coord,box_img,door_coord,door_img,key)


    if colision_door(x1,y1-case_size,door_coord,door_img,key) == None:#On regarde si on bouge vers une porte et si on peut l'ouvrir
        return(player_coord,player_img,box_coord,box_img,door_coord,door_img,key)


    if y1 == 0:#On regarde si on bouge en dehors de la fenêtre
        return(player_coord,player_img,box_coord,box_img,door_coord,door_img,key)


    for i in range(len(box_coord)):#On regarde si on bouge une boîte en même temps que le joueur
        if box_coord[i][0] == x1:
            if box_coord[i][1]+case_size==y1:
                x1_box = box_coord[i][0]
                y1_box = box_coord[i][1]


                if colision_wall(x1_box,y1_box-case_size,wall_coord) == None:#On regarde si notre boîte bouge vers un mur
                    return(player_coord,player_img,box_coord,box_img,door_coord,door_img,key)


                elif colision_door_box(x1_box,y1_box-case_size,door_coord,door_img,key) == None:#On regarde si notre boîte bouge vers une porte
                    return(player_coord,player_img,box_coord,box_img,door_coord,door_img,key)

                elif colision_box(x1_box,y1_box-case_size,box_coord) == None:#On regarde si notre boîte bouge vers contre une autre boîte
                    return(player_coord,player_img,box_coord,box_img,door_coord,door_img,key)

                elif y1_box == 0:#On regarde si notre boîte bouge en dehors de la fenêtre
                    return(player_coord,player_img,box_coord,box_img,door_coord,door_img,key)


                while y1 != (player_coord[1]-case_size):#Si on bouge avec une boîte on déplace l'image du joueur et de la boîte
                    y1_box = y1_box - case_size/10
                    y1 = y1 - case_size/10


                    efface(player_img)
                    efface(box_img[i])

                    player_img = image(x1, y1, up_gif, ancrage='nw', tag='')
                    box_img[i] = image(x1_box, y1_box, box_gif, ancrage='nw', tag='')

                    mise_a_jour()


                efface(player_img)
                player_img = image(x1, y1, up_gif, ancrage='nw', tag='')
                mise_a_jour()

                player_coord[1] = y1#On modifie les coordonées du joueur
                box_coord[i][1] = y1_box#et de la boîte


                return (player_coord,player_img,box_coord,box_img,door_coord,door_img,key)


    while y1 != (player_coord[1]-case_size):#On déplace le joueur et son image
        y1 = y1-case_size/10

        efface(player_img)
        player_img = image(x1, y1, up_gif, ancrage='nw', tag='')

        mise_a_jour()


    efface(player_img)
    player_img = image(x1, y1, up_gif, ancrage='nw', tag='')
    mise_a_jour()

    player_coord[1] = y1
    return (player_coord,player_img,box_coord,box_img,door_coord,door_img,key)

def down(player_coord,player_img,wall_coord,box_coord,box_img,door_coord,door_img,key,height_window,width_window):

    '''
    Fonction permettant de déplacer le joueur vers le bas
    '''

    x1 = player_coord[0]
    y1 = player_coord[1]



    if colision_wall(x1,y1+case_size,wall_coord) == None:
        return(player_coord,player_img,box_coord,box_img,door_coord,door_img,key)

    if colision_door(x1,y1+case_size,door_coord,door_img,key) == None:
        return(player_coord,player_img,box_coord,box_img,door_coord,door_img,key)

    if y1 == height_window-case_size:
        return(player_coord,player_img,box_coord,box_img,door_coord,door_img,key)


    for i in range(len(box_coord)):
        if box_coord[i][0] == x1:
            if box_coord[i][1]==y1+case_size:
                x1_box = box_coord[i][0]
                y1_box = box_coord[i][1]



                if colision_wall(x1_box,y1_box+case_size,wall_coord) == None:
                    return(player_coord,player_img,box_coord,box_img,door_coord,door_img,key)


                elif colision_door_box(x1_box,y1_box+case_size,door_coord,door_img,key) == None:
                    return(player_coord,player_img,box_coord,box_img,door_coord,door_img,key)

                elif colision_box(x1_box,y1_box+case_size,box_coord) == None:
                    return(player_coord,player_img,box_coord,box_img,door_coord,door_img,key)
                elif y1_box == height_window-case_size:
                    return(player_coord,player_img,box_coord,box_img,door_coord,door_img,key)

                while y1 != (player_coord[1]+case_size):
                    y1_box = y1_box + case_size/10
                    y1 = y1 + case_size/10

                    efface(player_img)
                    efface(box_img[i])
                    player_img = image(x1, y1, down_gif, ancrage='nw', tag='')
                    box_img[i] = image(x1_box, y1_box, box_gif, ancrage='nw', tag='')

                    mise_a_jour()


                efface(player_img)
                player_img = image(x1, y1, down_gif, ancrage='nw', tag='')
                mise_a_jour()
                player_coord[1] = y1
                box_coord[i][1] = y1_box
                return (player_coord,player_img,box_coord,box_img,door_coord,door_img,key)

    while y1 != (player_coord[1]+case_size):
        y1 = y1+case_size/10

        efface(player_img)
        player_img = image(x1, y1, down_gif, ancrage='nw', tag='')
        mise_a_jour()


    efface(player_img)
    player_img = image(x1, y1, down_gif, ancrage='nw', tag='')
    mise_a_jour()

    player_coord[1] = y1
    return (player_coord,player_img,box_coord,box_img,door_coord,door_img,key)

def right(player_coord,player_img,wall_coord,box_coord,box_img,door_coord,door_img,key,height_window,width_window):

    '''
    Fonction permettant de déplacer le joueur vers la droite
    '''

    x1 = player_coord[0]
    y1 = player_coord[1]

    if colision_wall(x1+case_size,y1,wall_coord) == None:
        return(player_coord,player_img,box_coord,box_img,door_coord,door_img,key)

    if colision_door(x1+case_size,y1,door_coord,door_img,key) == None:
        return(player_coord,player_img,box_coord,box_img,door_coord,door_img,key)


    if x1 == width_window -case_size:
        return(player_coord,player_img,box_coord,box_img,door_coord,door_img,key)

    for i in range(len(box_coord)):
        if box_coord[i][1] == y1:
            if box_coord[i][0]==x1+case_size:
                x1_box = box_coord[i][0]
                y1_box = box_coord[i][1]


                if colision_wall(x1_box+case_size,y1_box,wall_coord) == None:
                    return(player_coord,player_img,box_coord,box_img,door_coord,door_img,key)


                elif colision_door_box(x1_box+case_size,y1_box,door_coord,door_img,key) == None:
                    return(player_coord,player_img,box_coord,box_img,door_coord,door_img,key)

                elif colision_box(x1_box+case_size,y1_box,box_coord) == None:
                    return(player_coord,player_img,box_coord,box_img,door_coord,door_img,key)

                elif x1_box == width_window -case_size:
                    return(player_coord,player_img,box_coord,box_img,door_coord,door_img,key)


                while x1 != (player_coord[0]+case_size):
                    x1_box = x1_box + case_size/10
                    x1 = x1+case_size/10

                    efface(player_img)
                    efface(box_img[i])
                    player_img = image(x1, y1, right_gif, ancrage='nw', tag='')
                    box_img[i] = image(x1_box, y1_box, box_gif, ancrage='nw', tag='')

                    mise_a_jour()


                efface(player_img)
                player_img = image(x1, y1, right_gif, ancrage='nw', tag='')
                mise_a_jour()

                player_coord[0] = x1

                box_coord[i][0] = x1_box



                return (player_coord,player_img,box_coord,box_img,door_coord,door_img,key)

    while x1 != (player_coord[0]+case_size):
        x1 = x1+case_size/10

        efface(player_img)

        player_img = image(x1, y1, right_gif, ancrage='nw', tag='')

        mise_a_jour()


    efface(player_img)
    player_img = image(x1, y1, right_gif, ancrage='nw', tag='')
    mise_a_jour()

    player_coord[0] = x1
    return (player_coord,player_img,box_coord,box_img,door_coord,door_img,key)

def left(player_coord,player_img,wall_coord,box_coord,box_img,door_coord,door_img,key,height_window,width_window):

    '''
    Fonction permettant de déplacer le joueur vers la gauche
    '''

    x1 = player_coord[0]
    y1 = player_coord[1]

    if colision_wall(x1-case_size,y1,wall_coord) == None:
        return(player_coord,player_img,box_coord,box_img,door_coord,door_img,key)

    if colision_door(x1-case_size,y1,door_coord,door_img,key) == None:
        return(player_coord,player_img,box_coord,box_img,door_coord,door_img,key)

    if x1 == 0:
        return(player_coord,player_img,box_coord,box_img,door_coord,door_img,key)

    for i in range (len(box_coord)):#modifier
        if box_coord[i][1] == y1:
            if box_coord[i][0]+case_size==x1:
                x1_box = box_coord[i][0]
                y1_box = box_coord[i][1]



                if colision_wall(x1_box-case_size,y1_box,wall_coord) == None:
                    return(player_coord,player_img,box_coord,box_img,door_coord,door_img,key)


                elif colision_door_box(x1_box-case_size,y1_box,door_coord,door_img,key) == None:
                    return(player_coord,player_img,box_coord,box_img,door_coord,door_img,key)

                elif colision_box(x1_box-case_size,y1_box,box_coord) == None:
                    return(player_coord,player_img,box_coord,box_img,door_coord,door_img,key)


                elif x1_box == 0:
                    return(player_coord,player_img,box_coord,box_img,door_coord,door_img,key)

                while x1 != (player_coord[0]-case_size):
                    x1_box = x1_box - case_size/10
                    x1 = x1-case_size/10

                    efface(player_img)
                    efface(box_img[i])
                    player_img = image(x1, y1, left_gif, ancrage='nw', tag='')
                    box_img[i] = image(x1_box, y1_box, box_gif, ancrage='nw', tag='')

                    mise_a_jour()


                efface(player_img)
                player_img = image(x1, y1, left_gif, ancrage='nw', tag='')
                mise_a_jour()
                player_coord[0] = x1

                box_coord[i][0] = x1_box


                return (player_coord,player_img,box_coord,box_img,door_coord,door_img,key)

    while x1 != (player_coord[0]-case_size):
        x1 = x1-case_size/10

        efface(player_img)
        player_img = image(x1, y1, left_gif, ancrage='nw', tag='')
        mise_a_jour()

    efface(player_img)
    player_img = image(x1, y1, left_gif, ancrage='nw', tag='')

    mise_a_jour()
    player_coord[0] = x1

    return (player_coord,player_img,box_coord,box_img,door_coord,door_img,key)

def debug(player_coord,player_img,wall_coord,box_coord,box_img,door_coord,door_img,key,key_coord,key_img,target_coord,height_window,width_window):

    '''
    Fonction permettant de déplacer le joueur de manière aléatoire dans tous les sens
    '''

    while True :
        Bug = donne_evenement()
        type_event_Bug=type_evenement(Bug)
        if type_event_Bug=='Touche':
            debug_touche = touche(Bug)
            if debug_touche=='v' or debug_touche=='V':#Si on appuie sur la touche de debug on arrete le mode
                return (player_coord,player_img,box_coord,box_img,door_coord,door_img,key,key_coord,key_img,target_coord)


        deplacement_random=randint(0,3)#On tire un nombre au hasard pour définir le déplacement du joueur
        if deplacement_random == 0 :
            player_coord,player_img,box_coord,box_img,door_coord,door_img,key = up(player_coord,player_img,wall_coord,box_coord,box_img,door_coord,door_img,key,height_window,width_window)

        elif deplacement_random == 1 :
            player_coord,player_img,box_coord,box_img,door_coord,door_img,key = down(player_coord,player_img,wall_coord,box_coord,box_img,door_coord,door_img,key,height_window,width_window)

        elif deplacement_random == 2 :
            player_coord,player_img,box_coord,box_img,door_coord,door_img,key = left(player_coord,player_img,wall_coord,box_coord,box_img,door_coord,door_img,key,height_window,width_window)

        elif deplacement_random == 3 :
            player_coord,player_img,box_coord,box_img,door_coord,door_img,key = right(player_coord,player_img,wall_coord,box_coord,box_img,door_coord,door_img,key,height_window,width_window)

        key = key_holder(key_coord,player_coord,key_img,key)

        victory_game = victory(box_coord,target_coord,box_img)
        if victory_game == True:
            return (player_coord,player_img,box_coord,box_img,door_coord,door_img,key,key_coord,key_img,target_coord)



########################### FONCTIONS DE COLISION   #######################################################################################

def colision_wall(coord_x,coord_y,wall_coord):

    '''
    Fonction qui vérifie qu'on ne rentre pas en colision avec un mur
    '''

    for element in wall_coord:
        if element[0]==coord_x:#On regarde si les coordonées x du mur correspondent à la coordonée x de notre objet
            if element[1]==coord_y:#puis pareil avec le y et si c'est le cas on retourne None qui dis que le personnage ou la boîte ne peuvent pas avancer
                return

    return True

def colision_box(coord_x,coord_y,box_coord):

    '''
    Fonction qui vérifie qu'on ne rentre pas en colision avec une boîte
    '''

    for element in box_coord:
        if element[0]==coord_x:
            if element[1]==coord_y:
                return

    return True

def colision_door(coord_x,coord_y,door_coord,door_img,key):

    '''
    Fonction qui vérifie qu'on ne rentre pas en colision avec une porte
    '''

    for i in range(len(door_coord)):
        if door_coord[i][0]==coord_x:
            if door_coord[i][1]== coord_y:
                key,door_coord= colision_door_key(i,door_coord,door_img,key)#On va aller regardé si les le joueur possède un clé ou non
                return

    return True

def colision_door_box(coord_x,coord_y,door_coord,door_img,key):

    '''
    Fonction qui regarde si la boîte qu'on déplace rentre en colision avec une porte
    '''

    for i in range(len(door_coord)):
        if door_coord[i][0]==coord_x:
            if door_coord[i][1]== coord_y:
                return

    return True

def colision_door_key(i,door_coord,door_img,key):

    '''
    Regarde si on possède une clé ou non pour ouvrir une porte
    '''

    if True in key:
        efface(door_img[i])
        key.pop()
        door_coord.pop(i)
        door_img.pop(i)

    return key,door_coord


###############################  FONTCTIONS D'AFFICHAGE #####################################################################################

def wall():

    '''
    On realise l'affichage des murs en fonction de la liste contenant la position des objets de la map
    '''
    wall_coord = []

    for i in range(len(map_game)):
        if map_game[i] == 'W':
            ax = (i % map_format) * case_size #On utilise le modulo de façon a obtenir la numérotation des lignes de notre élément, dans ce cas, W, map_format etant le nombre d'éléments
            ay = (i // map_format) * case_size #dans une ligne du jeu. Et avec le quotient on obtient la numérotation des colonnes de l'élément.
                                            #De plus on multiplie par case_size car cela represente la taille d'une case
            image(ax, ay, wall_gif, ancrage='nw', tag='')
            wall_coord.append((ax,ay))

            mise_a_jour()
    return(wall_coord)

def empty_case():

    '''
    On realise l'affichage du sol en fonction de la liste contenant la position des objets de la map
    '''

    for i in range(len(map_game)):
        if map_game[i] != 'W':
            ax = (i % map_format) * case_size
            ay = (i // map_format) * case_size
            image(ax, ay, floor_gif, ancrage='nw', tag='')


            mise_a_jour()

def box():

    '''
    On realise l'affichage des boites en fonction de la liste contenant la position des objets de la map
    '''

    box_coord = []
    box_img = []
    for i in range(len(map_game)):
        if 'B' in map_game[i] :
            ax = (i % map_format) * case_size
            ay = (i // map_format) * case_size
            if map_game[i]=='BT':
                box1 = image(ax, ay, box_ok_gif, ancrage='nw', tag='')
            else:
                box1 = image(ax, ay, box_gif, ancrage='nw', tag='')
            box_img.append(box1)

            box_coord.append([ax,ay])
            mise_a_jour()

    return(box_coord,box_img)

def door():

    '''
    On realise l'affichage des portes en fonction de la liste contenant la position des objets de la map
    '''

    door_coord = []
    door_img = []

    for i in range(len(map_game)):
        if map_game[i] == 'D':
            ax = (i % map_format) * case_size
            ay = (i // map_format) * case_size

            door1 = image(ax , ay, door_gif, ancrage='nw')
            door_img.append(door1)
            door_coord.append((ax,ay))
            mise_a_jour()

    return(door_coord,door_img)

def position_start():

    '''
    On declare la position de depart pour le joueur et on affiche le joueur sur cette position.
    '''

    for i in range(len(map_game)):
        if 'S' in map_game[i] :
            ax = ((i % map_format) * case_size)
            ay = ((i // map_format) * case_size)

            player_img = image(ax, ay, up_gif, ancrage='nw', tag='')
            mise_a_jour()
    player_coord =[ax,ay]

    return(player_img,player_coord)

def position_target():

    '''
    On declare la position des cibles pour les boites et on affiche une croix sur ces position.
    '''

    target_coord = []

    for i in range(len(map_game)):#modifier
        if 'T' in map_game[i]:
            ax = ((i % map_format) * case_size)
            ay = ((i // map_format) * case_size)
            image(ax, ay, target_gif, ancrage='nw', tag='')
            target_coord.append((ax,ay))
            mise_a_jour()
    return(target_coord)

def position_key():
    '''
    On declare la position des clés pour les boites et on affiche une clé sur ces position.
    '''
    key_coord = []
    key_img = []

    for i in range(len(map_game)):
        if map_game[i] == 'K':
            ax = ((i % map_format) * case_size)
            ay = ((i // map_format) * case_size)
            key1 = image(ax, ay, key_gif, ancrage='nw', tag='')
            key_coord.append((ax,ay))
            key_img.append(key1)
            mise_a_jour()

    return(key_coord,key_img)


############################################### FONCTIONS GAMEPLAY ######################################################

def key_holder(key_coord, player_coord,key_img,key):

    '''
    Fonction qui regarde si le joueur est placé sur une clé et si oui ajoute la clé dans la liste des clé du joueur
    '''

    for i in range(len(key_coord)):
        if player_coord[0] == key_coord[i][0] and player_coord[1] == key_coord[i][1]:
            key.append(True)

            efface(key_img[i])#Supprime la clé des images, des coordonées.
            key_coord.pop(i)
            key_img.pop(i)
            break

    return(key)

def victory(box_coord,target_coord,box_img):

    '''
    Fonction qui regarde s'il y a les boites dans les cibles et donc si le joueur à gagné
    '''

    victory_game = False
    counter_victory = 0
    for i in range (len(box_coord)):
        for j in range (len(target_coord)):

            if box_coord[i][0] == target_coord[j][0] and box_coord[i][1] == target_coord[j][1]:#Si on à une boites à les même coordonées que une cible
                efface(box_img[i])
                box_img[i]=image(box_coord[i][0],box_coord[i][1],box_ok_gif,ancrage='nw')#On met l'image boite OK
                counter_victory += 1 #et on ajoute 1 au ompteur
                break

            else:
                efface(box_img[i])
                box_img[i]=image(box_coord[i][0],box_coord[i][1],box_gif,ancrage='nw')

    if counter_victory == len(target_coord) :#Si le compteur vaut la longueur de target_coord on gagne
        victory_game = True


    return(victory_game)

def editeur(name_map):

    '''
    Depuis l'éditeur charger le jeu avec la carte qui vient d'être créée
    '''

    read_map(name_map)
    play()

def read_map(Editeur=None):

    '''
    Fonction qui permet de lire un fichier et d'obtenir la forme de la map
    '''

    global map_game, map_format, name_map

    if Editeur != None:#Pour quand on joue à partir de l'editeur on envoie le nom de la map depuis celui-ci
        name_map = Editeur

    map_txt = open('maps/'+name_map,"r")
    map_choose = map_txt.readline()#Pour ne pas prendre en compte titre ...
    map_game = []
    num_key=0

    for ligne in map_txt:
        if ligne[0]  not in "BTS.KWD" and ligne[0] != '':#Dans les fichiers de sauvegarde on enregistre le nombre de clé en mémoire donc cela permet de voir quand c'est le cas
            num_key=int(ligne.strip())
            continue
        lst_ligne = list(ligne [:-1])
        i=0
        while i != len(lst_ligne):
            if lst_ligne[i]=="|":#Lorsqu'on sauvegarde on peut avoir une boite sur un target c'est alors représenter avec des |BT|
                map_game.append(lst_ligne[i+1]+lst_ligne[i+2])
                i+=4
            else:
                map_game.append(lst_ligne[i])
                i+=1

        map_format = len (lst_ligne)
    map_txt.close()
    parametre()
    play(num_key)

def save(player_coord,box_coord,target_coord,key_coord,door_coord,wall_coord,name_map,key):

    '''
    Cette fonction lit la map et recrée une liste avec la disposition des differents objets à un instant donné.
    Elle enregistre par la suite cette disposition dans un fichier texte en tenant compte du bon format.
    '''

    map_game_save = []
    hauteur = ((len(map_game))//map_format)*int(case_size)

    for i in range(0,hauteur,int(case_size)):
        for j in range(0,(map_format*int(case_size)),int(case_size)):   #On lit la map et on regarde les coordonnées

            if [j,i] == player_coord:
                if tuple(player_coord) in target_coord:
                    map_game_save.append('|ST|')
                else:
                    map_game_save.append('S')

            elif [j,i] in box_coord:
                if tuple([j,i]) in target_coord:
                    map_game_save.append('|BT|')
                else:
                    map_game_save.append('B')


            elif (j,i) in target_coord:
                map_game_save.append('T')

            elif (j,i) in key_coord:
                map_game_save.append('K')

            elif (j,i) in door_coord:
                map_game_save.append('D')

            elif (j,i) in wall_coord:
                map_game_save.append('W')

            else:
                map_game_save.append('.')

    x = 1

    with open('maps/'+name_map+"_save",'w') as save_file:   #On crée un fichier sauvegarde
        save_file.write('Titre: "save"')
        save_file.write('\n')

        for i in range(len(map_game_save)):


            if i == (map_format*x)-1:
                save_file.write(map_game_save[i])
                save_file.write('\n')
                x+=1


            else:
                save_file.write(map_game_save[i])

        save_file.write(str(len(key)))
        print("Votre map a ete sauvegarde avec le nom " + name_map+"_save" + " dans le repertoire maps.")

def parametre():

    '''
    Fonction permettant de redéfinir la taille des images
    '''

    global case_size,box_gif,floor_gif,floor_gif,key_gif,door_gif,target_gif,wall_gif,right_gif,left_gif,up_gif,down_gif,box_ok_gif

    cree_fenetre(500,500)
    taille_img=50
    tuple_img=("box.gif","floor.gif","key.gif","door.gif","target.gif","wall.gif","player_r.gif","player_l.gif","player_u.gif","player_d.gif","box_ok.gif")
    width_case = round(((500//map_format)/taille_img),1)
    print(map_format,len(map_game))
    height_case = round(((500//(len(map_game)//map_format))/taille_img),1)#On définit la taille possible en hauteur et largeur des cases
    texte1=texte(250,250,"En Chargement ...",ancrage='center',police='Purisa',taille=20)
    mise_a_jour()

    if height_case >= width_case and width_case<1 :#En fonction du faite que la hauteur soit plus grande ou plus petite que la largeur on redéfini la taille des image de manières
                                                    #à avoir un jeu qui s'adapte à la taille de la map
        case_size = taille_img*width_case
        for element in (tuple_img):
            img=create(element,int(width_case*10),10)#On envoie le nombre de colonne et de ligne qu'il faut supprimer afin de modifier la taille de l'image, fonction du module Redim_img

        box_gif = "box_redim.gif"
        floor_gif = "floor_redim.gif"
        key_gif = "key_redim.gif"
        door_gif = "door_redim.gif"
        target_gif = "target_redim.gif"
        wall_gif = "wall_redim.gif"
        right_gif = "player_r_redim.gif"
        left_gif = "player_l_redim.gif"
        up_gif = "player_u_redim.gif"
        down_gif = "player_d_redim.gif"
        box_ok_gif="box_ok_redim.gif"

    elif width_case > height_case and height_case<1 :#Ici la largeur est plus grande que la hauteur donc on établit la taille des cases en fonction de la largeur
        case_size = taille_img*height_case
        for element in (tuple_img):
            img=create(element,int(height_case*10),10)


        box_gif = "box_redim.gif"
        floor_gif = "floor_redim.gif"
        key_gif = "key_redim.gif"
        door_gif = "door_redim.gif"
        target_gif = "target_redim.gif"
        wall_gif = "wall_redim.gif"
        right_gif = "player_r_redim.gif"
        left_gif = "player_l_redim.gif"
        up_gif = "player_u_redim.gif"
        box_ok_gif="box_ok_redim.gif"
        down_gif = "player_d_redim.gif"

    else:
        case_size=taille_img
        box_gif = "box.gif"
        floor_gif = "floor.gif"
        key_gif = "key.gif"
        door_gif = "door.gif"
        target_gif = "target.gif"
        wall_gif = "wall.gif"
        right_gif = "player_r.gif"
        left_gif = "player_l.gif"
        up_gif = "player_u.gif"
        down_gif = "player_d.gif"
        box_ok_gif="box_ok.gif"
    efface(texte1)
    texte(250,230,"Chargement fini, vous pouvez",ancrage='center',police='Purisa',taille=20)
    texte(250,270,  "Cliquez pour jouer",ancrage='center',police='Purisa',taille=20)
    attente_clic()
    mise_a_jour()
    ferme_fenetre()

def remove_img(box_gif):

    '''
    Fonction qui supprime les images redimensionnées
    '''

    L=["box_redim.gif","box_ok_redim.gif","floor_redim.gif","key_redim.gif","door_redim.gif","target_redim.gif","wall_redim.gif","player_r_redim.gif","player_l_redim.gif","player_u_redim.gif","player_d_redim.gif"]

    if L[0] == box_gif:#On regarde si box_gif est redimensionné on supprime alors les images
        for el in L:
            supprime(el)


##################### FONCTION SOLUTION ###################

def result(num_key):

    '''
    Fonction qui permet de faire bouger le joueur en lisant un chemin indiquant la réponse
    '''

    lst_result=list(os.listdir('result'))
    print(name_map)
    if name_map in lst_result:
        with open("result/"+name_map,'r') as file:

            lst_move=file.read()
            ferme_fenetre()
            width_window = map_format * case_size
            height_window = (len(map_game)//map_format)*case_size
            cree_fenetre(width_window,height_window)
            wall_coord = wall()
            empty_case()
            box_coord,box_img = box()
            door_coord,door_img = door()
            player_img,player_coord = position_start()
            target_coord = position_target()
            key_coord,key_img = position_key()
            key = []
            victory_game = False#On redéfinie tout les paramètres de jeu

            for element in lst_move:#Et on déplace le joueur en fonction des déplacement écrit dans le fichier
                sleep(0.2)
                mise_a_jour()
                efface('text')
                texte(5, 5, 'Clés:'+str(len(key)), couleur='white', ancrage='nw', police='Purisa', taille=10, tag='text')
                if  element == 'Q':
                    player_coord,player_img,box_coord,box_img,door_coord,door_img,key  = left(player_coord,player_img,wall_coord,box_coord,box_img,door_coord,door_img,key,height_window,width_window)
                elif element == 'D':
                    player_coord,player_img,box_coord,box_img,door_coord,door_img,key = right(player_coord,player_img,wall_coord,box_coord,box_img,door_coord,door_img,key,height_window,width_window)
                elif element == 'S':
                    player_coord,player_img,box_coord,box_img,door_coord,door_img,key = down(player_coord,player_img,wall_coord,box_coord,box_img,door_coord,door_img,key,height_window,width_window)
                elif element == 'Z':
                    player_coord,player_img,box_coord,box_img,door_coord,door_img,key  = up(player_coord,player_img,wall_coord,box_coord,box_img,door_coord,door_img,key,height_window,width_window)
                key = key_holder(key_coord,player_coord,key_img,key)

                victory_game = victory(box_coord,target_coord,box_img)
                if victory_game == True:
                    texte(width_window//2, height_window//2, "Voila comment gagner", couleur='white', ancrage='center', police='Purisa', taille=int(width_window//20), tag='text')
                    texte(width_window//2, height_window//2+height_window//7,"Le jeu va redémarrer", couleur='white', ancrage='center', police='Purisa', taille=int(width_window//20), tag='text')
                    mise_a_jour()
    else:
        ferme_fenetre()
        cree_fenetre(500,500)
        mise_a_jour()
        texte(250,230, "Il n'y a pas de solution existante !", couleur='black', ancrage='center', police='Purisa', taille=15, tag='text')
        texte(250,260, "Le jeu va donc redémarrer", couleur='black', ancrage='center', police='Purisa', taille=15, tag='text')
        mise_a_jour()


    sleep(2)
    efface_tout()
    ferme_fenetre()
    play(num_key)

def read_result(num_key):

    '''
    Fonction qui permet d'écrire le chemin de réponse dans un fichier
    '''

    with open("result/"+name_map,'w') as file:

            ferme_fenetre()
            width_window = map_format * case_size
            height_window = (len(map_game)//map_format)*case_size
            cree_fenetre(width_window,height_window)
            wall_coord = wall()
            empty_case()
            box_coord,box_img = box()
            door_coord,door_img = door()
            player_img,player_coord = position_start()
            target_coord = position_target()
            key_coord,key_img = position_key()
            key = []
            victory_game = False
            remove=False

            while victory_game == False:
                mise_a_jour()
                efface('text')
                texte(5, 5, 'Clés:'+str(len(key)), couleur='white', ancrage='nw', police='Purisa', taille=10, tag='text')
                event = donne_evenement()
                type_event = type_evenement(event)
                if type_event=='Touche':
                    nom_touche = touche(event)

                    #On ajoute la direction pressée par le joueur dans le fichier de réponse
                    if nom_touche == 'Left' or nom_touche == 'q' or nom_touche == 'Q':
                        player_coord,player_img,box_coord,box_img,door_coord,door_img,key  = left(player_coord,player_img,wall_coord,box_coord,box_img,door_coord,door_img,key,height_window,width_window)
                        file.write('Q')
                    elif nom_touche == 'Right' or nom_touche == 'd' or nom_touche == 'D':
                        player_coord,player_img,box_coord,box_img,door_coord,door_img,key = right(player_coord,player_img,wall_coord,box_coord,box_img,door_coord,door_img,key,height_window,width_window)
                        file.write('D')
                    elif nom_touche == 'Down' or nom_touche == 's' or nom_touche == 'S':
                        player_coord,player_img,box_coord,box_img,door_coord,door_img,key = down(player_coord,player_img,wall_coord,box_coord,box_img,door_coord,door_img,key,height_window,width_window)
                        file.write('S')
                    elif nom_touche == 'Up' or nom_touche == 'z' or nom_touche == 'Z':
                        player_coord,player_img,box_coord,box_img,door_coord,door_img,key  = up(player_coord,player_img,wall_coord,box_coord,box_img,door_coord,door_img,key,height_window,width_window)
                        file.write('Z')

                    elif nom_touche == 'f' or nom_touche == 'F':
                        remove=True#Si on arrête d'écrire la réponse remove devient True
                        break

                key = key_holder(key_coord,player_coord,key_img,key)
                victory_game = victory(box_coord,target_coord,box_img)
                if victory_game == True:
                    texte(width_window//2, height_window//2, "Vous avez trouver comment gagner !", couleur='white', ancrage='center', police='Purisa', taille=int(width_window//25), tag='text')
                    texte(width_window//2, height_window//2+height_window//7,"Le jeu va redémarrer", couleur='white', ancrage='center', police='Purisa', taille=int(width_window//25), tag='text')
                    mise_a_jour()
                    break

    if remove == True:
        os.remove("result/"+name_map)#On supprime le fichier car il n'est pas complet
        texte(width_window//2, height_window//2, "Vous avez annulé la solution !", couleur='white', ancrage='center', police='Purisa', taille=int(width_window//20), tag='text')
        texte(width_window//2, height_window//2+height_window//7,"Le jeu va redémarrer", couleur='white', ancrage='center', police='Purisa', taille=int(width_window//20), tag='text')
        mise_a_jour()

    sleep(2)
    efface_tout()
    ferme_fenetre()
    play(num_key)


############ FONCTION MENU ####################

def menu():
    '''
    Cette fonction permet d'afficher le menu avant le debut du jeu
    '''

    cree_fenetre(500,500)

    image(0, 0, 'background.gif', ancrage='nw')

    #On affiche un titre et 3 options

    texte(250-(longueur_texte('SOKOBAN')//2), 20, 'SOKOBAN', couleur='white', ancrage='nw', police='Purisa', taille=24, tag='')

    play_width = longueur_texte('JOUER')
    texte(250-(play_width//2), 150, 'JOUER', couleur='red', ancrage='nw', police='Purisa', taille=24, tag='')
    rectangle(250 - play_width//2, 148, 250 + play_width//2, 200, couleur='white')

    edit_width = longueur_texte('Editeur')
    texte(250-(edit_width//2), 230, 'Editeur', couleur='red', ancrage='nw', police='Purisa', taille=24, tag='')
    rectangle(250 - edit_width//2, 228, 250 + edit_width//2, 280, couleur='white')

    quit_width = longueur_texte('Quitter')
    texte(250-(quit_width//2), 310, 'Quitter', couleur='red', ancrage='nw', police='Purisa', taille=24, tag='')
    rectangle(250 - quit_width//2, 308, 250 + edit_width//2, 360, couleur='white')

    keys_width = longueur_texte('Touches')
    texte(25, 495-hauteur_texte(), 'Touches', couleur='red', ancrage='nw', police='Purisa', taille=17, tag='')


    while True:

        mise_a_jour()


        event = donne_evenement()
        type_event = type_evenement(event)

        lst_maps = list(os.listdir('maps'))
        lst_maps.sort()

        if type_event == 'ClicDroit' or type_event == 'ClicGauche':
            coord_clic = (clic_x(event), clic_y(event))

            if (250 - edit_width//2) <= coord_clic[0] <= (250 + edit_width//2) and 228 <= coord_clic[1] <= 280:
                menu_maps_editeur(lst_maps)

            if (250 - quit_width//2) <= coord_clic[0] <= (250 + quit_width//2) and 308 <= coord_clic[1] <= 360:
                exit()

            if (250 - play_width//2) <= coord_clic[0] <= (250 + play_width//2) and 148 <= coord_clic[1] <= 200:
                menu_maps(lst_maps)

            if 25 <= coord_clic[0] <= (25 + keys_width) and 440 <= coord_clic[1] <= 490:
                menu_keys()

def menu_maps(lst_maps):
    '''
    Cette fonction permet l'affichage des maps pour que le joueur puisse choisir son niveau sans avoir a interagir avec un terminal.
    De plus cette fonction peut aussi faire débuter le jeu en faisant appel a la fonction "play"
    '''

    efface_tout()
    x = 0
    text_width = longueur_texte(lst_maps[x])
    text_height = hauteur_texte()
    y_text = 100
    lst_window = []
    background = True


    while True:

        if background == True:
            image(0, 0, 'background.gif', ancrage='nw')
            background = False

        if x < len(lst_maps):
            text_width = longueur_texte(lst_maps[x])
            text_height = hauteur_texte()

            if y_text < 350:
                texte(250, y_text, lst_maps[x], couleur='red', ancrage='center', police='Purisa', taille=20, tag='')
                rectangle(250 - text_width//2, y_text-20, 250 + text_width//2, y_text+20, couleur='white')

                if x < len(lst_maps)-3: #Cette condition permet d'afficher une fleche seulement s'il existent des maps suffisants pour créer une nouvelle page
                    rectangle(300,400,400, 460, couleur='black')
                    ligne(315, 430, 375, 430, couleur='white', epaisseur=1, tag='')
                    ligne(350, 420, 375, 430, couleur='white', epaisseur=1, tag='')
                    ligne(350, 440, 375, 430, couleur='white', epaisseur=1, tag='')

                if x > 3: #De même pour cette fonction seulement si on dépasse la limite de maps par fenetre (dans ce cas 3 maps)

                    rectangle(100,400,200, 460, couleur='black')
                    ligne(115, 430, 175, 430, couleur='white', epaisseur=1, tag='')
                    ligne(140, 420, 115, 430, couleur='white', epaisseur=1, tag='')
                    ligne(140, 440, 115, 430, couleur='white', epaisseur=1, tag='')


                rectangle(15,15,115, 65, couleur='white')
                texte(65, 40, "MENU", couleur='purple', ancrage='center', police='Purisa', taille=20, tag='')

                lst_window.append(lst_maps[x])
                x += 1

        mise_a_jour()
        event = donne_evenement()
        type_event = type_evenement(event)

        if type_event == 'ClicDroit' or type_event == 'ClicGauche':
            coord_clic = (clic_x(event), clic_y(event))

            if  15 <= coord_clic[0] <= 115 and 15 <= coord_clic[1] <= 65:
                ferme_fenetre()
                menu()

            if 250 - (longueur_texte(lst_window[0])//2) <= coord_clic[0] <= 250 + (longueur_texte(lst_window[0])//2) and 80 <= coord_clic[1] <= 120:
                name_map = lst_window[0]
                ferme_fenetre()
                read_map(name_map)

            if len(lst_window) > 1 and 250 - (longueur_texte(lst_window[1])//2) <= coord_clic[0] <= 250 + (longueur_texte(lst_window[1])//2) and 180 <= coord_clic[1] <= 220:
                name_map = lst_window[1]
                ferme_fenetre()
                read_map(name_map)

            if len(lst_window) > 2 and 250 - (longueur_texte(lst_window[2])//2) <= coord_clic[0] <= 250 + (longueur_texte(lst_window[2])//2) and 280 <= coord_clic[1] <= 320:
                name_map = lst_window[2]
                ferme_fenetre()
                read_map(name_map)

            if 300 <= coord_clic[0] <= 400 and 400 <= coord_clic[1] <= 460 and x < len(lst_maps):    #Fleche avant
                efface_tout()
                background = True
                lst_window = []
                y_text = 0

            if  100 <= coord_clic[0] <= 200 and 400 <= coord_clic[1] <= 460:    #Fleche arriere
                if x <= 3:
                    continue

                background = True
                efface_tout()
                x = x-(len(lst_window))-3
                y_text = 0
                lst_window = []

        y_text += 100

def menu_maps_editeur(lst_maps):
    '''
    Cette fonction permet l'affichage d'un menu pour pouvoir gérer l'editeur de maps. Ce sous-menu permet à l'utilisateur de choisir
    entre éditer une map existante ou créer une nouvelle.
    '''

    efface_tout()
    choix = None
    image(0, 0, 'background.gif', ancrage='nw')


    rectangle(250-longueur_texte("Créer map"),125-hauteur_texte()//2, 250+longueur_texte("Créer map"), 125+hauteur_texte()//2, couleur='white')
    texte(250, 125, "Créer map", couleur='red', ancrage='center', police='Purisa', taille=20, tag='')
    rectangle(250-longueur_texte("Utiliser Map existante")//2,375-hauteur_texte()//2, 250+longueur_texte("Utiliser Map existante")//2, 375+hauteur_texte()//2, couleur='white')
    texte(250, 375, "Utiliser Map existante", couleur='red', ancrage='center', police='Purisa', taille=20, tag='')
    rectangle(15,15,115, 65, couleur='white')
    texte(65, 40, "MENU", couleur='purple', ancrage='center', police='Purisa', taille=20, tag='')

    while True:

        mise_a_jour()

        event = donne_evenement()
        type_event = type_evenement(event)

        if type_event == 'ClicDroit' or type_event == 'ClicGauche':
            coord_clic = (clic_x(event), clic_y(event))

            if  15 <= coord_clic[0] <= 115 and 15 <= coord_clic[1] <= 65:
                ferme_fenetre()
                menu()

            if 250-longueur_texte("Créer map") <= coord_clic[0] <= 250+longueur_texte("Créer map") and 125-hauteur_texte()//2 <= coord_clic[1] <= 125+hauteur_texte()//2:
                rows = int(input("Nombre de lignes pour votre map? "))      #Permet au joueur de choisir la taille de la nouvelle map
                columns = int(input("Nombre de colonnes pour votre map? "))
                ferme_fenetre()
                edit_map(col=columns,lig=rows)

            if 250-longueur_texte("Utiliser Map existante")//2 <= coord_clic[0] <= 250+longueur_texte("Utiliser Map existante")//2 and 375-hauteur_texte()//2 <= coord_clic[1] <= 375+hauteur_texte()//2:
                break


    x = 0
    text_width = longueur_texte(lst_maps[x])
    text_height = hauteur_texte()
    y_text = 100
    lst_window = []
    background = True


    while True:

        if background == True:
            image(0, 0, 'background.gif', ancrage='nw')
            background = False



        if x <= len(lst_maps)-1:
            text_width = longueur_texte(lst_maps[x])
            text_height = hauteur_texte()

            if y_text < 350:
                texte(250, y_text, lst_maps[x], couleur='red', ancrage='center', police='Purisa', taille=20, tag='')
                rectangle(250 - text_width//2, y_text-20, 250 + text_width//2, y_text+20, couleur='white')

                if x < len(lst_maps)-3:

                    rectangle(300,400,400, 460, couleur='black')
                    ligne(315, 430, 375, 430, couleur='white', epaisseur=1, tag='')
                    ligne(350, 420, 375, 430, couleur='white', epaisseur=1, tag='')
                    ligne(350, 440, 375, 430, couleur='white', epaisseur=1, tag='')

                if x > 3:

                    rectangle(100,400,200, 460, couleur='black')
                    ligne(115, 430, 175, 430, couleur='white', epaisseur=1, tag='')
                    ligne(140, 420, 115, 430, couleur='white', epaisseur=1, tag='')
                    ligne(140, 440, 115, 430, couleur='white', epaisseur=1, tag='')


                rectangle(15,15,115, 65, couleur='white')
                texte(65, 50, "MENU", couleur='purple', ancrage='center', police='Purisa', taille=20, tag='')

                lst_window.append(lst_maps[x])
                x += 1

        mise_a_jour()
        event = donne_evenement()
        type_event = type_evenement(event)

        if type_event == 'ClicDroit' or type_event == 'ClicGauche':
            coord_clic = (clic_x(event), clic_y(event))

            if  15 <= coord_clic[0] <= 115 and 15 <= coord_clic[1] <= 65:
                ferme_fenetre()
                menu()

            if 250 - (longueur_texte(lst_window[0])//2) <= coord_clic[0] <= 250 + (longueur_texte(lst_window[0])//2) and 80 <= coord_clic[1] <= 120:
                name_map = lst_window[0]
                ferme_fenetre()
                edit_map(name_map)

            if 250 - (longueur_texte(lst_window[1])//2) <= coord_clic[0] <= 250 + (longueur_texte(lst_window[1])//2) and 180 <= coord_clic[1] <= 220:
                name_map = lst_window[1]
                ferme_fenetre()
                edit_map(name_map)

            if len(lst_window) > 2 and 250 - (longueur_texte(lst_window[2])//2) <= coord_clic[0] <= 250 + (longueur_texte(lst_window[2])//2) and 280 <= coord_clic[1] <= 320:
                name_map = lst_window[2]
                ferme_fenetre()
                edit_map(name_map)

            if  300 <= coord_clic[0] <= 400 and 400 <= coord_clic[1] <= 460 and x < len(lst_maps)-1:
                efface_tout()
                y_text = 0
                lst_window = []
                background = True

            if  100 <= coord_clic[0] <= 200 and 400 <= coord_clic[1] <= 460:
                if x <= 3:
                    continue

                efface_tout()
                x = x-(len(lst_window))-3
                y_text = 0
                lst_window = []
                background = True

        y_text += 100

def menu_keys():
    '''
    Cette fonction permet l'affichage d'une fenetre indiquant au joueur quels sont les touches définies pour le jeu.
    '''

    efface_tout()
    image(0, 0, 'background.gif', ancrage='nw')

    texte(250, 30, 'TOUCHES', couleur='white', ancrage='center', police='Purisa', taille=24, tag='')

    rectangle(15,15,115, 65, couleur='white')
    texte(65, 40, "Retour", couleur='white', ancrage='center', police='Purisa', taille=15, tag='')

    texte(250, 100, 'UP = Z', couleur='red', ancrage='center', police='Purisa', taille=15, tag='')
    texte(250, 136, 'DOWN = S', couleur='red', ancrage='center', police='Purisa', taille=15, tag='')
    texte(250, 172, 'RIGHT = D', couleur='red', ancrage='center', police='Purisa', taille=15, tag='')
    texte(250, 208, 'LEFT = Q', couleur='red', ancrage='center', police='Purisa', taille=15, tag='')
    texte(250, 244, 'MENU = M', couleur='red', ancrage='center', police='Purisa', taille=15, tag='')
    texte(250, 280, 'DEBUG = V', couleur='red', ancrage='center', police='Purisa', taille=15, tag='')
    texte(250, 316, 'RESTART = R', couleur='red', ancrage='center', police='Purisa', taille=15, tag='')
    texte(250, 352, 'SAVE = B', couleur='red', ancrage='center', police='Purisa', taille=15, tag='')
    texte(250, 388, 'EDITEUR = E', couleur='red', ancrage='center', police='Purisa', taille=17, tag='')
    texte(250, 424, 'CONSTRUIRE CHEMIN REPONSE = F', couleur='red', ancrage='center', police='Purisa', taille=17, tag='')
    texte(250, 460, 'EXECUTER CHEMIN = G', couleur='red', ancrage='center', police='Purisa', taille=17, tag='')

    while True:

        mise_a_jour()

        event = donne_evenement()
        type_event = type_evenement(event)

        if type_event == 'ClicDroit' or type_event == 'ClicGauche':
            coord_clic = (clic_x(event), clic_y(event))

            if  15 <= coord_clic[0] <= 115 and 15 <= coord_clic[1] <= 65:
                ferme_fenetre()
                menu()

################## FONCTION MAIN ########################

def play(num_key=0):

    '''
    Fonction principale qui permet de faire fonctionner tout le jeu en faisant appel aux fonctions nécessaires.
    '''

    width_window = map_format * case_size
    height_window = (len(map_game)//map_format)*case_size
    cree_fenetre(width_window,height_window)
    wall_coord = wall()
    empty_case()
    target_coord = position_target()
    box_coord,box_img = box()
    door_coord,door_img = door()
    player_img,player_coord = position_start()
    key_coord,key_img = position_key()
    key = [True]*num_key

    texte(5, 5, 'Clés:'+str(len(key)), couleur='white', ancrage='nw', police='Purisa', taille=10, tag='text')
    victory_game = False



    while victory_game == False:
        mise_a_jour()
        efface('text')
        texte(5, 5, 'Clés:'+str(len(key)), couleur='white', ancrage='nw', police='Purisa', taille=10, tag='text')

        event = donne_evenement() #Permet de definir quel evenement s'est produit avec le clavier ou la souris
        type_event = type_evenement(event) #nous donne que le type de l'evenement

        if type_event=='Touche':
            nom_touche = touche(event) #nous donne le nom de la touche pressée


            if nom_touche == 'Left' or nom_touche == 'q' or nom_touche == 'Q':
                player_coord,player_img,box_coord,box_img,door_coord,door_img,key  = left(player_coord,player_img,wall_coord,box_coord,box_img,door_coord,door_img,key,height_window,width_window)
            elif nom_touche == 'Right' or nom_touche == 'd' or nom_touche == 'D':
                player_coord,player_img,box_coord,box_img,door_coord,door_img,key = right(player_coord,player_img,wall_coord,box_coord,box_img,door_coord,door_img,key,height_window,width_window)
            elif nom_touche == 'Down' or nom_touche == 's' or nom_touche == 'S':
                player_coord,player_img,box_coord,box_img,door_coord,door_img,key = down(player_coord,player_img,wall_coord,box_coord,box_img,door_coord,door_img,key,height_window,width_window)
            elif nom_touche == 'Up' or nom_touche == 'z' or nom_touche == 'Z':
                player_coord,player_img,box_coord,box_img,door_coord,door_img,key  = up(player_coord,player_img,wall_coord,box_coord,box_img,door_coord,door_img,key,height_window,width_window)
            elif nom_touche == 'v' or nom_touche == 'V':
                player_coord,player_img,box_coord,box_img,door_coord,door_img,key,key_coord,key_img,target_coord = debug(player_coord,player_img,wall_coord,box_coord,box_img,door_coord,door_img,key,key_coord,key_img,target_coord,height_window,width_window)

            elif nom_touche == 'b' or nom_touche == 'B':
                save(player_coord,box_coord,target_coord,key_coord,door_coord,wall_coord,name_map,key)

            elif nom_touche == 'r' or nom_touche == 'R':#On recommence le niveau
                ferme_fenetre()
                play()

            elif nom_touche == 'm' or nom_touche == 'M':#On revient au menu
                ferme_fenetre()
                remove_img(box_gif)
                menu()

            elif nom_touche=='e' or nom_touche=='E':#On va à l'éditeur
                ferme_fenetre()
                edit_map(name_map)

            elif nom_touche == 'g' or nom_touche=='G':#On regarde le chemin pour gagner
                result(num_key)

            elif nom_touche == 'f' or nom_touche=='F':#On écrit le fichier le réponse
                read_result(num_key)

            key = key_holder(key_coord,player_coord,key_img,key)

            victory_game = victory(box_coord,target_coord,box_img)
            if victory_game == True:
                longe=longueur_texte("Gagne")/2
                haut=hauteur_texte()
                texte(width_window/2-longe,height_window/2-haut ,"Gagne",couleur='yellow')
                remove_img(box_gif)

                while True :
                        mise_a_jour()
                        event2 = donne_evenement()
                        type_event2 = type_evenement(event2)
                        if type_event2=='Touche':
                            nom_touche2 = touche(event2)


                            if nom_touche2 == 'r' or nom_touche2 == 'R':
                                ferme_fenetre()
                                read_map()
                                play()

                            elif nom_touche2=='e' or nom_touche2=='E':
                                ferme_fenetre()
                                edit_map(name_map)

                            elif nom_touche2=='m' or nom_touche2=='M':
                                ferme_fenetre()
                                menu()

                        if type_event2 == 'ClicGauche':
                                ferme_fenetre()
                                menu()
                ferme_fenetre()

if __name__ == '__main__':
    menu()
