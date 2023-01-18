from bibliotheque import *
import copy
import time
from random import randint



## Tâche 1 :



def conversion(str):
    """ 
    Reçoit une chaine de caractère contenant uniquement des chiffres et des espaces et renvoie une liste des entiers que contient la chaine.
    >>> conversion("1 2 2 1 3")
    [1, 2, 2, 1, 3]
    """
    
    liste = str.split()
    
    resultat = []
    
    for caractere in liste :
        
        resultat.append(int(caractere))
       
    return resultat
    


def lire_grille(nom_fichier):
    """ 
    Prend en argument une chaîne de caractères nom_fichier et renvoie une liste de listes décrivant les valeurs des cellules de la grille.
    >>> lire_grille('grille_exple.txt')
    [[2, 2, 1, 5, 3], [2, 3, 1, 4, 5], [1, 1, 1, 3, 5], [1, 3, 5, 4, 2], [5, 4, 3, 2, 1]]
    """

    fichier = open(nom_fichier, "r")
    
    contenu = fichier.readlines()
    
    fichier.close()
    
    hauteur = len(contenu)

    valeurs_cellules = []
    
    for i in range(hauteur):
        
        ligne = conversion(contenu[i])
        
        valeurs_cellules.append(ligne)
       
    return valeurs_cellules
    
    
    
def afficher_grille(grille):
    """
    Prend en argument une liste de listes représentant une grille, et l’affichant joliment sur le terminal.
    >>> afficher_grille([[2,1,3,1], [2,2,2,1], [1,1,1,1], [1,1,1,1]])
    2     1     3     1
    
    
    2     2     2     1
    
    
    1     1     1     1
    
    
    1     1     1     1
    """
    
    for i in range(len(grille)):
        
        for j in range(len(grille[0])):
            
            grille[i][j]  = str(grille[i][j])
            
        print("     ".join(grille[i]))
            
        print("\n")



def ecrire_grille(grille, nom_fichier):
    """
    Prend en argument une grille sous forme de liste de listes de nombres et un nom de fichier, et sauvegardant la grille fournie dans le fichier indiqué, en respectant le même format
    'texte.txt' : fichier texte vide.
    >>> ecrire_grille([[2,2,1,5,3], [2,3,1,4,5], [1,1,1,3,5], [1,3,5,4,2], [5,4,3,2,1]], 'texte.txt')
    """
    
    fichier = open(nom_fichier, "w")
    
    for i in range(len(grille)):
    
        for j in range(len(grille[0])) :
            
            fichier.write(str(grille[i][j]))
            
            fichier.write("\t")
            
        fichier.write("\n")
  
    fichier.close()
    
    
    
## Tâche 2 :



def colonnes(grille):
    """
    Prend en argument une liste de liste. Renvoie une liste de liste des colonnes de la grille.
    >>> colonnes([[2,2,1,5,3], [2,3,1,4,5], [1,1,1,3,5], [1,3,5,4,2], [5,4,3,2,1]])
    [[2, 2, 1, 1, 5], [2, 3, 1, 3, 4], [1, 1, 1, 5, 3], [5, 4, 3, 4, 2], [3, 5, 5, 2, 1]]
    """
    
    ensemble_colonnes = []
    
    for i in range(len(grille[0])):
        
        colonne = []
        
        for j in range(len(grille)):
            
            colonne.append(grille[j][i])
            
        ensemble_colonnes.append(colonne)
        
    return ensemble_colonnes
    
    
    
def compter_nb_occurrence(liste):
    """
    Prend en argument une liste de liste. Renvoie True si pour toutes les listes de "liste", chaque élement de la liste ne possède qu'une seule occurrence (l'élément None n'est pas considéré, il peut y avoir plusieurs occurrences des cet élément), renvoie False sinon.
    >>> compter_nb_occurrence([[2,2,1,5,3], [2,3,1,4,5], [1,1,1,3,5], [1,3,5,4,2], [5,4,3,2,1]])
    False
    >>> compter_nb_occurrence([[None,2,None,5,3], [2,3,1,4,None], [None,1,None,3,5], [1,None,5,None,2], [5,4,3,2,1]])
    True
    """
    
    for index in range(len(liste)):

        for element in liste[index]:
            
            if element != None:
            
                nb_occurrence = liste[index].count(element)
                
                if nb_occurrence > 1 :
                    
                    return False
                    
    return True



def sans_conflit(grille, noircies):
    """
    Prend en arguments une liste de liste grille décrivant le contenu des cellules et un ensemble noircies décrivant l’ensemble des cellules noircies. Renvoie True si la règle du jeu numéro 1 est respectée, autrement dit si aucune des cellules visibles de la grille ne contient le même nombre qu’une autre cellule visible située sur la même ligne ou la même colonne, et False sinon.
    >>> sans_conflit([[2,2,1,5,3], [2,3,1,4,5], [1,1,1,3,5], [1,3,5,4,2], [5,4,3,2,1]], {(2, 0), (0, 0), (3, 3), (2, 2), (3, 1), (0, 2), (1, 4)}) 
    True
    >>> sans_conflit([[2,2,1,5,3], [2,3,1,4,5], [1,1,1,3,5], [1,3,5,4,2], [5,4,3,2,1]], {(2, 0), (3, 3), (2, 2), (3, 1), (0, 2), (1, 4)})
    False
    """
    
    dico = {}
    
    for couple in noircies :
        
        dico[couple] = grille[couple[0]][couple[1]]
        
        grille[couple[0]][couple[1]] = None
        
    # Même ligne    
    
    lignes_valide = compter_nb_occurrence(grille)
        
    # Même colonne
    
    colonnes_valide = compter_nb_occurrence(colonnes(grille))
    
    # Ré-établir la grille
    
    for couple in noircies :
        
        grille[couple[0]][couple[1]] = dico[couple] 
        
    # Résultat
      
    if lignes_valide == True and colonnes_valide == True :
        
        return True
        
    else:

        return False



