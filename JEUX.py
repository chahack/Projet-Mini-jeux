from bibliotheque import *
import tkinter.font as tkFont
from copy import deepcopy
import subprocess
import sys


def menu() :
    """
    Affiche un menu proposant les différents jeux.
    """
    
    valeur = largeur_plateau/4
    
    # Fond du menu
    
    rectangle(0, 0, largeur_plateau-1, hauteur_plateau-1, couleur = 'black', remplissage = 'white', epaisseur = 3)
    texte(largeur_plateau/2, 2*contour, "JEUX", couleur = 'black', ancrage = 'center', police = 'Times new roman', taille = 30)
    ligne(valeur, 4*contour-ecart_boutons, 3*valeur, 4*contour-ecart_boutons, couleur = 'black', epaisseur = 1) 
    
    hauteur_bouton_menu = (hauteur_plateau-8*contour-2*ecart_boutons)/3
    largeur_bouton_menu = (largeur_plateau-8*contour)/2
    
    # Boutons de gauche
    
    rectangle(2*contour, 5*contour, largeur_bouton_menu+2*contour, 5*contour+hauteur_bouton_menu, couleur = 'black', remplissage = '#84d3ea', epaisseur = 2)
    rectangle(2*contour, 6*contour+hauteur_bouton_menu, largeur_bouton_menu+2*contour,6*contour+2*hauteur_bouton_menu, couleur = 'black', remplissage = '#43acca', epaisseur = 2)
    rectangle(2*contour, 7*contour+2*hauteur_bouton_menu, largeur_bouton_menu+2*contour,7*contour+3*hauteur_bouton_menu, couleur = 'black', remplissage = '#178daf', epaisseur = 2)
    
    texte(2*contour+largeur_bouton_menu/2, 5*contour+hauteur_bouton_menu/2, "LUNAR LANDER", couleur = "white", ancrage = 'center', police = 'Times new roman', taille = 25)
    texte(2*contour+(largeur_bouton_menu/2), 6*contour+hauteur_bouton_menu/2+hauteur_bouton_menu, "SNAKE", couleur = "white", ancrage = 'center', police = 'Times new roman', taille = 25)
    texte(2*contour+largeur_bouton_menu/2, 7*contour+hauteur_bouton_menu/2+2*hauteur_bouton_menu, "HITORI", couleur = "white", ancrage = 'center', police = 'Times new roman', taille = 25)
    
    # Boutons de droite
    
    rectangle(6*contour+largeur_bouton_menu, 5*contour, largeur_plateau-2*contour, 5*contour+hauteur_bouton_menu, couleur = 'black', remplissage = '#097897', epaisseur = 2)
    rectangle(6*contour+largeur_bouton_menu, 6*contour+hauteur_bouton_menu, largeur_plateau-2*contour,6*contour+2*hauteur_bouton_menu, couleur = 'black', remplissage = '#025b74', epaisseur = 2)
    rectangle(6*contour+largeur_bouton_menu, 7*contour+2*hauteur_bouton_menu, largeur_plateau-2*contour,7*contour+3*hauteur_bouton_menu, couleur = 'black', remplissage = '#a6a6a6', epaisseur = 2)
    
    texte(largeur_plateau-2*contour-largeur_bouton_menu/2, 5*contour+hauteur_bouton_menu/2, "MORPION", couleur = "white", ancrage = 'center', police = 'Times new roman', taille = 25)
    texte(largeur_plateau-2*contour-largeur_bouton_menu/2, 6*contour+hauteur_bouton_menu/2+hauteur_bouton_menu, "SUDOKU", couleur = "white", ancrage = 'center', police = 'Times new roman', taille = 25)
    texte(largeur_plateau-2*contour-(largeur_bouton_menu/2), 7*contour+(hauteur_bouton_menu/2)+2*hauteur_bouton_menu, "QUITTER", couleur = "white", ancrage = 'center', police = 'Times new roman', taille = 25)
    
    # Definition de la grille en fonction du clic
    
    x,y = attend_clic_gauche()
    
    jeu = None
    
    if x >= 2*contour and x <= largeur_bouton_menu+2*contour :
        
        if y >= 5*contour and y <= 5*contour+hauteur_bouton_menu :
            
            jeu = "lunar_lander.py"
            
        elif y >= 6*contour+hauteur_bouton_menu and y <= 6*contour+2*hauteur_bouton_menu :
            
            jeu = "snake.py"
                
        elif y >= 7*contour+2*hauteur_bouton_menu and y <= 7*contour+3*hauteur_bouton_menu :
            
            jeu = "hitori.py"

    if x >= 6*contour+largeur_bouton_menu and x <= largeur_plateau-2*contour :
            
        if y >= 5*contour and y <= 5*contour+hauteur_bouton_menu :
            
            jeu = "morpion.py"

        elif y >= 6*contour+hauteur_bouton_menu and y <= 6*contour+2*hauteur_bouton_menu :
            
            jeu = "sudoku.py"

        elif y >= 7*contour+2*hauteur_bouton_menu and y <= 7*contour+3*hauteur_bouton_menu :    
            
            jeu = False
    
    return jeu


# INITIALISATION


contour = 30

largeur_plateau = 1090 
hauteur_plateau = 660

nb_boutons = 13

ecart_boutons = 15

largeur_bouton = 200
hauteur_bouton = (hauteur_plateau-2*contour-(ecart_boutons*(nb_boutons-1)))/nb_boutons

JEUX = True

while JEUX: 

    fenetre = cree_fenetre(largeur_plateau,hauteur_plateau)

    jeu = menu()
    
    if jeu != None and jeu != False :
        
        ferme_fenetre()
    
        subprocess.run(["python", jeu])
    
        print("OK")
    
    if jeu == False :
        
        ferme_fenetre()
        
        JEUX = False