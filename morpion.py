from bibliotheque import*
import copy
import time
from random import randint


def afficher_grille() :
    """
    Affiche le quadrillage, les valeurs de la grille, un case de message et les boutons joliment dans la fenêtre.
    """
    
    rectangle(0, 0, largeur_plateau, hauteur_plateau, remplissage = "white")
    
    # Quadrillage
    
    rectangle(contour, contour, contour+taille_grille, contour+taille_grille, couleur = 'black', remplissage = 'white', epaisseur = 2)
    
    ax = contour
    ay = contour
    
    for i in range(len(grille)):
        
        ax += taille_grille/len(grille)
        by = ay+taille_grille
        
        ligne(ax, ay, ax, by, couleur = 'black', epaisseur = 2)
       
    ax = contour
    ay = contour
       
    for i in range(len(grille)):
        
        ay += taille_grille/len(grille)
        bx = ax+taille_grille
        
        ligne(ax, ay, bx, ay, couleur = 'black', epaisseur = 2)
        
    # Case message
    
    ax = 2*contour+taille_grille
    bx = ax+largeur_bouton
    ay = hauteur_plateau-contour-largeur_bouton
        
    rectangle(ax, ay, bx, ay+largeur_bouton, couleur = "black", remplissage = "white", epaisseur = 2)
    
    # Boutons
    
    ay = contour
    by = ay+hauteur_bouton
    
    rectangle(ax, ay, bx, by, couleur = "black", remplissage = '#226BF4', epaisseur = 2)
    texte(ax+largeur_bouton/2, ay+hauteur_bouton/2, "QUITTER", couleur = "black", ancrage = "center", police = "Times New Roman" , taille = 16)
    rectangle(ax, by+ecart_boutons, bx, by+ecart_boutons+hauteur_bouton, couleur = "black", remplissage = '#4222F4', epaisseur = 2)
    texte(ax+largeur_bouton/2, by+ecart_boutons+hauteur_bouton/2, "NOUVELLE PARTIE", couleur = "black", ancrage = "center", police = "Times New Roman" , taille = 16)
    rectangle(ax, by+2*ecart_boutons+hauteur_bouton, bx, by+2*ecart_boutons+2*hauteur_bouton, couleur = "black", remplissage = '#AB22F4', epaisseur = 2)
    texte(ax+largeur_bouton/2, by+2*ecart_boutons+hauteur_bouton+hauteur_bouton/2, "RECOMMENCER", couleur = "black", ancrage = "center", police = "Times New Roman" , taille = 16)
    rectangle(ax, by+3*ecart_boutons+2*hauteur_bouton, bx, by+3*ecart_boutons+3*hauteur_bouton, couleur = "black", remplissage = '#F422D4', epaisseur = 2)
    texte(ax+largeur_bouton/2, by+3*ecart_boutons+2*hauteur_bouton+hauteur_bouton/2, "ANNULER", couleur = "black", ancrage = "center", police = "Times New Roman" , taille = 16)
    
    # Affichage jeu 
    
    taille_case = taille_grille/len(grille)
    ecart = 15
    
    for i in range(len(grille)) :
        
        for j in range(len(grille[0])) :
            
            if grille[i][j] == 1 :
                
                ax = contour+j*taille_case
                ay = contour+i*taille_case
                
                ligne(ax+ecart, ay+ecart, ax+taille_case-ecart, ay+taille_case-ecart, couleur = 'red', epaisseur = 2)
                ligne(ax+taille_case-ecart, ay+ecart, ax+ecart, ay+taille_case-ecart, couleur = 'red', epaisseur = 2)
                
            if grille[i][j] == 2 :
                
                x = contour+j*taille_case+taille_case/2
                y = contour+i*taille_case+taille_case/2
                
                cercle(x, y, taille_case/2-ecart, couleur = '#00FF08', epaisseur = 2)
    
    
    