def sans_voisines_noircies(grille, noircies):
    """
    Prend en arguments une liste de liste grille décrivant le contenu des cellules et un ensemble noircies décrivant l’ensemble des cellules noircies. Renvoie True si la règle du jeu numéro 2 est respectée, autrement dit si aucune cellule noircies n’est voisine (par un de ses quatre bords) d’une autre cellule noircies, et False sinon.
    >>> sans_voisines_noircies([[2,2,1,5,3], [2,3,1,4,5], [1,1,1,3,5], [1,3,5,4, 2], [5, 4, 3, 2, 1]], {(2, 0), (0, 0), (3, 3), (2, 2), (3, 1), (0, 2), (1, 4)}) 
    True
    >>> sans_voisines_noircies([[2,2,1,5,3], [2,3,1,4,5], [1,1,1,3,5], [1,3,5,4,2], [5,4,3,2,1]], {(2, 0), (0, 0), (3, 3), (2, 2), (3, 1), (0, 2), (1, 4), (1, 3)}) 
    False
    """
        
    for couple in noircies :
        
        if (couple[0]-1, couple[1]) in noircies or (couple[0]+1, couple[1]) in noircies or (couple[0], couple[1]-1) in noircies or (couple[0], couple[1]+1) in noircies :
            
            return False 
    
    return True
    
    
       
def dans_grille(grille, i, j):
    """
    Renvoie True si le pixel (i, j)
    est un pixel de la grille, False sinon.
    >>> dans_grille([[1,1], [2,2]], 0, 0)
    True
    >>> dans_grille([[1,1], [1,1]], 4, 3)
    False
    """
    
    return (0 <= i < len(grille) and 0 <= j < len(grille[i]))
    
    
    
def voisins(i, j):
    """
    Renvoie la liste des voisins du pixel (i, j)
    (sans prendre en compte les bords).
    >>> voisins(0, 0)
    [(1, 0), (0, 1), (-1, 0), (0, -1)]
    """
    
    return [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]
    
    
    
def remplacement(grille, i, j, nouvelle_valeur):
    """
    Remplace la zone du pixel (i, j)
    par la nouvelle_valeur. On suppose
    que (i, j) est bien un pixel de
    la grille.
    >>> remplacement([[1,1,1], [3,3,1]], 0, 0, None)
    [[None, None, None], [3, 3, None]]
    >>> remplacement([[1,3,1], [1,1,3]], 0, 0, None)
    [[None, 3, 1], [None, None, 3]]
    """
    
    valeur_prec = grille[i][j]
    
    if valeur_prec == nouvelle_valeur:
        
        return
        
    grille[i][j] = nouvelle_valeur
    
    for vi, vj in voisins(i, j):
        
        if (dans_grille(grille, vi, vj) and grille[vi][vj] == valeur_prec):
            
            remplacement(grille, vi, vj, nouvelle_valeur)
            
    return grille



def connexe(grille, noircies):
    """
    Prend en arguments une liste de liste grille décrivant le contenu des cellules et un ensemble noircies décrivant l’ensemble des cellules noircies. Renvoie True si la règle du jeu numéro 3 est respectée, autrement dit si les cellules visibles de la grille forment une seule zone (ou région, ou composante connexe), et False sinon.
    >>> connexe([[2,2,1,5,3], [2,3,1,4,5], [1,1,1,3,5], [1,3,5,4,2], [5,4,3,2,1]], {(2, 0), (0, 0), (3, 3), (2, 2), (3, 1), (0, 2), (1, 4)})
    True
    >>> connexe([[2,2,1,5,3], [2,3,1,4,5], [1,1,1,3,5], [1,3,5,4,2], [5,4,3,2,1]], {(2, 0), (0, 0), (3, 3), (2, 2), (3, 1), (0, 2), (1, 4), (3, 4)})
    False
    """
    
    # Stocker tous les éléments de la grille dans un dictionnaire
    
    dico = {}
    
    for i in range(len(grille)) :
        
        for j in range(len(grille[0])) :
            
            dico[(i, j)] = grille[i][j] 
            
    # Liste composée de 1 (pour les cellules visibles) et de None (pour les celulles noircies)
            
    for couple in noircies :
                
        grille[couple[0]][couple[1]] = None
            
    for i in range(len(grille)):
        
        for j in range(len(grille[0])):
            
            if grille[i][j] != None :
                
                grille[i][j] = 1
    
    # Commencer l'analyse sur une case visible
    
    (i, j) = (0, 0)
    
    while (i, j) in noircies :
        
        if i == len(grille[0]) and j == len(grille) :
            
            i = 0
            j = 0
        
        if j == len(grille) :
            
            i += 1
            j = 0
        
        else :
            
            j += 1
            
    # Analyse
            
    remplacement(grille, i, j, 2)
        
    valeurs_grille = set()
    
    for liste in grille :
        
        for element in liste :
            
            valeurs_grille.add(element)
            
    # Ré-établir la grille
                
    for couple in dico :
        
        grille[couple[0]][couple[1]] = dico[couple]
        
    # Résultat
        
    if len(valeurs_grille) > 2 :
        
        return False
        
    else :
        
        return True
        
    
    
## Tâche 3 :



def afficher_grille_fenetre(grille):
    """
    Prend en argument une liste de listes représentant une grille, et l’affichant joliment dans une fenêtre et si un élément de la grille est égal à None la case est coloriée en noir.
    """
    
    efface_tout()
    
    
    # Fond de la fenêtre
    
    rectangle(0, 0, largeur_plateau, hauteur_plateau, couleur = "#eaeaea", remplissage = "#eaeaea")
    
    # Contour de la grille
    
    rectangle(contour, contour, largeur_plateau-2*contour-largeur_bouton, hauteur_plateau-contour, couleur = "#858585", remplissage = "white", epaisseur = 3)
    
    # Quadrillage de la grille
    
    nb_lignes = len(grille)
    nb_colonnes = len(grille[0])
    
    ax = contour
    ay = contour
    bx = contour
    by = contour
    
    largeur_case = (largeur_plateau-3*contour-largeur_bouton)/nb_colonnes 
    
    hauteur_case = (hauteur_plateau-2*contour)/nb_lignes

    for element in range(nb_colonnes-1):

        ax += largeur_case
        bx = ax
        by = hauteur_plateau-contour
        
        ligne(ax, ay, bx, by, couleur = '#858585', epaisseur = 3)
        
    for element in range(nb_lignes-1):
        
        ax = contour
        ay += hauteur_case
        bx = largeur_plateau-2*contour-largeur_bouton
        by = ay
        
        ligne(ax, ay, bx, by, couleur = '#858585', epaisseur = 3)
        
    # Valeurs des cases dans la grille
        
    j = 0
    
    for index in range(len(grille)):
        
        i = 0
        
        for chiffre in grille[index]:
            
            texte(i+(largeur_case/2)+contour, j+(hauteur_case/2)+contour, str(chiffre) , couleur = 'black', ancrage = 'center', police = 'Times new roman', taille = 28)
            
            i += largeur_case 
        
        j += hauteur_case



