from tkinter import *
import os

def create(file_img,Colonne_keep,Colonne_total):
    
    '''
    Fonction main du module
    '''

    # création d'un canvas pour photo #
    window = Tk()
    window.geometry("0x0")
    telephone= Canvas(window)
    telephone.pack()
    img=PhotoImage(file=file_img)#On crée un fenêtre vide à l'aide de tkinter afin de créer un objet PhotoImage et de pouvoir obtenir la matrice de celui-ci 

    ######## obtention de la matrice et travail sur la matrice #########
    M=matrix(img)
    M=redim(M,Colonne_keep,Colonne_total)
    M2,img=retransformer_img(M,img)
    write_img(M2,img,file_img)
    window.destroy()

def matrix(img):
    
    '''
    Fonction pour obtenir la matrice de l'image
    '''    


    M = [[img.get(j, i) for j in range(img.width())]  for i in range(img.height())]#get (j,i) car inverser comparer au canvas
    
    return M

def redim(M,Colonne_keep,Colonne_total):

    '''
    Fonction recréant la matrice selon la taille voulu pour le jeu
    '''

    colonne_loose=Colonne_total-Colonne_keep #le nombre de colonne sur lesquelles on veutt travailler et le nombre qu'on veut garder ex:1/4 je garde 1 colonne sur 4
    tuple_result=tuple(range(colonne_loose))

    i=0
    count=0
    while True:
        if (count %Colonne_total) in tuple_result:#on supprime un colonne si celle-ci à un numéro de colonne à supprimer
            M.pop(i)
        else:
            i+=1
        if i == len(M):
            break
        count+=1
        j=0
        counter = 0
        while j < len(M[i]):#Dans chaque ligne on supprime j s'il appartient au tuple des colonnes et lignes à supprimer

            if (counter %Colonne_total) in tuple_result:
                M[i].pop(j)
            else:
                j+=1
            counter+=1
    return M

def retransformer_img(M,img):

    '''
    Remettre la matrice en format hexadecimal
    '''
    
    img.blank()#On rénitialsie l'image pour qu'elle soit vide
    img=PhotoImage(width=len(M[0]), height=len(M))#On crée une image de la dimension voulu

    M2=[]
    for i in range(len(M)):#On tranforme chaque tuple (rgb) en code hexadécimal
        liste=[]
        for j in range(len(M[i])):
            pixel = "#%02x%02x%02x"  % M[i][j]
            liste.append(pixel)
        M2.append(" ".join(liste))

    
    return M2,img

def write_img(M2,img,file_img):

    '''
    On enregistre l'image grâce à cette fonction
    '''

    y = " ".join([ligne.join("{}") for ligne in M2])#On vient joindre des accolades avec les lignes car c'est le format utiliser pour réécrire une image, ex: {#00000 #1233FF} {#FFFFFF #111111}
    img.put(y, to=(0,0))#On vient mettre dans l'objet PhotoImage notre chaine de caractère contenant la matrice de l'image
    img.write(file_img[:-4]+"_redim.gif")#Et on sauvegarde l'image

def supprime(file):
    
    '''
    Fonction permettant de supprimer des images
    '''
    os.remove(file)
    

if __name__ == "__main__":
    pass
    
    
    
    
   
    