def joueur(etat_jeu) :
    """
    Prend en argument une valeur etat_jeu, 1 si c'est au joueur 1 de jouer, 2 si c'est au joueur 2 de jouer.
    Affiche dans la case message si c'est au joueur 1 ou au joueur 2 de jouer.
    """
    
    x = largeur_plateau-contour-largeur_bouton/2
    y_1 = hauteur_plateau-contour-(3/4)*largeur_bouton
    y_2 = hauteur_plateau-contour-(2/4)*largeur_bouton
    y_3 = hauteur_plateau-contour-(1/4)*largeur_bouton
    
    
    if etat_jeu == 1 :
        
        texte(x, y_1, "JOUEUR 1 :", couleur = 'red', ancrage = 'center', police = "Times New Roman" , taille = 18)
        texte(x, y_2, "A TOI DE JOUER", couleur = 'red', ancrage = 'center', police = "Times New Roman" , taille = 18)
        texte(x, y_3, "(CROIX)", couleur = 'red', ancrage = 'center', police = "Times New Roman" , taille=16)
        
    if etat_jeu == 2 :
        
        texte(x, y_1, "JOUEUR 2 :", couleur = '#00FF08', ancrage = 'center', police = "Times New Roman" , taille = 18)
        texte(x, y_2, "A TOI DE JOUER", couleur = '#00FF08', ancrage = 'center', police = "Times New Roman" , taille = 18)
        texte(x, y_3, "(ROND)", couleur = '#00FF08', ancrage = 'center', police = "Times New Roman" , taille = 16)
     
        
        