def noircir_case(grille, noircies, liste_evenement):
    """
    Prend en arguments une liste de liste grille décrivant le contenu des cellules, un ensemble noircies décrivant l’ensemble des cellules noircies et un liste contenant les évènements qui se sont produits pendant la partie.
    Ajoute les coordonnées de la case où il y a eu un clic à l'ensemble noircies. Si ces coordonnées se trouvent déjà dans l'ensemble, les coordonées sont enlevées de l'ensemble noircies.
    """
    
    largeur_case = (largeur_plateau-3*contour-largeur_bouton)/len(grille[0])
    hauteur_case = (hauteur_plateau-2*contour)/len(grille)
    
    x = abscisse_souris()
    y = ordonnee_souris()
    
    # Transcrire les coordonées du clic en indice d'une case dans la grille
    
    i = 0
    j = 0
    
    while x > contour :
        
        x -= largeur_case
        
        j += 1
        
    while y > contour :
        
        y -= hauteur_case
        
        i += 1
        

    coordonnee = (i-1, j-1)
    
    liste_evenement.append(coordonnee)
    
    # Ajout ou suppression de la case où il y a eu le clic dans noircies
    
    if coordonnee in noircies :
        
        noircies.discard(coordonnee)
        
    else :
        
        noircies.add(coordonnee)
    

    
def afficher_case_noircie(grille, noircies):
    """
    Prend en arguments une liste de liste grille décrivant le contenu des cellules et un ensemble noircies décrivant l’ensemble des cellules noircies.
    Efface la fenêtre. Affiche la grille et recouvre d'un rectangle noir toutes les cases dont les coordonnées se trouve dans l'ensemble noircies.
    """
    
    efface_tout()
    
    afficher_grille_fenetre(grille)
    
    largeur_case = (largeur_plateau-3*contour-largeur_bouton)/len(grille[0])
    hauteur_case = (hauteur_plateau-2*contour)/len(grille)
    
    for couple in noircies :
        
        ax = largeur_case*couple[1]+contour
        
        ay = hauteur_case*couple[0]+contour
        
        rectangle(ax, ay, ax+largeur_case, ay+hauteur_case, couleur = '#858585', remplissage = 'black', epaisseur = 3)
            
        texte(ax+(largeur_case/2), ay+(hauteur_case/2), str(grille[couple[0]][couple[1]]), couleur = "white", ancrage = "center", police = "Times New Roman", taille = 15)
        


def annuler():
    """
    Lorsque l'on appuie sur le bouton annuler, le dernier coup qui est annulé (si on avait noirci une case elle est dé-noircie et réciproquement si on avait dé-noirci une case elle est re-noircie).
    liste_evenement est un liste (de couple) qui contient tous les coups qui se produisent au fur et à mesure de la partie.
    """
    
    if  liste_evenement != []:
        
        if liste_evenement[-1] in noircies :
            
            noircies.discard(liste_evenement[-1])
            
            liste_evenement.pop(-1) 
            
        else :
            
            noircies.add(liste_evenement[-1])
            
            liste_evenement.pop(-1)
        
    
    
def recommencer():
    """
    Lorsque l'on appuie sur le bouton recommencer, la grille est remise à son état d'origine. L'ensemble noircies et la liste liste_evenement sont remis à zéro (vide).
    """
    
    efface_tout()
    
    noircies.clear()
    
    liste_evenement.clear()
    
    for element in noircies_depart :
        
        noircies.add(element)
        
    afficher_case_noircie(grille, noircies)
    
    

def gagne(grille, noircies):
    """
    Prend en arguments une liste de liste grille décrivant le contenu des cellules et un ensemble noircies décrivant l’ensemble des cellules noircies.
    Renvoie True si toutes les règles du jeu sont respectées, sinon renvoie False.
    >>> gagne([[2, 2, 1, 5, 3], [2, 3, 1, 4, 5], [1, 1, 1, 3, 5], [1, 3, 5, 4, 2], [5, 4, 3, 2, 1]],{(2, 0), (0, 0), (3, 3), (2, 2), (3, 1), (0, 2), (1, 4)})
    True
    >>> gagne([[2, 2, 1, 5, 3], [2, 3, 1, 4, 5], [1, 1, 1, 3, 5], [1, 3, 5, 4, 2], [5, 4, 3, 2, 1]],{(2, 0), (0, 0), (3, 3), (2, 2), (3, 1), (0, 2)})
    False
    """
    
    if sans_conflit(grille,noircies) and sans_voisines_noircies(grille,noircies) and connexe(grille, noircies):
        
        return True

    return False
    
    

