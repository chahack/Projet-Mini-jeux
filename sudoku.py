from bibliotheque import*
import copy
import time
from random import randint


def conversion(str):
    """ 
    Reçoit une chaine de caractère contenant uniquement des chiffres et des espaces.
    Renvoie une liste des entiers que contient la chaine.
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
    Prend en argument une chaîne de caractères nom_fichier.
    Renvoie une liste de listes décrivant les valeurs des cellules de la grille.
    >>> lire_grille("grille_simple1.txt")
    [[0, 0, 6, 0, 0, 3, 2, 7, 0], [0, 0, 2, 0, 0, 6, 0, 0, 0], [7, 0, 0, 2, 1, 5, 0, 0, 0], [0, 0, 3, 0, 2, 0, 0, 4, 1], [0, 0, 1, 0, 4, 9, 0, 0, 5], [5, 0, 0, 1, 0, 7, 0, 8, 2], [8, 6, 7, 0, 3, 0, 0, 2, 0], [3, 0, 0, 6, 0, 0, 0, 0, 0], [0, 1, 5, 0, 8, 0, 0, 0, 9]]
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
    Prend en argument une grille sous forme de liste de listes de nombres et un nom de fichier.
    Sauvegarde la grille fournie dans le fichier indiqué, en respectant le même format.
    """
    
    fichier = open(nom_fichier, "w")
    
    for i in range(len(grille)):
    
        for j in range(len(grille[0])) :
            
            fichier.write(str(grille[i][j]))
            
            fichier.write("\t")
            
        fichier.write("\n")
  
    fichier.close()
    
    
    
def colonnes(grille):
    """
    Prend en argument une liste de liste. 
    Renvoie une liste de liste des colonnes de la grille.
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
    Prend en argument une liste de listes.
    Renvoie True si pour toutes les listes de "liste", chaque élement de la liste ne possède qu'une seule occurrence renvoie False sinon.
    >>> compter_nb_occurrence([[2,2,1,5,3], [2,3,1,4,5], [1,1,1,3,5], [1,3,5,4,2], [5,4,3,2,1]])
    False
    >>> compter_nb_occurrence([[2,4,1,5,3], [2,3,1,4,5], [1,2,4,3,5], [1,3,5,4,2], [5,4,3,2,1]])
    True
    """
    
    for index in range(len(liste)):

        for element in liste[index]:
            
            nb_occurrence = liste[index].count(element)
            
            if nb_occurrence > 1 :
                
                return False
                    
    return True
    


def sans_conflit(grille) :
    """
    Prend en argument une liste de listes grille décrivant le contenu des cellules. 
    Renvoie True si aucune des cellules de la grille ne contient le même nombre qu’une autre cellule située sur la même ligne ou la même colonne, et False sinon.
    >>> sans_conflit([[2,2,1], [1,3,4], [3,1,2]])
    False 
    >>> sans_conflit([[2,4,1], [2,3,4], [3,1,2]])
    False
    >>> sans_conflit([[2,4,1], [1,3,4], [3,1,2]])
    True
    """
    
    # Même ligne    
    
    lignes_valide = compter_nb_occurrence(grille)
        
    # Même colonne
    
    colonnes_valide = compter_nb_occurrence(colonnes(grille))
    
    # Résultat
    
    if lignes_valide == True and colonnes_valide == True :
        
        return True
        
    else:

        return False
    
    
    
def cases_valides(grille):
    """
    Prend en argument une liste de listes grille décrivant le contenu des cellules. 
    Renvoie True si les cases (3*3) sont valides autrement dit s'il n'y a qu'une occurrence de chaque valeur dans la case, renvoie False sinon.
    >>> cases_valides([[1,2,3,4,5,6], [7,8,9,10,11,12], [13,14,15,16,17,18]])
    True
    >>> cases_valides([[2,2,3,4,5,6], [7,8,9,10,11,12], [13,14,15,16,17,18]])
    False
    """
    
    ensemble_cases = []
    
    i = 0
    
    while i < len(grille) :
        
        j = 0
        
        while j < len(grille[0]) :
            
            case = [grille[i][j], grille[i][j+1], grille[i][j+2], grille[i+1][j], grille[i+1][j+1], grille[i+1][j+2], grille[i+2][j], grille[i+2][j+1], grille[i+2][j+2]]
            
            ensemble_cases.append(case)
            
            j += 3
        
        i += 3
        
    if compter_nb_occurrence(ensemble_cases):
        
        return True
    
    else :
        
        return False
        

        
def grille_remplie(grille) :
    """
    Prend en argument une liste de listes grille décrivant le contenu des cellules. 
    Renvoie True si la grille est rempli, autrement dit si toutes les cases contiennent un numéro, renvoie False sinon.
    >>> grille_remplie([[0,1,2], [3,4,5]])
    False
    >>> grille_remplie([[1,1,2], [3,4,5]])
    True
    """
    
    for liste in grille :
        
        for element in liste :
            
            if element == 0 :
                
                return False
                
    return True
    
    
    