def colonnes(grille):
    """
    Prend en argument une liste de listes grille et renvoie une liste de listes des colonnes de la grille.
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
    

        
def gagne(grille):
    """
    Prend en argument une liste de liste grille. 
    Renvoie (True, 1) si le joueur 1 a gagné, c'est-à-dire si une ligne, une colonne ou une diagonale n'est composé que de croix. Renvoie (True, 2) si le joueur 2 a gagné, c'est-à-dire si une ligne, une colonne ou une diagonale n'est composé que de rond. Renvoie (False, 0) sinon.
    >>> gagne([[0,0,0], [0,0,0], [0,0,0]])
    (False, 0)
    >>> gagne([[1,1,1], [2,2,0], [0,0,0]])
    (True, 1)
    >>> gagne([[1,1,2], [2,2,2], [1,1,0]])
    (True, 2)
    """
    
    liste_colonnes = colonnes(grille)
    
    diagonale_1 = []
    diagonale_2 = []
    
    for i in range(len(grille)):
        
        diagonale_1.append(grille[i][i])
        diagonale_2.append(grille[i][len(grille)-1-i])
        
    if grille[0].count(1) == len(grille) or grille[1].count(1) == len(grille) or grille[2].count(1) == len(grille) or liste_colonnes[0].count(1) == len(grille) or  liste_colonnes[1].count(1) == len(grille) or liste_colonnes[2].count(1) == len(grille) or diagonale_1.count(1) == len(grille) or diagonale_2.count(1) == len(grille):
        
        return True, 1
    
    elif grille[0].count(2) == len(grille) or grille[1].count(2) == len(grille) or grille[2].count(2) == len(grille) or liste_colonnes[0].count(2) == len(grille) or  liste_colonnes[1].count(2) == len(grille) or liste_colonnes[2].count(2) == len(grille) or diagonale_1.count(2) == len(grille) or diagonale_2.count(2) == len(grille) :
        
        return True, 2
        
    else : 
    
        return False, 0
        
        
        
def remplir_grille(grille, etat_jeu) :
    """
    Prends en argument une liste de listes grille et un valeur etat_ jeu, 1 ou 2 selon le joueur qui doit jouer.
    Renvoie les coordonnées de la case où il y a eu le clic.
    """
    
    largeur_case = (largeur_plateau-3*contour-largeur_bouton)/len(grille)
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
        
    return (i-1, j-1)
    
    
    
def menu():
    """
    Affiche un menu proposant les choix des différentes grilles.
    """
    
    cases_depart = set()
    
    valeur = largeur_plateau/4
    
    # Fond du menu
    
    rectangle(0, 0, largeur_plateau-1, hauteur_plateau-1, couleur = 'black', remplissage = 'white', epaisseur = 3)
    texte(largeur_plateau/2, 2*contour, "MORPION", couleur='black', ancrage='center', police='Times new roman', taille=30)
    ligne(valeur, 4*contour-ecart_boutons, 3*valeur, 4*contour-ecart_boutons, couleur='black', epaisseur=1, tag='') 
    
    hauteur_bouton_menu = (hauteur_plateau-8*contour-2*ecart_boutons)/3
    largeur_bouton_menu = (largeur_plateau-8*contour)/2
    
    # Boutons
    
    rectangle(largeur_plateau/2-2*contour, 5*contour, largeur_plateau/2+2*contour, 5*contour+hauteur_bouton_menu, couleur = 'black', remplissage = '#84d3ea', epaisseur = 2)
    rectangle(largeur_plateau/2-2*contour, 6*contour+hauteur_bouton_menu, largeur_plateau/2+2*contour,6*contour+2*hauteur_bouton_menu, couleur = 'black', remplissage = '#43acca', epaisseur = 2)
    rectangle(largeur_plateau/2-2*contour, 7*contour+2*hauteur_bouton_menu, largeur_plateau/2+2*contour,7*contour+3*hauteur_bouton_menu, couleur = 'black', remplissage = '#178daf', epaisseur = 2)
    
    texte(largeur_plateau/2, 5*contour+hauteur_bouton_menu/2, "3 × 3", couleur="white", ancrage = 'center', police='Times new roman', taille=25)
    texte(largeur_plateau/2, 6*contour+hauteur_bouton_menu/2+hauteur_bouton_menu, "4 × 4", couleur="white", ancrage = 'center', police='Times new roman', taille=25)
    texte(largeur_plateau/2, 7*contour+hauteur_bouton_menu/2+2*hauteur_bouton_menu, "5 × 5", couleur="white", ancrage = 'center', police='Times new roman', taille=25)
    
    # Definition de la grille en fonction du clic
    
    x,y = attend_clic_gauche()
    
    grille = None
    
    if x >= largeur_plateau/2-2*contour and x <= largeur_plateau/2+2*contour :
        
        if y >= 5*contour and y <= 5*contour+hauteur_bouton_menu :
            
            grille = [[0,0,0], [0,0,0], [0,0,0]]
            
        elif y >= 6*contour+hauteur_bouton_menu and y <= 6*contour+2*hauteur_bouton_menu :
            
            grille = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
                
        elif y >= 7*contour+2*hauteur_bouton_menu and y <= 7*contour+3*hauteur_bouton_menu :
            
            grille = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]
               
    return grille
    
    
    
def grille_remplie(grille) :
    """
    Prend en argument une liste de listes. 
    Renvoie True si la grille est remplie, c'est-à-dire si la liste de liste n'est composé que de 1 et de 2, renvoie False sinon.
    """
    
    compteur = 0
    
    for liste in grille :
        
        for element in liste :
            
            if element == 1 or element == 2 :
                
                compteur += 1 
                
    if len(grille)*len(liste) == compteur :
        
        return True
        
    else : 

        return False
            
            
    
    
# INITIALISATION


contour = 30

largeur_plateau = 790 
hauteur_plateau = 560

taille_grille = 500

nb_boutons = 4

ecart_boutons = 15

largeur_bouton = 200
hauteur_bouton = (hauteur_plateau-2*contour-(ecart_boutons*(nb_boutons))-largeur_bouton)/nb_boutons

fenetre = cree_fenetre(largeur_plateau,hauteur_plateau)

valeur_menu = menu()

while valeur_menu == None:
    
    valeur_menu = menu()
    
grille = valeur_menu

grille_depart = copy.deepcopy(grille)

liste_evenement = []

evenements = 0

compteur = 1

cases_remplies = set()

temps_debut = time.time()

score_j_1 = 0
score_j_2 = 0

valeur_score = None


# BOUCLE PRINCIPALE


while True :
    
    etat_jeu = 1
    
    if compteur % 2 == 0 :
        
        etat_jeu = 2
    
    afficher_grille()
    
    joueur(etat_jeu)
    
    etat_victoire = gagne(grille)
    
    if etat_victoire[0] == True or grille_remplie(grille) == True :
        
        temps = time.time()
        
        if etat_victoire[1] == 1 :
        
            texte((largeur_plateau-contour-largeur_bouton)/2, 2*contour+taille_grille*(1/3), "BRAVO JOUEUR 1 !", couleur = 'red', ancrage = 'center', police = 'Times new roman', taille = 30)
            texte((largeur_plateau-contour-largeur_bouton)/2, taille_grille*(2/3)-2*contour, "Vous avez gagné ! !", couleur = 'red', ancrage = 'center', police = 'Times new roman', taille = 30)
            
            if valeur_score == None :
            
                score_j_1 += 1
                
                valeur_score = True
            
        if etat_victoire[1] == 2 :
            
            texte((largeur_plateau-contour-largeur_bouton)/2, 2*contour+taille_grille*(1/3), "BRAVO JOUEUR 2 !", couleur = '#00FF08', ancrage = 'center', police = 'Times new roman', taille = 30)
            texte((largeur_plateau-contour-largeur_bouton)/2, taille_grille*(2/3)-2*contour, "Vous avez gagné ! !", couleur = '#00FF08', ancrage = 'center', police = 'Times new roman', taille = 30)
            
            if valeur_score == None :
            
                score_j_2 += 1
                
                valeur_score = True
                
        if etat_victoire[0] != True :
            
            texte((largeur_plateau-contour-largeur_bouton)/2, taille_grille*(2/3)-2*contour, "MATCH NUL !", couleur = 'blue', ancrage = 'center', police = 'Times new roman', taille = 35)
        
        texte((largeur_plateau-contour-largeur_bouton)/2, taille_grille*(2/3)-(2/3)*contour, "Temps de jeu : " + str(round((temps-temps_debut),2)), couleur = 'grey', ancrage = 'center', police = 'Times new roman', taille = 25)
            
        ax = 2*contour+taille_grille
        bx = ax+largeur_bouton
        ay = hauteur_plateau-contour-largeur_bouton
        
        rectangle(ax, ay, bx, ay+largeur_bouton, couleur = "black", remplissage = "white", epaisseur = 2)
        texte(ax+largeur_bouton/2, ay+largeur_bouton*(1/3), "SCORE JOUEUR 1 : " + str(score_j_1), couleur = 'red', ancrage = 'center', police = 'Times new roman', taille = 15)
        texte(ax+largeur_bouton/2, ay+largeur_bouton*(2/3), "SCORE JOUEUR 2 : " + str(score_j_2), couleur = '#00FF08', ancrage = 'center', police = 'Times new roman', taille = 15)
        
    attend_ev()
    
    if abscisse_souris() >= contour and abscisse_souris() <= largeur_plateau-2*contour-largeur_bouton and ordonnee_souris() >= contour and ordonnee_souris() <= hauteur_plateau-contour and etat_victoire[0] != True :

        joueur(etat_jeu)
        
        i, j = remplir_grille(grille, etat_jeu)
        
        if (i, j) not in cases_remplies :
            
            cases_remplies.add((i,j))
            
            liste_evenement.append((i,j))
            
            if etat_jeu == 1 :
            
                grille[i][j] = 1
                
            if etat_jeu == 2 :
                
                grille[i][j] = 2
                
        else :
            
            compteur -= 1
            
    elif abscisse_souris() >= largeur_plateau-contour-largeur_bouton and abscisse_souris() <= largeur_plateau-contour and ordonnee_souris() >= contour and ordonnee_souris() <= hauteur_plateau-contour :
        
        if ordonnee_souris() >= contour and ordonnee_souris() <= hauteur_bouton+contour :
            
            break
            
        elif ordonnee_souris() >= hauteur_bouton+contour+ecart_boutons and ordonnee_souris() <= hauteur_bouton*2+contour+ecart_boutons :
            
            evenements = 0
            
            compteur = 0
            
            valeurs_menu = menu()
            
            while valeurs_menu == None :
                
                valeurs_menu = menu()
            
            grille = valeurs_menu
            
            cases_remplies = set()
            
            temps_debut = time.time()
            
            afficher_grille()
            
            score_j_1 = 0
            score_j_2 = 0
            
            valeur_score = None
            
            liste_evenement = []
            
            grille_depart = copy.deepcopy(grille)
            
        elif ordonnee_souris() >= hauteur_bouton*2+contour+2*ecart_boutons and ordonnee_souris() <= hauteur_bouton*3+contour+2*ecart_boutons :
            
            grille = copy.deepcopy(grille_depart)
            
            temps_debut = time.time()
            
            liste_evenement = []
            
            evenements = 0
            
            compteur = 0
            
            valeur_score = None

            cases_remplies = set()
            
        elif ordonnee_souris() >= hauteur_bouton*3+contour+3*ecart_boutons and ordonnee_souris() <= hauteur_bouton*4+contour+3*ecart_boutons :
            
            if  liste_evenement != []:
            
                dernier_i = liste_evenement[-1][0]
                dernier_j = liste_evenement[-1][1]
                
                grille[dernier_i][dernier_j] = 0
                
                cases_remplies.remove((dernier_i, dernier_j))
                
                liste_evenement.pop(-1) 
                
            compteur -= 2
            
    else :
        
        compteur -= 1

    compteur += 1
    
    
ferme_fenetre()
    
    