def menu():
    """
    Affiche un menu proposant les choix des différentes grilles.
    """
    
    chiffre = randint(1,8)
    
    noircies = set()
    
    print("chiffre n°", chiffre)
    
    valeur = largeur_plateau/4
    
    # Fond du menu
    
    rectangle(0, 0, largeur_plateau-1, hauteur_plateau-1, couleur = 'black', remplissage = 'white', epaisseur = 3)
    texte(largeur_plateau/2, 2*contour, "HITORI", couleur = 'black', ancrage = 'center', police = 'Times new roman', taille = 30)
    texte(largeur_plateau/2, 3*contour, "( ひとり )",couleur = 'black', ancrage = 'center', police = 'Times new roman', taille = 15)
    ligne(valeur, 4*contour-ecart_boutons, 3*valeur, 4*contour-ecart_boutons, couleur = 'black', epaisseur = 1)
    
    hauteur_bouton_menu = (hauteur_plateau-8*contour-2*ecart_boutons)/3
    largeur_bouton_menu = (largeur_plateau-8*contour)/2
    
    # Boutons de gauche
    
    rectangle(2*contour, 5*contour, largeur_bouton_menu+2*contour, 5*contour+hauteur_bouton_menu, couleur = 'black', remplissage = '#84d3ea', epaisseur = 2)
    rectangle(2*contour, 6*contour+hauteur_bouton_menu, largeur_bouton_menu+2*contour,6*contour+2*hauteur_bouton_menu, couleur = 'black', remplissage = '#43acca', epaisseur = 2)
    rectangle(2*contour, 7*contour+2*hauteur_bouton_menu, largeur_bouton_menu+2*contour,7*contour+3*hauteur_bouton_menu, couleur = 'black', remplissage = '#178daf', epaisseur = 2)
    
    texte(2*contour+(largeur_bouton_menu/2), 5*contour+(hauteur_bouton_menu/3)+10, "GRILLE TRÈS SIMPLE", couleur = "white", ancrage = 'center', police = 'Times new roman', taille = 25)
    texte(2*contour+(largeur_bouton_menu/2), 5*contour+2*(hauteur_bouton_menu/3), "(4x4, 5x5)", couleur = "white", ancrage = 'center', police = 'Times new roman', taille = 15)
    texte(2*contour+(largeur_bouton_menu/2), 6*contour+(hauteur_bouton_menu/3)+hauteur_bouton_menu+10, "GRILLE SIMPLE", couleur = "white", ancrage = 'center', police = 'Times new roman', taille = 25)
    texte(2*contour+(largeur_bouton_menu/2), 6*contour+2*(hauteur_bouton_menu/3)+hauteur_bouton_menu, "(6x6)", couleur = "white", ancrage = 'center', police = 'Times new roman', taille = 15)
    texte(2*contour+(largeur_bouton_menu/2), 7*contour+(hauteur_bouton_menu/3)+2*hauteur_bouton_menu+10, "GRILLE MOYENNE", couleur = "white", ancrage = 'center', police = 'Times new roman', taille = 25)
    texte(2*contour+(largeur_bouton_menu/2), 7*contour+2*(hauteur_bouton_menu/3)+2*hauteur_bouton_menu, "(7x7)", couleur = "white", ancrage = 'center', police = 'Times new roman', taille = 15)
    
    # Boutons de droite
    
    rectangle(6*contour+largeur_bouton_menu, 5*contour, largeur_plateau-2*contour, 5*contour+hauteur_bouton_menu, couleur = 'black', remplissage = '#097897', epaisseur = 2)
    rectangle(6*contour+largeur_bouton_menu, 6*contour+hauteur_bouton_menu, largeur_plateau-2*contour,6*contour+2*hauteur_bouton_menu, couleur = 'black', remplissage = '#025b74', epaisseur = 2)
    rectangle(6*contour+largeur_bouton_menu, 7*contour+2*hauteur_bouton_menu, largeur_plateau-2*contour,7*contour+3*hauteur_bouton_menu, couleur = 'black', remplissage = '#a6a6a6', epaisseur = 2)
    
    texte(largeur_plateau-2*contour-(largeur_bouton_menu/2), 5*contour+(hauteur_bouton_menu/3)+10, "GRILLE DIFFICILE", couleur = "white", ancrage = 'center', police = 'Times new roman', taille = 25)
    texte(largeur_plateau-2*contour-(largeur_bouton_menu/2), 5*contour+2*(hauteur_bouton_menu/3), "(8x8, 9x9)", couleur = "white", ancrage = 'center', police = 'Times new roman', taille = 15)
    texte(largeur_plateau-2*contour-(largeur_bouton_menu/2), 6*contour+(hauteur_bouton_menu/3)+hauteur_bouton_menu+10, "GRILLE TRÈS DIFFICILE", couleur = "white", ancrage = 'center', police = 'Times new roman', taille = 25)
    texte(largeur_plateau-2*contour-(largeur_bouton_menu/2), 6*contour+2*(hauteur_bouton_menu/3)+hauteur_bouton_menu, "(10x10, 11x10, 11x11, 12x12, 17x17)", couleur = "white", ancrage = 'center', police = 'Times new roman', taille = 15)
    texte(largeur_plateau-2*contour-(largeur_bouton_menu/2), 7*contour+(hauteur_bouton_menu/2)+2*hauteur_bouton_menu, "FICHIER SAUVEGARDÉ", couleur = "white", ancrage = 'center', police = 'Times new roman', taille = 25)
    
    # Définition de la grille en fonction du clic
    
    x,y = attend_clic_gauche()
    
    grille = None
    
    if x >= 2*contour and x <= largeur_bouton_menu+2*contour :
        
        if y >= 5*contour and y <= 5*contour+hauteur_bouton_menu :
            
            grille = lire_grille("grille_tres_simple" + str(chiffre) + "_hitori.txt")
            
        elif y >= 6*contour+hauteur_bouton_menu and y <= 6*contour+2*hauteur_bouton_menu :
            
            grille = lire_grille("grille_simple" + str(chiffre) + "_hitori.txt")
                
        elif y >= 7*contour+2*hauteur_bouton_menu and y <= 7*contour+3*hauteur_bouton_menu :
            
            grille = lire_grille("grille_moyenne" + str(chiffre) + "_hitori.txt")

    if x >= 6*contour+largeur_bouton_menu and x <= largeur_plateau-2*contour :
            
        if y >= 5*contour and y <= 5*contour+hauteur_bouton_menu :
            
            grille = lire_grille("grille_difficile" + str(chiffre) + "_hitori.txt")

        elif y >= 6*contour+hauteur_bouton_menu and y <= 6*contour+2*hauteur_bouton_menu :
            
            grille = lire_grille("grille_tres_difficile" + str(chiffre) + "_hitori.txt")

        elif y >= 7*contour+2*hauteur_bouton_menu and y <= 7*contour+3*hauteur_bouton_menu :    
            
            appel = lire_grille_noircies("fichier_sauvegarde_hitori.txt")
            
            if appel[0] == [] :
                
                texte(largeur_plateau/2, hauteur_plateau/2, "IMPOSSIBLE, aucun fichier sauvegardé.", couleur = "red", ancrage = 'center', police = 'Times new roman', taille = 28)
                
                attente(1)
                
                grille = menu()[0]
                
            else :
                
                grille = appel[0]
                
                noircies = appel[1]
                     
    return grille, noircies