def afficher_grille_fenetre(grille, cases_depart):
    """
    Prend en argument une liste de listes représentant une grille et un ensemble représentant les cases de départ, et l’affiche joliment dans une fenêtre.
    """
    
    efface_tout()
    
    boutons()
    
    # Fond de la fenêtre
    
    rectangle(0, 0, largeur_plateau, hauteur_plateau, couleur = "#eaeaea", remplissage = "#eaeaea")
    
    # Contour de la grille
    
    rectangle(contour, contour, largeur_plateau-2*contour-largeur_bouton, hauteur_plateau-contour, remplissage = "white", epaisseur = 3)
    
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
        
        ligne(ax, ay, bx, by, couleur = '#A1A1A1', epaisseur = 3)
        
    for element in range(nb_lignes-1):
        
        ax = contour
        ay += hauteur_case
        bx = largeur_plateau-2*contour-largeur_bouton
        by = ay
        
        ligne(ax, ay, bx, by, couleur = '#A1A1A1', epaisseur = 3)
        
    # Traits plus foncés
    
    ax = contour
    ay = contour
    bx = contour
    by = contour
    
    for element in range(nb_colonnes):

        bx = ax
        by = hauteur_plateau-contour
        
        if element % 3 == 0 :
        
            ligne(ax, ay, bx, by, couleur = '#717171', epaisseur = 3)

        ax += largeur_case
        
    for element in range(nb_lignes):
        
        ax = contour
        bx = largeur_plateau-2*contour-largeur_bouton
        by = ay
        
        if element % 3 == 0 :
        
            ligne(ax, ay, bx, by, couleur = '#717171', epaisseur = 3)
        
        ay += hauteur_case
        
    rectangle(contour, contour, largeur_plateau-2*contour-largeur_bouton, hauteur_plateau-contour, couleur = "#717171", epaisseur = 3)
        
    # Valeurs des cases dans la grille
       
    for i in range(len(grille)) :
        
        for j in range(len(grille[0])) :
           
            if grille[i][j] != 0 and (i, j) in cases_depart:
                
                texte(j*largeur_case + contour + (largeur_case/2), i*hauteur_case + contour + (hauteur_case/2), str(grille[i][j]), couleur = "#0030E5", ancrage = "center", police = "Times New Roman", taille = 20)
        
        
        