def boutons():
    """
    Affiche les boutons dans la fenêtre.
    """

    rectangle(largeur_plateau-largeur_bouton-contour, contour, largeur_plateau-contour, hauteur_bouton+contour, couleur = "#000000", remplissage = "#B244F1", epaisseur = 2)
    texte(largeur_plateau-contour-(largeur_bouton/2), hauteur_bouton/2+contour, "QUITTER", couleur = 'black', ancrage = 'center', police = 'Times new roman', taille = 15)
    
    rectangle(largeur_plateau-largeur_bouton-contour,hauteur_bouton+contour+ecart_boutons,largeur_plateau-contour,hauteur_bouton*2+contour+ecart_boutons, couleur = "#000000", remplissage = "#F144E4", epaisseur = 2)
    texte(largeur_plateau-contour-(largeur_bouton/2), hauteur_bouton+ecart_boutons+(hauteur_bouton/2)+contour, "RÉSOUDRE", couleur = 'black', ancrage = 'center', police = 'Times new roman', taille = 15)
    
    rectangle(largeur_plateau-largeur_bouton-contour,hauteur_bouton*2+contour+2*ecart_boutons,largeur_plateau-contour,hauteur_bouton*3+contour+2*ecart_boutons, couleur = "#000000", remplissage = "#F1447E", epaisseur = 2)
    texte(largeur_plateau-contour-(largeur_bouton/2), 2*hauteur_bouton+2*ecart_boutons+(hauteur_bouton/2)+contour, "AFFICHER SOLVEUR", couleur = 'black', ancrage = 'center', police = 'Times new roman', taille = 15)
    
    rectangle(largeur_plateau-largeur_bouton-contour,hauteur_bouton*3+contour+3*ecart_boutons,largeur_plateau-contour,hauteur_bouton*4+contour+3*ecart_boutons, couleur = "#000000", remplissage = "#F14E44", epaisseur = 2)
    texte(largeur_plateau-contour-(largeur_bouton/2), 3*hauteur_bouton+3*ecart_boutons+(hauteur_bouton/2)+contour, "RECOMMENCER", couleur = 'black', ancrage = 'center', police = 'Times new roman', taille = 15)
    
    rectangle(largeur_plateau-largeur_bouton-contour,hauteur_bouton*4+contour+4*ecart_boutons,largeur_plateau-contour,hauteur_bouton*5+contour+4*ecart_boutons, couleur = "#000000", remplissage = "#F17E44", epaisseur = 2)
    texte(largeur_plateau-contour-(largeur_bouton/2), 4*hauteur_bouton+4*ecart_boutons+(hauteur_bouton/2)+contour, "ANNULER", couleur = 'black', ancrage = 'center', police = 'Times new roman', taille = 15)
    
    rectangle(largeur_plateau-largeur_bouton-contour,hauteur_bouton*5+contour+5*ecart_boutons,largeur_plateau-contour,hauteur_bouton*6+contour+5*ecart_boutons, couleur = "#000000", remplissage = "#F1A444", epaisseur = 2)
    texte(largeur_plateau-contour-(largeur_bouton/2), 5*hauteur_bouton+5*ecart_boutons+(hauteur_bouton/2)+contour, "CONFLITS", couleur = 'black', ancrage = 'center', police = 'Times new roman', taille = 15)
    
    rectangle(largeur_plateau-largeur_bouton-contour,hauteur_bouton*6+contour+6*ecart_boutons,largeur_plateau-contour,hauteur_bouton*7+contour+6*ecart_boutons, couleur = "#000000", remplissage = "#F1DE44", epaisseur = 2)
    texte(largeur_plateau-contour-(largeur_bouton/2), 6*hauteur_bouton+6*ecart_boutons+(hauteur_bouton/2)+contour, "INDICE", couleur = 'black', ancrage = 'center', police = 'Times new roman', taille = 15)
    
    rectangle(largeur_plateau-largeur_bouton-contour,hauteur_bouton*7+contour+7*ecart_boutons,largeur_plateau-contour,hauteur_bouton*8+contour+7*ecart_boutons, couleur = "#000000", remplissage = "#B6F144", epaisseur = 2)
    texte(largeur_plateau-contour-(largeur_bouton/2), 7*hauteur_bouton+7*ecart_boutons+(hauteur_bouton/2)+contour, "NOUVELLE PARTIE", couleur = 'black', ancrage = 'center', police = 'Times new roman', taille = 15)
    
    rectangle(largeur_plateau-largeur_bouton-contour,hauteur_bouton*8+contour+8*ecart_boutons,largeur_plateau-contour,hauteur_bouton*9+contour+8*ecart_boutons, couleur = "#000000", remplissage = "#26C027", epaisseur = 2)
    texte(largeur_plateau-contour-(largeur_bouton/2), 8*hauteur_bouton+8*ecart_boutons+(hauteur_bouton/2)+contour, "SAUVEGARDER",  couleur = 'black', ancrage = 'center', police = 'Times new roman', taille = 15)
    
    rectangle(largeur_plateau-largeur_bouton-contour,hauteur_bouton*9+contour+9*ecart_boutons,largeur_plateau-contour,hauteur_bouton*10+contour+9*ecart_boutons, couleur = "black", remplissage = "#26C0A4", epaisseur = 2)
    texte(largeur_plateau-contour-(largeur_bouton/2), 9*hauteur_bouton+9*ecart_boutons+contour+(hauteur_bouton/2), "NOMBRE DE COUPS : " + str(evenements),  couleur = 'black', ancrage = 'center', police = 'Times new roman', taille = 11)
        
    
    
## Tâche 4 :



def resoudre(grille,noircies, i, j):
    """
    Fonction qui prend en argument une liste de liste, grille ; un ensemble, noircies et des coordonnées de la grille, i, j.
    Si la grille possède une solution, elle renvoie l'ensemble noircies, sinon elle renvoie None.
    Elle modifie noircies sur place.
    >>> print(resoudre([[2, 2, 1, 5, 3], [2, 3, 1, 4, 5], [1, 1, 1, 3, 5], [1, 3, 5, 4, 2], [5, 4, 3, 2, 1]], set(), 0, 0))
    {(0, 0), (3, 3), (3, 1), (1, 4), (2, 0), (2, 2), (0, 2)}
    >>> print(resoudre([[2, 2, 1, 5, 3], [2, 3, 1, 4, 5], [1, 1, 1, 3, 5], [1, 3, 5, 4, 2], [5, 4, 3, 2, 2]], set(), 0, 0))
    None
    """
    
    if i == len(grille)-1 and j == len(grille[0]):
        
        if gagne(grille,noircies) :
            
            return noircies
            
        else :
            
            return None
    
    if j == len(grille[0]) :
        
        i += 1
        
        j = 0
        
    cellule = (i, j)
    
    element_cellule = grille[i][j]
    
    if connexe(grille, noircies) == False or sans_voisines_noircies(grille, noircies) == False :
        
        return None
        
    if gagne(grille, noircies) :
        
        return noircies
        
    else :
        
        ligne = grille[i].count(element_cellule)
        
        colonne_cellule = []
        
        for liste in grille :
            
            colonne_cellule.append(liste[j])
            
        colonne = colonne_cellule.count(element_cellule)
                
        if ligne < 2 and colonne < 2 :
            
            noircies.discard(cellule)
            
            return resoudre(grille, noircies, i, j+1)
            
        else :
            
            noircies.add(cellule)
            
            resoudre(grille, noircies, i, j+1)
            
            if gagne(grille, noircies) :
                
                return noircies
                
            else :
                
                noircies.discard(cellule)
                
                resoudre(grille, noircies, i, j+1)
                
                if gagne(grille, noircies) :
                    
                    return noircies
                    
                else : 
                
                    return None
        
    
    
## Améliorations :



def resoudre_affichage(grille,noircies, i, j):
    """
    Fonction qui prend en argument une liste de liste, grille ; un ensemble, noircies et des coordonnées de la grille, i, j.
    Si la grille possède une solution, elle renvoie l'ensemble noircies, sinon elle renvoie None.
    Affiche les cases noircies au fur et à mesure de la recherche.
    """
    
    afficher_case_noircie(grille, noircies)
    
    boutons()
    
    mise_a_jour()
    
    if i == len(grille)-1 and j == len(grille[0]):
        
        if gagne(grille, noircies) :
            
            return noircies
            
        else :
            
            return None
    
    if j == len(grille[0]) :
        
        i += 1
        
        j = 0
        
    cellule = (i, j)
    
    element_cellule = grille[i][j]
    
    if connexe(grille, noircies) == False or sans_voisines_noircies(grille, noircies) == False :
        
        return None
        
    if gagne(grille, noircies):
        
        return noircies
        
    else :
        
        ligne = grille[i].count(element_cellule)
        
        colonne_cellule = []
        
        for liste in grille :
            
            colonne_cellule.append(liste[j])
            
        colonne = colonne_cellule.count(element_cellule)
                
        if ligne < 2 and colonne < 2 :
            
            noircies.discard(cellule)
            
            return resoudre_affichage(grille, noircies, i, j+1)
            
        else :
            
            noircies.add(cellule)
            
            resoudre_affichage(grille, noircies, i, j+1)
            
            if gagne(grille, noircies) :
                
                return noircies
                
            else :
                
                noircies.discard(cellule)
                
                resoudre_affichage(grille, noircies, i, j+1)
                
                if gagne(grille, noircies) :
                    
                    return noircies
                    
                else : 
                
                    return None
                    


def doublons(liste, index_liste, ensemble_doublons, etat):
    """
    Prend en argument une liste ; un nombre index_liste correspondant à l'index de la liste dans la grille ; une liste d'ensemble ensemble_doublons et une chaîne de caractère etat pour savoir si la liste est une ligne ou une colonne.
    La fonction ajoute les ensembles de cellules en conflit de chaque ligne et de chaque colonne à la liste “ensemble_doublons”.
    Modifie la liste ensemble_doublons sur place.
    >>> doublons([2, 2, 1, 5, 3], 0, [], ligne)
    [{(1, 0), (0, 0)}]
    >>> doublons([1, 1, 1, 3, 5], 2, [{(0, 1), (0, 0)}], ligne)
    [{(0, 1), (0, 0)}, {(1, 2), (0, 2), (2, 2)}]
    """
    
    for element in liste :
        
        doublons = set()
        
        compte = []
        
        for i,e in enumerate(liste):
            
            if e == element :
                
                compte.append(i)
        
        if len(compte) >= 2:
            
            for i in compte :
                
                if etat == "ligne" :
                
                    doublons.add((index_liste, i))
                    
                else :
            
                    doublons.add((i, index_liste))
                    
            if doublons not in ensemble_doublons :
                
                ensemble_doublons.append(doublons)
                
                
            
def cellules_en_conflit(grille):
    """
    Prend en arguments une liste de liste grille décrivant le contenu des cellules.
    Renvoie une liste d'ensemble (tous les ensembles de cellules en conflit entre elles) de toutes les cellules en conflits (cellules se situant sur la même ligne ou colonne et possédant le même chiffre).
    >>> cellules_en_conflit([[2,2,1,5,3], [2,3,1,4,5], [1,1,1,3,5], [1,3,5,4,2], [5,4,3,2,1]])
    {(0, 1), (1, 2), (0, 0), (1, 3), (3, 3), (3, 0), (0, 2), (3, 1), (2, 1), (1, 4), (2, 0), (2, 4), (2, 2), (1, 0), (1, 1)}
    """
    
    ensemble_doublons = []
    
    etat = "ligne"
    
    index_liste = 0
    
    for liste in grille :
        
        doublons(liste, index_liste, ensemble_doublons, etat)
        
        index_liste += 1
   
    etat = "colonne"
    
    ensemble_colonnes = colonnes(grille)
    
    index_liste = 0
    
    for liste in ensemble_colonnes :
        
        doublons(liste, index_liste, ensemble_doublons, etat)
        
        index_liste += 1
        
    return ensemble_doublons
    
    
    
def cellules_isolees(grille, noircies):
    """
    Prend en arguments une liste de liste grille décrivant le contenu des cellules et un ensemble, noircies.
    Renvoie les cellules isolées (ne respectant pas la règle n°3). (Similaire à "connexe" mais renvoie les éléments qui sont en conflits au lieu de True et False).
    >>> cellules_isolees([[2,2,1,5,3], [2,3,1,4,5], [1,1,1,3,5], [1,3,5,4,2], [5,4,3,2,1]], {(2, 0), (0, 0), (3, 3), (2, 2), (3, 1), (0, 2), (1, 4)})
    []
    >>> cellules_isolees([[2,2,1,5,3], [2,3,1,4,5], [1,1,1,3,5], [1,3,5,4,2], [5,4,3,2,1]], {(2, 0), (0, 0), (3, 3), (2, 2), (3, 1), (0, 2), (1, 4), (3, 4)})
    [(3, 0), (3, 2), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]
    """
    
    grille_modifiable = copy.deepcopy(grille)
    
    for couple in noircies :
                
        grille_modifiable[couple[0]][couple[1]] = None
            
            
    for elem in range(len(grille_modifiable)):
        
        for element in range(len(grille_modifiable[0])):
            
            if grille_modifiable[elem][element] != None :
                
                grille_modifiable[elem][element] = 1
    
    # Commencer l'analyse sur une case visible
    
    (i, j) = (0, 0)
    
    while (i, j) in noircies :
        
        if i == len(grille_modifiable[0]) and j == len(grille_modifiable) :
            
            i = 0
            j = 0
        
        if j == len(grille_modifiable) :
            
            i += 1
            j = 0
        
        else :
            
            j += 1
            
    # Analyse
            
    remplacement(grille_modifiable, i, j, 2)
    
    # Résultat
    
    elements_isoles = []
                
    index_liste = 0
                
    for liste in grille_modifiable :
        
        index_element = 0
        
        for element in liste :
            
            if element == 1 :
                
                elements_isoles.append((index_liste, index_element))
                
            index_element += 1
                
        index_liste += 1
        
    return elements_isoles
    
    
                    