def remplir_grille(grille, cases_depart, liste_evenement):
    """
    Prend en argument une liste de listes représentant une grille, un ensemble représentant les cases de départ et un liste de couple indiquant les coordonnées des cases jouées.
    Remplie dans la grille les nouvelles cases jouées au fur et à mesure de la partie.
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

    if coordonnee not in cases_depart :
        
        ax = coordonnee[1]*largeur_case+contour
        ay = coordonnee[0]*hauteur_case+contour
        
        rectangle(ax, ay, ax+largeur_case, ay+hauteur_case, couleur = "#0030E5", epaisseur = 3) 
        
        attend_ev()
        
        x = abscisse_souris()
        y = ordonnee_souris()
        
        valeur = 0
        
        if x >= largeur_plateau-largeur_bouton-contour and x <= largeur_plateau-contour-largeur_bouton/2-ecart_boutons/2 :
            
            if y >= hauteur_bouton*8+contour+8*ecart_boutons and y <= hauteur_bouton*9+contour+8*ecart_boutons :
                
                valeur = 1
                
            elif y >= hauteur_bouton*9+contour+9*ecart_boutons and y <= hauteur_bouton*10+contour+9*ecart_boutons :
                
                valeur = 3
                
            elif y >= hauteur_bouton*10+contour+10*ecart_boutons and y <= hauteur_bouton*11+contour+10*ecart_boutons :
                
                valeur = 5
                
            elif y >= hauteur_bouton*11+contour+11*ecart_boutons and y <= hauteur_bouton*12+contour+11*ecart_boutons :
                
                valeur = 7
                
            elif y >= hauteur_bouton*12+contour+12*ecart_boutons and y <= hauteur_bouton*13+contour+12*ecart_boutons :
                
                valeur = 9
                
        elif x >= largeur_plateau-contour-largeur_bouton/2+ecart_boutons/2 and x <= largeur_plateau-contour :
            
            if y >= hauteur_bouton*8+contour+8*ecart_boutons and y <= hauteur_bouton*9+contour+8*ecart_boutons :
                
                valeur = 2
                
            elif y >= hauteur_bouton*9+contour+9*ecart_boutons and y <= hauteur_bouton*10+contour+9*ecart_boutons :
                
                valeur = 4
                
            elif y >= hauteur_bouton*10+contour+10*ecart_boutons and y <= hauteur_bouton*11+contour+10*ecart_boutons :
                
                valeur = 6
                
            elif y >= hauteur_bouton*11+contour+11*ecart_boutons and y <= hauteur_bouton*12+contour+11*ecart_boutons :
                
                valeur = 8
                
        grille[coordonnee[0]][coordonnee[1]] = valeur
        
        if valeur != 0 :
    
            liste_evenement.append(coordonnee)
        
        afficher_cases_remplies(grille, cases_depart)
        
    else :
        
        texte((largeur_plateau-largeur_bouton-contour)/2, hauteur_plateau/2, "Impossible, c'est une case de départ !", couleur = "red", ancrage="center", police = "Helvetica", taille = 20)
        
        attente(1)
        
        
        
def afficher_cases_remplies(grille, cases_depart) :
    """
    Prend en argument une liste de listes représentant une grille et un ensemble représentant les cases de départ.
    Affiche les nouvelles cases jouées au fur et à mesure de la partie.
    """
    
    efface_tout()
    
    afficher_grille_fenetre(grille, cases_depart)
    
    largeur_case = (largeur_plateau-3*contour-largeur_bouton)/len(grille[0])
    hauteur_case = (hauteur_plateau-2*contour)/len(grille)
    
    for i in range(len(grille)) :
        
        for j in range(len(grille[0])):
            
            if (i,j) not in cases_depart and grille[i][j] != 0 :
                
                texte(j*largeur_case + contour + (largeur_case/2), i*hauteur_case + contour + (hauteur_case/2), str(grille[i][j]), couleur = "black", ancrage = "center", police = "Times New Roman", taille = 20)
        

    
def gagne(grille):
    """
    Prend en arguments une liste de liste grille décrivant le contenu des cellules.
    Renvoie True si toutes les règles du jeu sont respectées, sinon renvoie False.
    """
    
    if sans_conflit(grille) and cases_valides(grille) and grille_remplie(grille) :
        
        return True
    
    return False
    
    
    
def menu():
    """
    Affiche un menu proposant les choix des différentes grilles.
    """
    
    chiffre = randint(1,4)
    
    cases_depart = set()
    
    valeur = largeur_plateau/4
    
    # Fond du menu
    
    rectangle(0, 0, largeur_plateau-1, hauteur_plateau-1, couleur = 'black', remplissage = 'white', epaisseur = 3)
    texte(largeur_plateau/2, 2*contour, "SUDOKU", couleur = 'black', ancrage = 'center', police = 'Times new roman', taille = 30)
    texte(largeur_plateau/2, 3*contour, "( 数独 )", couleur = 'black', ancrage = 'center', police = 'Times new roman', taille = 15)
    ligne(valeur, 4*contour-ecart_boutons, 3*valeur, 4*contour-ecart_boutons, couleur = 'black', epaisseur = 1) 
    
    hauteur_bouton_menu = (hauteur_plateau-8*contour-2*ecart_boutons)/3
    largeur_bouton_menu = (largeur_plateau-8*contour)/2
    
    # Boutons de gauche
    
    rectangle(2*contour, 5*contour, largeur_bouton_menu+2*contour, 5*contour+hauteur_bouton_menu, couleur = 'black', remplissage = '#84d3ea', epaisseur = 2)
    rectangle(2*contour, 6*contour+hauteur_bouton_menu, largeur_bouton_menu+2*contour,6*contour+2*hauteur_bouton_menu, couleur = 'black', remplissage = '#43acca', epaisseur = 2)
    rectangle(2*contour, 7*contour+2*hauteur_bouton_menu, largeur_bouton_menu+2*contour,7*contour+3*hauteur_bouton_menu, couleur = 'black', remplissage = '#178daf', epaisseur = 2)
    
    texte(2*contour+largeur_bouton_menu/2, 5*contour+hauteur_bouton_menu/2, "GRILLE TRÈS SIMPLE", couleur = "white", ancrage = 'center', police = 'Times new roman', taille = 25)
    texte(2*contour+(largeur_bouton_menu/2), 6*contour+hauteur_bouton_menu/2+hauteur_bouton_menu, "GRILLE SIMPLE", couleur = "white", ancrage = 'center', police = 'Times new roman', taille = 25)
    texte(2*contour+largeur_bouton_menu/2, 7*contour+hauteur_bouton_menu/2+2*hauteur_bouton_menu, "GRILLE MOYENNE", couleur = "white", ancrage = 'center', police = 'Times new roman', taille = 25)
    
    # Boutons de droite
    
    rectangle(6*contour+largeur_bouton_menu, 5*contour, largeur_plateau-2*contour, 5*contour+hauteur_bouton_menu, couleur = 'black', remplissage = '#097897', epaisseur = 2)
    rectangle(6*contour+largeur_bouton_menu, 6*contour+hauteur_bouton_menu, largeur_plateau-2*contour,6*contour+2*hauteur_bouton_menu, couleur = 'black', remplissage = '#025b74', epaisseur = 2)
    rectangle(6*contour+largeur_bouton_menu, 7*contour+2*hauteur_bouton_menu, largeur_plateau-2*contour,7*contour+3*hauteur_bouton_menu, couleur = 'black', remplissage = '#a6a6a6', epaisseur = 2)
    
    texte(largeur_plateau-2*contour-largeur_bouton_menu/2, 5*contour+hauteur_bouton_menu/2, "GRILLE DIFFICILE", couleur = "white", ancrage = 'center', police = 'Times new roman', taille = 25)
    texte(largeur_plateau-2*contour-largeur_bouton_menu/2, 6*contour+hauteur_bouton_menu/2+hauteur_bouton_menu, "GRILLE TRÈS DIFFICILE", couleur = "white", ancrage = 'center', police = 'Times new roman', taille = 25)
    texte(largeur_plateau-2*contour-(largeur_bouton_menu/2), 7*contour+(hauteur_bouton_menu/2)+2*hauteur_bouton_menu, "FICHIER SAUVEGARDÉ", couleur = "white", ancrage = 'center', police = 'Times new roman', taille = 25)
    
    # Definition de la grille en fonction du clic
    
    x,y = attend_clic_gauche()
    
    grille = None
    
    if x >= 2*contour and x <= largeur_bouton_menu+2*contour :
        
        if y >= 5*contour and y <= 5*contour+hauteur_bouton_menu :
            
            grille = lire_grille("grille_tres_simple" + str(chiffre) + "_sudoku.txt")
            
        elif y >= 6*contour+hauteur_bouton_menu and y <= 6*contour+2*hauteur_bouton_menu :
            
            grille = lire_grille("grille_simple" + str(chiffre) + "_sudoku.txt")
                
        elif y >= 7*contour+2*hauteur_bouton_menu and y <= 7*contour+3*hauteur_bouton_menu :
            
            grille = lire_grille("grille_moyenne" + str(chiffre) + "_sudoku.txt")

    if x >= 6*contour+largeur_bouton_menu and x <= largeur_plateau-2*contour :
            
        if y >= 5*contour and y <= 5*contour+hauteur_bouton_menu :
            
            grille = lire_grille("grille_difficile" + str(chiffre) + "_sudoku.txt")

        elif y >= 6*contour+hauteur_bouton_menu and y <= 6*contour+2*hauteur_bouton_menu :
            
            grille = lire_grille("grille_tres_difficile" + str(chiffre) + "_sudoku.txt")

        elif y >= 7*contour+2*hauteur_bouton_menu and y <= 7*contour+3*hauteur_bouton_menu :    
            
            appel = lire_grille_cases_depart("fichier_sauvegarde_sudoku.txt")
            
            if appel[0] == [] :
                
                texte(largeur_plateau/2, hauteur_plateau/2, "IMPOSSIBLE, aucun fichier sauvegardé.", couleur = "red", ancrage = 'center', police = 'Times new roman', taille = 28)
                
                attente(1)
                
                grille = menu()[0]
                
            else :
                
                grille = appel[0]
                
                cases_depart = appel[1]
    
    if grille != None and cases_depart == set() : 
        
        for i in range(len(grille)) :
            
            for j in range(len(grille[0])):
                
                if grille[i][j] != 0 :
                    
                    cases_depart.add((i, j))
               
    return grille, cases_depart
    
    
    
def boutons():
    """
    Affiche les boutons dans la fenêtre.
    """

    rectangle(largeur_plateau-largeur_bouton-contour, contour, largeur_plateau-contour, hauteur_bouton+contour, couleur = "#000000", remplissage = "#FF3654", epaisseur = 2)
    texte(largeur_plateau-contour-(largeur_bouton/2), hauteur_bouton/2+contour, "QUITTER", couleur = 'black', ancrage = 'center', police = 'Times new roman', taille = 15)
    
    rectangle(largeur_plateau-largeur_bouton-contour,hauteur_bouton+contour+ecart_boutons,largeur_plateau-contour,hauteur_bouton*2+contour+ecart_boutons, couleur = "#000000", remplissage = "#FF369E", epaisseur = 2)
    texte(largeur_plateau-contour-(largeur_bouton/2), hauteur_bouton+ecart_boutons+(hauteur_bouton/2)+contour, "RECOMMENCER", couleur = 'black', ancrage = 'center', police = 'Times new roman', taille = 15)
    
    rectangle(largeur_plateau-largeur_bouton-contour,hauteur_bouton*2+contour+2*ecart_boutons,largeur_plateau-contour,hauteur_bouton*3+contour+2*ecart_boutons, couleur = "#000000", remplissage = "#FF36E4", epaisseur = 2)
    texte(largeur_plateau-contour-(largeur_bouton/2), 2*hauteur_bouton+2*ecart_boutons+(hauteur_bouton/2)+contour, "ANNULER", couleur = 'black', ancrage = 'center', police = 'Times new roman', taille = 15)
    
    rectangle(largeur_plateau-largeur_bouton-contour,hauteur_bouton*3+contour+3*ecart_boutons,largeur_plateau-contour,hauteur_bouton*4+contour+3*ecart_boutons, couleur = "#000000", remplissage = "#C536FF", epaisseur = 2)
    texte(largeur_plateau-contour-(largeur_bouton/2), 3*hauteur_bouton+3*ecart_boutons+(hauteur_bouton/2)+contour, "NOUVELLE PARTIE", couleur = 'black', ancrage = 'center', police = 'Times new roman', taille = 15)
    
    rectangle(largeur_plateau-largeur_bouton-contour,hauteur_bouton*4+contour+4*ecart_boutons,largeur_plateau-contour,hauteur_bouton*5+contour+4*ecart_boutons, couleur = "#000000", remplissage = "#8536FF", epaisseur = 2)
    texte(largeur_plateau-contour-(largeur_bouton/2), 4*hauteur_bouton+4*ecart_boutons+(hauteur_bouton/2)+contour, "SAUVEGARDER", couleur = 'black', ancrage = 'center', police = 'Times new roman', taille = 15)
    
    rectangle(largeur_plateau-largeur_bouton-contour,hauteur_bouton*5+contour+5*ecart_boutons,largeur_plateau-contour,hauteur_bouton*6+contour+5*ecart_boutons, couleur = "black", remplissage = "#363FFF", epaisseur = 2)
    texte(largeur_plateau-contour-(largeur_bouton/2), 5*hauteur_bouton+5*ecart_boutons+contour+(hauteur_bouton/2), "CONFLITS", couleur = 'black', ancrage = 'center', police = 'Times new roman', taille = 15)
    
    rectangle(largeur_plateau-largeur_bouton-contour,hauteur_bouton*6+contour+6*ecart_boutons,largeur_plateau-contour,hauteur_bouton*7+contour+6*ecart_boutons, couleur = "black", remplissage = "#367FFF", epaisseur = 2)
    texte(largeur_plateau-contour-(largeur_bouton/2), 6*hauteur_bouton+6*ecart_boutons+contour+(hauteur_bouton/2), "INDICE", couleur = 'black', ancrage = 'center', police = 'Times new roman', taille = 15)
    
    rectangle(largeur_plateau-largeur_bouton-contour,hauteur_bouton*7+contour+7*ecart_boutons,largeur_plateau-contour,hauteur_bouton*8+contour+7*ecart_boutons, couleur = "black", remplissage = "#717171", epaisseur = 2)
    texte(largeur_plateau-contour-(largeur_bouton/2), 7*hauteur_bouton+7*ecart_boutons+contour+(hauteur_bouton/2), "NOMBRE DE COUPS : " + str(evenements), couleur = 'black', ancrage = 'center', police = 'Times new roman', taille = 13)
    
    rectangle(largeur_plateau-largeur_bouton-contour,hauteur_bouton*8+contour+8*ecart_boutons,largeur_plateau-contour- largeur_bouton/2-ecart_boutons/2,hauteur_bouton*9+contour+8*ecart_boutons, couleur = "black", remplissage = "#A1A1A1", epaisseur = 2)
    texte(largeur_plateau-contour-(3/4)*largeur_bouton-ecart_boutons/4, 8*hauteur_bouton+8*ecart_boutons+contour+(hauteur_bouton/2), "1", couleur = 'black', ancrage = 'center', police = 'Times new roman', taille = 15)
    
    rectangle(largeur_plateau-contour-largeur_bouton/2+ecart_boutons/2,hauteur_bouton*8+contour+8*ecart_boutons,largeur_plateau-contour,hauteur_bouton*9+contour+8*ecart_boutons, couleur = "black", remplissage = "#A1A1A1", epaisseur = 2)
    texte(largeur_plateau-contour-(1/4)*largeur_bouton+ecart_boutons/4, 8*hauteur_bouton+8*ecart_boutons+contour+(hauteur_bouton/2), "2", couleur = 'black', ancrage = 'center', police = 'Times new roman', taille = 15)
    
    rectangle(largeur_plateau-largeur_bouton-contour,hauteur_bouton*9+contour+9*ecart_boutons,largeur_plateau-contour- largeur_bouton/2-ecart_boutons/2,hauteur_bouton*10+contour+9*ecart_boutons, couleur = "black", remplissage = "#A1A1A1", epaisseur = 2)
    texte(largeur_plateau-contour-(3/4)*largeur_bouton-ecart_boutons/4, 9*hauteur_bouton+9*ecart_boutons+contour+(hauteur_bouton/2), "3", couleur = 'black', ancrage = 'center', police = 'Times new roman', taille = 15)
    
    rectangle(largeur_plateau-contour-largeur_bouton/2+ecart_boutons/2,hauteur_bouton*9+contour+9*ecart_boutons,largeur_plateau-contour,hauteur_bouton*10+contour+9*ecart_boutons, couleur = "black", remplissage = "#A1A1A1", epaisseur = 2)
    texte(largeur_plateau-contour-(1/4)*largeur_bouton+ecart_boutons/4, 9*hauteur_bouton+9*ecart_boutons+contour+(hauteur_bouton/2), "4", couleur = 'black', ancrage = 'center', police = 'Times new roman', taille = 15)
    
    rectangle(largeur_plateau-largeur_bouton-contour,hauteur_bouton*10+contour+10*ecart_boutons,largeur_plateau-contour- largeur_bouton/2-ecart_boutons/2,hauteur_bouton*11+contour+10*ecart_boutons, couleur = "black", remplissage = "#A1A1A1", epaisseur = 2)
    texte(largeur_plateau-contour-(3/4)*largeur_bouton-ecart_boutons/4, 10*hauteur_bouton+10*ecart_boutons+contour+(hauteur_bouton/2), "5", couleur = 'black', ancrage = 'center', police = 'Times new roman', taille = 15)
    
    rectangle(largeur_plateau-contour-largeur_bouton/2+ecart_boutons/2,hauteur_bouton*10+contour+10*ecart_boutons,largeur_plateau-contour,hauteur_bouton*11+contour+10*ecart_boutons, couleur = "black", remplissage = "#A1A1A1", epaisseur = 2)
    texte(largeur_plateau-contour-(1/4)*largeur_bouton+ecart_boutons/4, 10*hauteur_bouton+10*ecart_boutons+contour+(hauteur_bouton/2), "6", couleur = 'black', ancrage = 'center', police = 'Times new roman', taille = 15)
    
    rectangle(largeur_plateau-largeur_bouton-contour,hauteur_bouton*11+contour+11*ecart_boutons,largeur_plateau-contour- largeur_bouton/2-ecart_boutons/2,hauteur_bouton*12+contour+11*ecart_boutons, couleur = "black", remplissage = "#A1A1A1", epaisseur = 2)
    texte(largeur_plateau-contour-(3/4)*largeur_bouton-ecart_boutons/4, 11*hauteur_bouton+11*ecart_boutons+contour+(hauteur_bouton/2), "7", couleur = 'black', ancrage = 'center', police = 'Times new roman', taille = 15)
    
    rectangle(largeur_plateau-contour-largeur_bouton/2+ecart_boutons/2,hauteur_bouton*11+contour+11*ecart_boutons,largeur_plateau-contour,hauteur_bouton*12+contour+11*ecart_boutons, couleur = "black", remplissage = "#A1A1A1", epaisseur = 2)
    texte(largeur_plateau-contour-(1/4)*largeur_bouton+ecart_boutons/4, 11*hauteur_bouton+11*ecart_boutons+contour+(hauteur_bouton/2), "8", couleur = 'black', ancrage = 'center', police = 'Times new roman', taille = 15)
    
    rectangle(largeur_plateau-largeur_bouton-contour,hauteur_bouton*12+contour+12*ecart_boutons,largeur_plateau-contour- largeur_bouton/2-ecart_boutons/2,hauteur_bouton*13+contour+12*ecart_boutons, couleur = "black", remplissage = "#A1A1A1", epaisseur = 2)
    texte(largeur_plateau-contour-(3/4)*largeur_bouton-ecart_boutons/4, 12*hauteur_bouton+12*ecart_boutons+contour+(hauteur_bouton/2), "9", couleur = 'black', ancrage = 'center', police = 'Times new roman', taille = 15)
    
    
    
def conversion_ensemble(str) :
    """
    Reçoit une chaine de caractère contenant uniquement des chiffres.
    Renvoie un ensemble de couple des valeurs de la chaîne de caractère.
    >>> conversion_ensemble('123456')
    {(1, 2), (3, 4), (5, 6)}
    """
    
    ensemble = set()
    
    i = 0
    
    while i < (len(str)) :
        
        ensemble.add((int(str[i]), int(str[i+1])))
        
        i += 2
        
    return ensemble
      
            

def lire_grille_cases_depart(nom_fichier):
    """ 
    Prend en argument une chaîne de caractères nom_fichier.
    Renvoie une liste de listes décrivant les valeurs des cellules de la grille et un ensemble décrivant les cases de départ.
    """

    fichier = open(nom_fichier, "r")
    
    contenu = fichier.readlines()
    
    fichier.close()
    
    cases_depart = set()
    
    hauteur = len(contenu)

    valeurs_cellules = []
    
    for i in range(hauteur-1):
        
        cellule = conversion(contenu[i])
        
        valeurs_cellules.append(cellule)
    
    if valeurs_cellules != [] :
        
        cases_depart = conversion_ensemble(contenu[hauteur-1])
        
    return valeurs_cellules, cases_depart
    
    

def sauvegarder(grille, cases_depart) :
    """
    Prend en argument une liste de listes grille décrivant le contenu des cellules et un ensemble, cases_depart.
    Sauvegarde une partie en cours, c'est-à-dire, la stock dans un fichier texte particulier prenant en compte les cases de départ (la dernière ligne du fichier, liste de chiffre à la suite).
    """
    
    ecrire_grille(grille, "fichier_sauvegarde_sudoku.txt")
    
    fichier = open("fichier_sauvegarde_sudoku.txt", "a")
    
    for couple in cases_depart :
        
        for valeur in couple : 
        
            fichier.write(str(valeur))
    
    fichier.close()
        


def doublons(liste, index_liste, ensemble_doublons, etat):
    """
    Prend en argument une liste ; un nombre index_liste correspondant à l'index de la liste dans la grille ; un ensemble ensemble_doublons et une chaîne de caractère etat pour savoir si la liste est une ligne ou une colonne.
    Modifie l'ensemble ensemble_doublons sur place.
    """

    for element in liste :
        
        if element != 0 :
        
            compte = []
            
            for i,e in enumerate(liste):
                
                if e == element :
                    
                    compte.append(i)
            
            if len(compte) >= 2:
                
                for i in compte :
                    
                    if etat == "ligne" :
                    
                        ensemble_doublons.add((index_liste, i))
                        
                    else :
                
                        ensemble_doublons.add((i, index_liste))    
        
        
        
def cases(grille) :
    """
    Prend en argument une liste de listes grille décrivant le contenu des cellules.
    Renvoie une liste de listes des différentes cases (3*3) de la grille
    """
    
    ensemble_cases = []
    
    i = 0
    
    while i < len(grille) :
        
        j = 0
        
        while j < len(grille[0]) :
            
            case = [grille[i][j], grille[i][j+1], grille[i][j+2], grille[i+1][j], grille[i+1][j+1], grille[i+1][j+2], grille[i+2][j], grille[i+2][j+1], grille[i+2][j+2]]
            
            ensemble_cases.append(case)
            
            j += 3
        
        i += 3
        
    return ensemble_cases
    
    
        
def conflits(grille):
    """
    Prend en argument une liste de listes grille décrivant le contenu des cellules.
    Renvoie un ensemble, ensemble_doublons, représentant les conflits de cellules en ligne ou en colonne et un autre ensemble, index_case, représentant les cases (3*3) en conflits. Les deux ensembles sont composés de couple de coordonnées.
    """
    
    ensemble_doublons = set()
    
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
        
    ensemble_cases = cases(grille)
    
    compteur_colonne = 0
    compteur_ligne = 0
    
    valeur  = len(ensemble_cases)/(len(grille)/3)
    
    index_case = set()
    
    for index in range(len(ensemble_cases)):
        
        if index % valeur == 0 and index != 0 :
            
            compteur_ligne += 1
            compteur_colonne = 0

        for element in ensemble_cases[index]:
            
            if element != 0 :
            
                nb_occurrence = ensemble_cases[index].count(element)
                
                if nb_occurrence > 1  :
                    
                    index_case.add((compteur_ligne, compteur_colonne))
           
        compteur_colonne += 1
                
    return ensemble_doublons, index_case
    


def afficher_conflits(grille) :
    """
    Prend en argument une liste de listes grille décrivant le contenu des cellules.
    Fait apparaître les cases (3*3) et les cellules en conflits.
    """
    
    largeur_case = (largeur_plateau-3*contour-largeur_bouton)/len(grille[0])
    hauteur_case = (hauteur_plateau-2*contour)/len(grille)
    
    ensemble_doublons, index_case = conflits(grille)
    
    if ensemble_doublons != set() :
        
        for i,j in ensemble_doublons :
            
            ax = contour+j*largeur_case
            ay = contour+i*hauteur_case
            
            rectangle(ax, ay, ax+largeur_case, ay+hauteur_case, couleur = "#FF0000", epaisseur = 4)
            
    if index_case != set() :
        
        for i,j in index_case :
            
            ax = contour+(j*(3*largeur_case))
            ay = contour+(i*(3*hauteur_case))
            
            rectangle(ax, ay, ax+(3*largeur_case), ay+(3*hauteur_case), couleur = "#FF7000", epaisseur = 4)  
            
            

def indice(grille):
    """
    Prend en argument une liste de listes grille décrivant le contenu des cellules.
    Fait apparaitre les cellules de la même valeur, selectionné ultérieurement.
    """
    
    largeur_case = (largeur_plateau-3*contour-largeur_bouton)/len(grille[0])
    hauteur_case = (hauteur_plateau-2*contour)/len(grille)
    
    texte((largeur_plateau-largeur_bouton-contour)/2, hauteur_plateau/2, "Appuyez sur le chiffre dont vous voulez voir les emplacements !", couleur = "red", ancrage="center", police = "Helvetica", taille = 20)
    
    attend_ev()
    
    afficher_cases_remplies(grille, cases_depart)
    boutons()
    
    x = abscisse_souris()
    y = ordonnee_souris()
    
    valeur = 0
    
    if x >= largeur_plateau-largeur_bouton-contour and x <= largeur_plateau-contour-largeur_bouton/2-ecart_boutons/2 :
        
        if y >= hauteur_bouton*8+contour+8*ecart_boutons and y <= hauteur_bouton*9+contour+8*ecart_boutons :
            
            valeur = 1
            
        elif y >= hauteur_bouton*9+contour+9*ecart_boutons and y <= hauteur_bouton*10+contour+9*ecart_boutons :
            
            valeur = 3
            
        elif y >= hauteur_bouton*10+contour+10*ecart_boutons and y <= hauteur_bouton*11+contour+10*ecart_boutons :
            
            valeur = 5
            
        elif y >= hauteur_bouton*11+contour+11*ecart_boutons and y <= hauteur_bouton*12+contour+11*ecart_boutons :
            
            valeur = 7
            
        elif y >= hauteur_bouton*12+contour+12*ecart_boutons and y <= hauteur_bouton*13+contour+12*ecart_boutons :
            
            valeur = 9
            
    elif x >= largeur_plateau-contour-largeur_bouton/2+ecart_boutons/2 and x <= largeur_plateau-contour :
        
        if y >= hauteur_bouton*8+contour+8*ecart_boutons and y <= hauteur_bouton*9+contour+8*ecart_boutons :
            
            valeur = 2
            
        elif y >= hauteur_bouton*9+contour+9*ecart_boutons and y <= hauteur_bouton*10+contour+9*ecart_boutons :
            
            valeur = 4
            
        elif y >= hauteur_bouton*10+contour+10*ecart_boutons and y <= hauteur_bouton*11+contour+10*ecart_boutons :
            
            valeur = 6
            
        elif y >= hauteur_bouton*11+contour+11*ecart_boutons and y <= hauteur_bouton*12+contour+11*ecart_boutons :
            
            valeur = 8
            
    ensemble_cases_identiques = set()

    if valeur != 0 :
    
        for i in range(len(grille)):
            
            for j in range(len(grille[0])):
                
                if grille[i][j] == valeur :
                    
                    ensemble_cases_identiques.add((i,j))
                
    if ensemble_cases_identiques != set() :
        
        for i,j in ensemble_cases_identiques :
                
            ax = j*largeur_case+contour
            ay = i*hauteur_case+contour
            
            rectangle(ax, ay, ax+largeur_case, ay+hauteur_case, couleur = "#F1F732", epaisseur = 3) 
            
            
    
    
# INITIALISATION


contour = 30

largeur_plateau = 1090 
hauteur_plateau = 660

nb_boutons = 13

ecart_boutons = 15

largeur_bouton = 200
hauteur_bouton = (hauteur_plateau-2*contour-(ecart_boutons*(nb_boutons-1)))/nb_boutons

fenetre = cree_fenetre(largeur_plateau,hauteur_plateau)

valeurs_menu = menu()

while valeurs_menu[0] == None:
    
    valeurs_menu = menu()
    
grille, cases_depart = valeurs_menu[0], valeurs_menu[1]

temps_debut = time.time()

liste_evenement = []

grille_depart = copy.deepcopy(grille)

evenements = 0


# BOUCLE PRINCIPALE

        
while True :    

    afficher_cases_remplies(grille, cases_depart)
    
    boutons() 
    
    if gagne(grille) == True :
        
        temps = time.time()
        
        texte((largeur_plateau-contour-largeur_bouton)/2, hauteur_plateau/2,"BRAVO ! Vous avez gagné !", couleur = '#FE0000', ancrage = 'center', police = 'Times new roman', taille = 48)
        
        texte((largeur_plateau-contour-largeur_bouton)/2, hauteur_plateau/2+2*contour,"Temps de jeu : " + str(round((temps-temps_debut),2)), couleur = '#FF6565', ancrage = 'center', police = 'Times new roman', taille = 30)
        
    attend_ev()
    
    if ordonnee_souris() >= contour and ordonnee_souris() <= hauteur_plateau-contour :
        
        if abscisse_souris() >= contour and abscisse_souris() <= largeur_plateau-2*contour-largeur_bouton :
            
            remplir_grille(grille, cases_depart, liste_evenement)
            
            evenements += 1
            
        elif abscisse_souris() >= largeur_plateau-contour-largeur_bouton and abscisse_souris() <= largeur_plateau-contour :
            
            if ordonnee_souris() >= contour and ordonnee_souris() <= hauteur_bouton+contour :
                
                break
                
            elif ordonnee_souris() >= hauteur_bouton+contour+ecart_boutons and ordonnee_souris() <= hauteur_bouton*2+contour+ecart_boutons :
                
                grille = copy.deepcopy(grille_depart)
                
                liste_evenement = []
                
                evenements = 0
                
                temps_debut = time.time()
                
            elif ordonnee_souris() >= hauteur_bouton*2+contour+2*ecart_boutons and ordonnee_souris() <= hauteur_bouton*3+contour+2*ecart_boutons :
                
                if  liste_evenement != []:
                
                    dernier_i = liste_evenement[-1][0]
                    dernier_j = liste_evenement[-1][1]
                    
                    grille[dernier_i][dernier_j] = 0
                    
                    liste_evenement.pop(-1) 
                
            elif ordonnee_souris() >= hauteur_bouton*3+contour+3*ecart_boutons and ordonnee_souris() <= hauteur_bouton*4+contour+3*ecart_boutons :
                
                evenements = 0
                
                valeurs_menu = menu()
                
                while valeurs_menu[0] == None:
                    
                    valeurs_menu = menu()
                
                grille, cases_depart = valeurs_menu[0], valeurs_menu[1]
                
                temps_debut = time.time()
                
                afficher_cases_remplies(grille, cases_depart)
                
                liste_evenement = []
                
                grille_depart = copy.deepcopy(grille)
                
            elif ordonnee_souris() >= hauteur_bouton*4+contour+4*ecart_boutons and ordonnee_souris() <= hauteur_bouton*5+contour+4*ecart_boutons :
                
                sauvegarder(grille, cases_depart)
                
            elif ordonnee_souris() >= hauteur_bouton*5+contour+5*ecart_boutons and ordonnee_souris() <= hauteur_bouton*6+contour+5*ecart_boutons :
                
                afficher_conflits(grille)
                
                attend_ev()
                
            elif ordonnee_souris() >= hauteur_bouton*6+contour+6*ecart_boutons and ordonnee_souris() <= hauteur_bouton*7+contour+6*ecart_boutons :
                
                indice(grille)
                
                attend_ev()
            
    boutons() 
    
    mise_a_jour()
    
# Fermeture et sortie    
    
ferme_fenetre()