def verification(grille, noircies) :
    """
    Prend en arguments une liste de liste grille décrivant le contenu des cellules et un ensemble, noircies.
    Affiche les cellules qui sont en conflits. 
    Les cellules ne respectant pas la règle n°1 sont affichées en surbrillance en vert, les cellules ne respectant pas la règle n°2 sont affichées en surbrillance en rouge et les cellules ne respectant pas la règle n°3 sont affichées en surbrillance en jaune.
    """
    
    largeur_colonne = (largeur_plateau-3*contour-largeur_bouton)/len(grille[0])
    hauteur_colonne = (hauteur_plateau-2*contour)/len(grille)
    
    conflit = cellules_en_conflit(grille)
    
    liste_conflit = []
    
    # Règle n°1 enfreinte 
    
    for ensemble in conflit :
        
        # Pour que le conflit soit quand même affiché même s'il regroupe plus de 2 cellules dont des cellules noircies
        
        compteur = 0
        
        for couple in ensemble :
            
            if couple in noircies :
                
                compteur += 1
                       
        if len(ensemble)-compteur > 1 :
            
            liste_conflit.append(ensemble)
           
    for ensemble in liste_conflit :
        
        for element in ensemble :
            
            ax = largeur_colonne*element[1]+contour
            
            ay = hauteur_colonne*element[0]+contour
        
            if element  not in noircies :
                
                rectangle(ax, ay, ax+largeur_colonne,ay+hauteur_colonne, couleur = '#7D7D7D', remplissage = '#4F97CE', epaisseur = 3)
                    
                texte(ax+(largeur_colonne/2), ay+(hauteur_colonne/2), str(grille[element[0]][element[1]]), couleur = "black", ancrage = "center", police = "Times New Roman", taille = 28)

    # Règle n°3 enfreinte
            
    if connexe(grille, noircies) == False :
        
        for element in cellules_isolees(grille, noircies) :
            
            ax = largeur_colonne*element[1]+contour
            
            ay = hauteur_colonne*element[0]+contour
            
            rectangle(ax, ay, ax+largeur_colonne,ay+hauteur_colonne, couleur = '#7D7D7D', remplissage = "#0011AA", epaisseur = 3)
            
            texte(ax+(largeur_colonne/2), ay+(hauteur_colonne/2), str(grille[element[0]][element[1]]), couleur = "black", ancrage = "center", police = "Times New Roman", taille = 28)
    
    # Règle n°2 enfreinte
            
    for element in noircies :
        
        if (element[0]-1, element[1]) in noircies or (element[0]+1, element[1]) in noircies or (element[0], element[1]-1) in noircies or (element[0], element[1]+1) in noircies :
            
            ax = largeur_colonne*element[1]+contour
            
            ay = hauteur_colonne*element[0]+contour
        
            rectangle(ax, ay, ax+largeur_colonne,ay+hauteur_colonne, couleur = '#1BD0DB', remplissage = "black", epaisseur = 5)
            
            texte(ax+(largeur_colonne/2), ay+(hauteur_colonne/2), str(grille[element[0]][element[1]]), couleur = "#1BD0DB", ancrage = "center", police = "Times New Roman", taille = 15)



def indice(grille, noircies) :
    """
    Prend en arguments une liste de liste grille décrivant le contenu des cellules et un ensemble, noircies.
    Affiche en surbrillance une case qui doit être noirci (obtenue grâce au solveur).
    """
    
    largeur_colonne = (largeur_plateau-3*contour-largeur_bouton)/len(grille[0])
    
    hauteur_colonne = (hauteur_plateau-2*contour)/len(grille)
    
    ensemble_noircies = resoudre(grille, set() , 0, 0)
    
    noircies_indice = copy.deepcopy(noircies)
    
    if resoudre(grille, noircies_indice , 0, 0) == None :
        
        texte((largeur_plateau-largeur_bouton)/2, hauteur_plateau/2, "PERDU !", couleur = "red", ancrage = "center", police = "Times New Roman", taille = 40)
        
        attend_ev()
        
    else :
        
        if gagne(grille, noircies) == False :
        
            for couple in ensemble_noircies :
                
                if couple not in noircies :
                    
                    ax = largeur_colonne*couple[1] + contour
                    
                    ay = hauteur_colonne*couple[0] + contour
                
                    rectangle(ax, ay, ax+largeur_colonne,ay+hauteur_colonne, couleur = 'blue', remplissage = "white", epaisseur = 5)
                    
                    texte(ax+(largeur_colonne/2), ay+(hauteur_colonne/2), str(grille[couple[0]][couple[1]]), couleur = "blue", ancrage = "center", police = "Times New Roman", taille = 28)
                    
                    attend_ev()
                    
                    break
                    
                    

def conversion_ensemble(str) :
    """
    Reçoit une chaine de caractère contenant uniquement des chiffres et renvoie un ensemble de couple.
    >>> conversion_ensemble('123456')
    {(1, 2), (3, 4), (5, 6)}
    """
    
    ensemble = set()
    
    i = 0
    
    while i < (len(str)) :
        
        ensemble.add((int(str[i]), int(str[i+1])))
        
        i += 2
        
    return ensemble
      
            

def lire_grille_noircies(nom_fichier):
    """ 
    Prend en argument une chaîne de caractères nom_fichier et renvoie une liste de listes décrivant les valeurs des cellules de la grille et un ensemble décrivant les cases noircies.
    >>> lire_grille_noircies("fichier_sauvegarde_test.txt")
    ([[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [6, 5, 4, 3, 2], [5, 5, 2, 1, 4], [4, 1, 5, 6, 2]], {(2, 4), (3, 3)})
    """

    fichier = open(nom_fichier, "r")
    
    contenu = fichier.readlines()
    
    fichier.close()
    
    noircies = set()
    
    hauteur = len(contenu)

    valeurs_cellules = []
    
    for i in range(hauteur-1):
        
        cellule = conversion(contenu[i])
        
        valeurs_cellules.append(cellule)
        
    if valeurs_cellules != [] and contenu[hauteur-1] != "None":
        
        noircies = conversion_ensemble(contenu[hauteur-1])
        
    return valeurs_cellules, noircies
    
    

def sauvegarder(grille, noircies) :
    """
    Prend en arguments une liste de liste grille décrivant le contenu des cellules et un ensemble, noircies.
    Sauvegarde une partie en cours, c'est-à-dire, la stock dans un fichier texte particulier prenant en compte les cases noircies (la dernière ligne du fichier, liste de chiffre la suite).
    """
    
    ecrire_grille(grille, "fichier_sauvegarde_hitori.txt")
    
    fichier = open("fichier_sauvegarde_hitori.txt", "a")
    
    for couple in noircies :
        
        for valeur in couple : 
        
            fichier.write(str(valeur))
    print(noircies)
    if noircies == set() :
        
        fichier.write("None")
    
    fichier.close()
    


def generateur_grille():
    
    longueur_plateau = int(input("longueur du plateau : "))
    
    hauteur_plateau = int(input("hauteur du plateau : "))
    
    grille = []
    
    for i in range(hauteur_plateau):
        
        ligne = []
        
        for j in range(longueur_plateau):
            
            ligne.append(randint(1,max(longueur_plateau, hauteur_plateau)))
            
        grille.append(ligne)
    
    compteur = 0
    
    while resoudre(grille, set(), 0, 0) == None :
        
        for i in range(hauteur_plateau):
            
            for j in range(longueur_plateau):
                
                grille [i][j] = randint(1,max(longueur_plateau, hauteur_plateau))
                
        compteur += 1 

    return grille
            
            
    
    
# INITIALISATION


contour = 30

largeur_plateau = 1090 
hauteur_plateau = 660

nb_boutons = 10

ecart_boutons = 15

largeur_bouton = 200
hauteur_bouton = (hauteur_plateau-2*contour-(ecart_boutons*(nb_boutons-1)))/nb_boutons

fenetre = cree_fenetre(largeur_plateau,hauteur_plateau)

valeurs_menu = menu()

while valeurs_menu[0] == None:
    
    valeurs_menu = menu()
    
grille, noircies = valeurs_menu[0], valeurs_menu[1]

temps_debut = time.time()

liste_evenement = []

grille_depart = copy.deepcopy(grille)
noircies_depart = copy.deepcopy(noircies)

evenements = 0


# BOUCLE PRINCIPALE


while True :    
    
    afficher_case_noircie(grille, noircies)

    boutons()
    
    if gagne(grille, noircies) == True :
        
        temps = time.time()
        
        texte((largeur_plateau-contour-largeur_bouton)/2, hauteur_plateau/2, "BRAVO ! Vous avez gagné !", couleur = '#FE0000', ancrage = 'center', police = 'Times new roman', taille = 48)
        
        texte((largeur_plateau-contour-largeur_bouton)/2, hauteur_plateau/2+2*contour, "Temps de jeu : " + str(round((temps-temps_debut),2)), couleur = '#F4598D', ancrage = 'center', police = 'Times new roman', taille = 30)
        
    attend_ev()
    
    if ordonnee_souris() >= contour and ordonnee_souris() <= hauteur_plateau-contour :
        
        if abscisse_souris() >= contour and abscisse_souris() <= largeur_plateau-2*contour-largeur_bouton:
            
            noircir_case(grille, noircies, liste_evenement)
            
            evenements += 1
            
        if abscisse_souris() >= largeur_plateau-contour-largeur_bouton and abscisse_souris() <= largeur_plateau-contour :
            
            if ordonnee_souris() >= contour and ordonnee_souris() <= hauteur_bouton+contour :
                
                break
                
            elif ordonnee_souris() >= hauteur_bouton+contour+ecart_boutons and ordonnee_souris() <= hauteur_bouton*2+contour+ecart_boutons :
                
                resoudre(grille, noircies, 0, 0)
                
            elif ordonnee_souris() >= hauteur_bouton*2+contour+2*ecart_boutons and ordonnee_souris() <= hauteur_bouton*3+contour+2*ecart_boutons :
                
                resoudre_affichage(grille, noircies, 0, 0)
                
            elif ordonnee_souris() >= hauteur_bouton*3+contour+3*ecart_boutons and ordonnee_souris() <= hauteur_bouton*4+contour+3*ecart_boutons :
                
                recommencer()
                
                temps_debut = time.time()
                
                evenements = 0
                
            elif ordonnee_souris() >= hauteur_bouton*4+contour+4*ecart_boutons and ordonnee_souris() <= hauteur_bouton*5+contour+4*ecart_boutons :
                
                annuler()
                
            elif ordonnee_souris() >= hauteur_bouton*5+contour+5*ecart_boutons and ordonnee_souris() <= hauteur_bouton*6+contour+5*ecart_boutons :
            
                verification(grille, noircies)
                
                attend_ev()
                
            elif ordonnee_souris() >= hauteur_bouton*6+contour+6*ecart_boutons and ordonnee_souris() <= hauteur_bouton*7+contour+6*ecart_boutons :
                
                indice(grille, noircies)
                
            elif ordonnee_souris() >= hauteur_bouton*7+contour+7*ecart_boutons and ordonnee_souris() <= hauteur_bouton*8+contour+7*ecart_boutons :
                
                evenements = 0
                
                valeurs_menu = menu()
                
                while valeurs_menu[0] == None:
                    
                    valeurs_menu = menu()
                
                grille, noircies = valeurs_menu[0], valeurs_menu[1]
                
                temps_debut = time.time()
                
                afficher_case_noircie(grille, noircies)
                
                liste_evenement = []
                
                grille_depart = copy.deepcopy(grille)
                
                noircies_depart = copy.deepcopy(noircies)
                
            elif ordonnee_souris() >= hauteur_bouton*8+contour+8*ecart_boutons and ordonnee_souris() <= hauteur_bouton*9+contour+8*ecart_boutons :
                
                sauvegarder(grille, noircies)
                
    boutons()         
    
    mise_a_jour()
    
# Fermeture et sortie
    
ferme_fenetre()