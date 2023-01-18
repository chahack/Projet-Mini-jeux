from bibliotheque import *
from time import sleep
from random import randint
import time



def case_vers_pixel(case) :
    """
    Prend en argument un couple de coordonnée, case.
    Fonction recevant les coordonnées d'une case du plateau sous la forme d'un couple d'entiers (ligne, colonne) et renvoyant les coordonnées du pixel se trouvant au centre de cette case. Ce calcul prend en compte la taille de chaque case, donnée par la variable globale taille_case.
    """
    
    i, j = case
    
    return (i + .5) * taille_case, (j + .5) * taille_case
    
    

def affiche_fond(nb_joueurs) :
    """
    Prend en argument un valeur nb_joueur (1 ou 2).
    Fait les différents affichage de la fenêtre.
    """
    
    # Fond
    
    x, y = largeur_fenetre * taille_case, hauteur_fenetre * taille_case
    
    rectangle(0, 0, x, y, couleur = 'black', remplissage = '#E0EBF0', epaisseur = 2)
    
    rectangle(contour * taille_case, contour * taille_case, (contour+largeur_plateau) * taille_case, (contour+hauteur_plateau) * taille_case, couleur = 'black', remplissage = "white", epaisseur = 2)
    
    # Boutons
    
    ax = (2*contour+largeur_plateau)*taille_case
    
    texte(ax+(largeur_boutons*taille_case)/2, (contour+hauteur_boutons/2)*taille_case, "BOUTONS :", ancrage = 'center', police = 'Times New Roman', taille = 16)
    ligne(ax+(largeur_boutons*taille_case)/2-4*ecart*taille_case, contour*taille_case+(hauteur_boutons/2+ecart)*taille_case, ax+(largeur_boutons/2+4*ecart)*taille_case, (contour+hauteur_boutons/2+ecart)*taille_case, epaisseur = 1)
    rectangle(ax, (contour+hauteur_boutons+ecart)*taille_case, ax+largeur_boutons*taille_case, (contour+2*hauteur_boutons+ecart)*taille_case, couleur = 'black', remplissage = '#D8D8D8', epaisseur = 2)
    texte(ax+(largeur_boutons*taille_case)/2, (contour+ecart+hauteur_boutons*(3/2))*taille_case, "NOUVELLE PARTIE", ancrage = 'center', police = 'Times New Roman', taille = 16)
    rectangle(ax, (contour+2*hauteur_boutons+2*ecart)*taille_case, ax+largeur_boutons*taille_case, (contour+3*hauteur_boutons+2*ecart)*taille_case, couleur = 'black', remplissage = '#BFBFBF', epaisseur = 2)
    texte(ax+(largeur_boutons*taille_case)/2, (contour+2*ecart+hauteur_boutons*(5/2))*taille_case, "PAUSE", ancrage = 'center', police = 'Times New Roman', taille = 16)
    rectangle(ax, (contour+3*hauteur_boutons+3*ecart)*taille_case, ax+largeur_boutons*taille_case, (contour+4*hauteur_boutons+3*ecart)*taille_case, couleur = 'black', remplissage = '#7D7D7D', epaisseur = 2)
    texte(ax+(largeur_boutons*taille_case)/2, (contour+3*ecart+hauteur_boutons*(7/2))*taille_case, "QUITTER", ancrage = 'center', police = 'Times New Roman', taille = 16)
    
    # Case de message, score et description des commandes
    
    if nb_joueurs == 1 :

        rectangle((largeur_fenetre-contour-largeur_boutons)*taille_case, (hauteur_fenetre-contour-11*ecart)*taille_case, (largeur_fenetre-contour)*taille_case, (hauteur_fenetre-contour)*taille_case, couleur = 'black', remplissage = 'white', epaisseur = 2)
            
        texte((largeur_fenetre-contour-largeur_boutons/2)*taille_case, (hauteur_fenetre-contour-9*ecart)*taille_case, "Score : " + str(score), couleur = 'black', ancrage = 'center', police = 'Helvetica', taille = 18)
        texte((largeur_fenetre-contour-largeur_boutons/2)*taille_case, (hauteur_fenetre-contour-(13/2)*ecart)*taille_case, "Haut : Flèche du haut", couleur = 'black', ancrage = 'center', police = 'Helvetica', taille = 12) 
        texte((largeur_fenetre-contour-largeur_boutons/2)*taille_case, (hauteur_fenetre-contour-5*ecart)*taille_case, "Bas : Flèche du bas", couleur = 'black', ancrage = 'center', police = 'Helvetica', taille = 12) 
        texte((largeur_fenetre-contour-largeur_boutons/2)*taille_case, (hauteur_fenetre-contour-(7/2)*ecart)*taille_case, "Droite : Flèche droite", couleur = 'black', ancrage = 'center', police = 'Helvetica', taille = 12)
        texte((largeur_fenetre-contour-largeur_boutons/2)*taille_case, (hauteur_fenetre-contour-2*ecart)*taille_case, "Gauche : Flèche gauche", couleur = 'black', ancrage = 'center', police = 'Helvetica', taille = 12) 
        
    if nb_joueurs == 2 :
        
        rectangle((largeur_fenetre-contour-largeur_boutons)*taille_case, (hauteur_fenetre-contour-16*ecart)*taille_case, (largeur_fenetre-contour)*taille_case, (hauteur_fenetre-contour)*taille_case, couleur = 'black', remplissage = 'white', epaisseur = 2)
        
        texte((largeur_fenetre-contour-largeur_boutons/2)*taille_case, (hauteur_fenetre-contour-(29/2)*ecart)*taille_case, "JOUEUR 1", couleur = 'black', ancrage = 'center', police = 'Helvetica', taille = 14)
        texte((largeur_fenetre-contour-largeur_boutons/2)*taille_case, (hauteur_fenetre-contour-13*ecart)*taille_case, "Score : " + str(score), couleur = 'black', ancrage = 'center', police = 'Helvetica', taille = 12)
        texte((largeur_fenetre-contour-largeur_boutons/2)*taille_case, (hauteur_fenetre-contour-12*ecart)*taille_case, "Haut : Flèche du haut", couleur = 'black', ancrage = 'center', police = 'Helvetica', taille = 12) 
        texte((largeur_fenetre-contour-largeur_boutons/2)*taille_case, (hauteur_fenetre-contour-11*ecart)*taille_case, "Bas : Flèche du bas", couleur = 'black', ancrage = 'center', police = 'Helvetica', taille = 12) 
        texte((largeur_fenetre-contour-largeur_boutons/2)*taille_case, (hauteur_fenetre-contour-10*ecart)*taille_case, "Droite : Flèche droite", couleur = 'black', ancrage = 'center', police = 'Helvetica', taille = 12)
        texte((largeur_fenetre-contour-largeur_boutons/2)*taille_case, (hauteur_fenetre-contour-9*ecart)*taille_case, "Gauche : Flèche gauche", couleur = 'black', ancrage = 'center', police = 'Helvetica', taille = 12)
        
        texte((largeur_fenetre-contour-largeur_boutons/2)*taille_case, (hauteur_fenetre-contour-7*ecart)*taille_case, "JOUEUR 2", couleur = 'black', ancrage = 'center', police = 'Helvetica', taille = 14)
        texte((largeur_fenetre-contour-largeur_boutons/2)*taille_case, (hauteur_fenetre-contour-(11/2)*ecart)*taille_case, "Score : " + str(score_2), couleur = 'black', ancrage = 'center', police = 'Helvetica', taille = 12)
        texte((largeur_fenetre-contour-largeur_boutons/2)*taille_case, (hauteur_fenetre-contour-(9/2)*ecart)*taille_case, "Haut : Touche 'Z'", couleur = 'black', ancrage = 'center', police = 'Helvetica', taille = 12) 
        texte((largeur_fenetre-contour-largeur_boutons/2)*taille_case, (hauteur_fenetre-contour-(7/2)*ecart)*taille_case, "Bas : Touche 'W'", couleur = 'black', ancrage = 'center', police = 'Helvetica', taille = 12) 
        texte((largeur_fenetre-contour-largeur_boutons/2)*taille_case, (hauteur_fenetre-contour-(5/2)*ecart)*taille_case, "Droite : Touche 'S'", couleur = 'black', ancrage = 'center', police = 'Helvetica', taille = 12)
        texte((largeur_fenetre-contour-largeur_boutons/2)*taille_case, (hauteur_fenetre-contour-(3/2)*ecart)*taille_case, "Gauche : Touche 'Q'", couleur = 'black', ancrage = 'center', police = 'Helvetica', taille = 12)
    
  
    
def affiche_mur(mur):
    """
    Prend en argument un couple de coordonées, mur.
    Affiche un mur.
    """

    ax, ay = case_vers_pixel(mur) 
    bx, by = case_vers_pixel((mur[0] + largeur_mur, mur[1] + hauteur_mur))
    
    rectangle(ax, ay, bx, by, couleur = 'black', remplissage = 'brown', epaisseur = 2) 
        
              

def generer_mur(serpent):
    """
    Prend en argument une liste de couple, serpent.
    Renvoie un couple de coordonnée correspondant a un mur généré de façon aléatoire.
    """
    
    mur = (randint(contour, contour+largeur_plateau-largeur_mur)-0.5, randint(contour, contour+hauteur_plateau-hauteur_mur)-0.5)
    
    while mur in serpent or mur in pomme :
        
        mur = (randint(contour, contour+largeur_plateau-largeur_mur)-0.5, randint(contour, contour+hauteur_plateau-hauteur_mur)-0.5)
        
    return mur
    
    
def generer_mur_2(serpent, serpent_2):
    
    mur = (randint(contour, contour+largeur_plateau-largeur_mur)-0.5, randint(contour, contour+hauteur_plateau-hauteur_mur)-0.5)
    
    while mur in serpent or mur in pomme or mur in serpent_2 :
        
        mur = (randint(contour, contour+largeur_plateau-largeur_mur)-0.5, randint(contour, contour+hauteur_plateau-hauteur_mur)-0.5)
        
    return mur


def affiche_pommes(pomme):
    
    x, y = case_vers_pixel(pomme) 
    
    cercle(x, y, taille_case/2, couleur = 'darkred', remplissage = 'red', epaisseur = 1) 
    
    rectangle(x - 2, y - taille_case * .4, x + 2, y - taille_case * .7, couleur = 'darkgreen', remplissage = 'green')
              

def generer_pomme(serpent):
    
    pomme = (randint(contour, contour+largeur_plateau-taille_serpent), randint(contour, contour+hauteur_plateau-taille_serpent)) 
    
    while pomme in serpent or (pomme[0] >= mur[0] and pomme[0] <= mur[0] + largeur_mur and pomme[1] >= mur[1] and pomme[1] <= mur[1] + hauteur_mur) :
        
        pomme = (randint(contour, contour+largeur_plateau-taille_serpent/2), randint(contour, contour+hauteur_plateau-taille_serpent/2))                
    
    return pomme
    
    
def generer_pomme_2(serpent, serpent_2):
    
    pomme = (randint(contour, contour+largeur_plateau-taille_serpent), randint(contour, contour+hauteur_plateau-taille_serpent)) 
    
    while pomme in serpent or (pomme[0] >= mur[0] and pomme[0] <= mur[0] + largeur_mur and pomme[1] >= mur[1] and pomme[1] <= mur[1] + hauteur_mur) or pomme in serpent_2:
        
        pomme = (randint(contour, contour+largeur_plateau-taille_serpent/2), randint(contour, contour+hauteur_plateau-taille_serpent/2))                
    
    return pomme
    
        
def pomme_manger(serpent, pomme, direction):

    if (pomme[0] >= serpent[0][0] + direction[0] - 0.5 and pomme[0] <= serpent[0][0] + direction[0] + 0.5) and (pomme[1] >= serpent[0][1] + direction[1] - 0.5 and pomme[1] <= serpent[0][1] + direction[1] + 0.5) : 
    
        serpent.append(None)
        
        pomme = None
        
    return serpent, pomme
    
    
def pomme_manger_2(serpent_2, pomme, direction_2):
    
    if pomme != None :
        
        if (pomme[0] >= serpent_2[0][0] + direction_2[0] - 0.5 and pomme[0] <= serpent_2[0][0] + direction_2[0] + 0.5) and (pomme[1] >= serpent_2[0][1] + direction_2[1] - 0.5 and pomme[1] <= serpent_2[0][1] + direction_2[1] + 0.5) : 
        
            serpent_2.append(False)
            
            pomme = False
            
    return serpent_2, pomme
    
        
def game_over(serpent):
    
    serpent_sans_tete = serpent.copy()
    
    serpent_sans_tete.pop([0][0])
    
    if (serpent[0][0], serpent[0][1]) in serpent_sans_tete:
        
        return True 
            
    if serpent[0][1] < contour or serpent[0][0] < contour or serpent[0][1] > hauteur_plateau + contour - taille_serpent or serpent[0][0] > largeur_plateau + contour - taille_serpent :
        
        return True
        
    if serpent[0][0] >= mur[0] and serpent[0][0] <= mur[0] + largeur_mur and serpent[0][1] >= mur[1] and serpent[0][1] <= mur[1] + hauteur_mur :
        
        return True 
            

def actualise_serpent(serpent, direction):
    
    serpent.insert(0,(serpent[0][0] + direction[0], serpent[0][1] + direction[1]))
    
    serpent.pop()
    
    return serpent


def affiche_serpent(serpent):
    
    for point in serpent:
        
        x, y = case_vers_pixel((point)) 

        cercle(x, y, taille_case/2 + 1, couleur='#2B7A00', remplissage='#53C217', epaisseur = 2)


def change_direction(direction, touche):
    
    if touche == 'Up':
        # flèche haut pressée
        return (0, -1)
        
    elif touche == 'Down':
        # flèche bas pressée
        return (0, 1)
        
    elif touche == 'Left':
        # flèche gauche pressée
        return (-1, 0)
        
    elif touche == 'Right':
        # flèche droite pressée
        return (1, 0)
        
    else:
        return direction
        
        
def game_over_2(serpent, serpent_2) :
    
    serpent_sans_tete = serpent.copy()
    
    serpent_sans_tete.pop([0][0])
    
    serpent_sans_tete_2 = serpent.copy()
    
    serpent_sans_tete_2.pop([0][0])
    
    if (serpent[0][0], serpent[0][1]) in serpent_sans_tete:
        
        return True, 1
            
    if serpent[0][1] < contour or serpent[0][0] < contour or serpent[0][1] > hauteur_plateau + contour - taille_serpent or serpent[0][0] > largeur_plateau + contour - taille_serpent :
        
        return True, 1
        
    if serpent[0][0] >= mur[0] and serpent[0][0] <= mur[0] + largeur_mur and serpent[0][1] >= mur[1] and serpent[0][1] <= mur[1] + hauteur_mur :
        
        return True, 1
        
    if (serpent[0][0], serpent[0][1]) in serpent_2 :
        
        return True, 1
        
    if (serpent_2[0][0], serpent_2[0][1]) in serpent_sans_tete_2 :
        
        return True, 2 
            
    if serpent_2[0][1] < contour or serpent_2[0][0] < contour or serpent_2[0][1] > hauteur_plateau + contour - taille_serpent or serpent_2[0][0] > largeur_plateau + contour - taille_serpent :
        
        return True, 2
        
    if serpent_2[0][0] >= mur[0] and serpent_2[0][0] <= mur[0] + largeur_mur and serpent_2[0][1] >= mur[1] and serpent_2[0][1] <= mur[1] + hauteur_mur :
        
        return True, 2
        
    if (serpent_2[0][0], serpent_2[0][1]) in serpent :
        
        return True, 2
        
    return False, None
            

def actualise_serpent_2(serpent, direction_2):
    
    serpent_2.insert(0,(serpent_2[0][0] + direction_2[0], serpent_2[0][1] + direction_2[1]))
    
    serpent_2.pop()
    
    return serpent_2


def affiche_serpent_2(serpent_2):
    
    for point in serpent_2 :
        
        x, y = case_vers_pixel((point)) 

        cercle(x, y, taille_case/2 + 1, couleur='#CE7F25', remplissage='#FF9A28', epaisseur = 2)


def change_direction_2(direction_2, touche):
    
    if touche == 'z':
        # flèche haut pressée
        return (0, -1)
        
    elif touche == 'w':
        # flèche bas pressée
        return (0, 1)
        
    elif touche == 'q':
        # flèche gauche pressée
        return (-1, 0)
        
    elif touche == 's':
        # flèche droite pressée
        return (1, 0)
        
    else:
        return direction_2
        
        
def menu():
    
    x = (largeur_fenetre/2)*taille_case
    
    # Fond du menu
    
    rectangle(0, 0, (largeur_fenetre)*taille_case-1, (hauteur_fenetre)*taille_case-1, couleur = 'black', remplissage = 'white', epaisseur = 3)    
    texte(x, (hauteur_fenetre/2-4*contour)*taille_case, "SNAKE", couleur="red", ancrage='center', police='Times New Roman', taille=26)
    ligne(10*contour*taille_case, (hauteur_fenetre/2-3*contour)*taille_case, (largeur_fenetre-10*contour)*taille_case, (hauteur_fenetre/2-3*contour)*taille_case, couleur="red", epaisseur=2)
    
    # Boutons
    
    rectangle((largeur_fenetre/2-contour/2-largeur_boutons)*taille_case, (hauteur_fenetre/2)*taille_case, (largeur_fenetre/2-contour/2)*taille_case, (hauteur_fenetre/2+2*hauteur_boutons)*taille_case, couleur="black", remplissage="#FAE038", epaisseur = 2)
    texte((largeur_fenetre/2-contour/2-largeur_boutons/2)*taille_case, (hauteur_fenetre/2+hauteur_boutons)*taille_case, "1 JOUEUR", couleur="black", ancrage='center', police='Times New Roman', taille=17)
    rectangle((largeur_fenetre/2+contour/2)*taille_case, (hauteur_fenetre/2)*taille_case, (largeur_fenetre/2+contour/2+largeur_boutons)*taille_case, (hauteur_fenetre/2+2*hauteur_boutons)*taille_case, couleur="black", remplissage="#FA7C38", epaisseur = 2)
    texte((largeur_fenetre/2+contour/2+largeur_boutons/2)*taille_case, (hauteur_fenetre/2+hauteur_boutons)*taille_case, "2 JOUEURS", couleur="black", ancrage='center', police='Times New Roman', taille=17)
    
    # Definition de la grille en fonction du clic
    
    x, y = attend_clic_gauche()
    
    nb_joueurs = None
    
    if y >= (hauteur_fenetre/2)*taille_case and y <= (hauteur_fenetre/2+2*hauteur_boutons)*taille_case :
        
        if x >= (largeur_fenetre/2-contour/2-largeur_boutons)*taille_case and x <= (largeur_fenetre/2-contour/2)*taille_case:
            
            nb_joueurs = 1
            
        if x >= (largeur_fenetre/2+contour/2)*taille_case and x <= (largeur_fenetre/2+contour/2+largeur_boutons)*taille_case :
            
            nb_joueurs = 2
            
    return nb_joueurs
        
        
        


# programme principal

# dimensions du jeu

taille_case = 10

largeur_fenetre = 79 
hauteur_fenetre = 56 
largeur_plateau = 50 
hauteur_plateau = 50 

largeur_mur = 4 
hauteur_mur = 2 

contour = 3 
ecart = contour/2 
largeur_boutons = 20
nb_boutons = 8
hauteur_boutons = (hauteur_plateau-(ecart*(nb_boutons-1)))/nb_boutons

taille_serpent = 2

# initialisation du jeu

mur = (randint(contour, contour+largeur_plateau-largeur_mur)-0.5, randint(contour, contour+hauteur_plateau-hauteur_mur)-0.5)

framerate = 10  # taux de rafraîchissement du jeu en images/s

cree_fenetre(largeur_fenetre * taille_case, hauteur_fenetre * taille_case)

valeur_menu = menu()

while valeur_menu == None:
    
    valeur_menu = menu()
    
nb_joueurs = valeur_menu

if nb_joueurs == 1 :

    serpent = [(contour + ecart, contour + ecart)] 
    
    score = 0
    direction = (0, 0)  # direction initiale du serpent
        
    pomme = generer_pomme(serpent)
    
    mur = generer_mur(serpent)
    
if nb_joueurs == 2 :
    
    serpent = [(contour + ecart, contour + ecart)]
    serpent_2 = [(contour + ecart, contour + 2*ecart)]
    
    score = 0
    direction = (0, 0)  # direction initiale du serpent
    
    score_2 = 0
    direction_2 = (0, 0)  # direction initiale du serpent

    pomme = generer_pomme_2(serpent, serpent_2)
    
    mur = generer_mur_2(serpent, serpent_2)

etat_fermeture = None

nouvelle_partie = None


# boucle principale

while True:
    
    ev = donne_ev()
    
    ty = type_ev(ev)
    
    if ty == None or ty == 'Touche' :
        
        # affichage des objets
        
        if nb_joueurs == 1 :
    
            serpent, pomme = pomme_manger(serpent, pomme, direction)
            
            serpent = actualise_serpent(serpent, direction)
            
        if nb_joueurs == 2 :
            
            serpent, pomme = pomme_manger(serpent, pomme, direction)
            serpent_2, pomme = pomme_manger_2(serpent_2, pomme, direction_2)
            
            serpent = actualise_serpent(serpent, direction)
            serpent_2 = actualise_serpent_2(serpent_2, direction_2)
        
        if pomme == None or pomme == False :
            
            if nb_joueurs == 1 :
            
                pomme = generer_pomme(serpent)
                
                score += 1
                
            if nb_joueurs == 2 :
                
                if pomme == None :
                    
                    score += 1
                    
                if pomme == False :
                    
                    score_2 += 1
                
                pomme = generer_pomme_2(serpent, serpent_2)
                    
            framerate += 2
            
        efface_tout()
        
        affiche_fond(nb_joueurs)
        
        affiche_pommes(pomme)  
        
        affiche_mur(mur)
        
        if nb_joueurs == 1 :
        
            affiche_serpent(serpent)
            
        if nb_joueurs == 2 :
            
            affiche_serpent(serpent)
            
            affiche_serpent_2(serpent_2)
            
        if nb_joueurs == 1 :   
         
            if game_over(serpent) == True :
                
                affiche_fond(nb_joueurs)
                
                texte((contour+largeur_plateau/2)*taille_case, (contour+hauteur_plateau/2)*taille_case, "Perdu !", couleur='gold', ancrage='center', police='Helvetica', taille=30)
                
                evenement = attend_clic_gauche()
                
                x, y = evenement[0], evenement[1]
                
                while x <= (2*contour+largeur_plateau)*taille_case or x >= (2*contour+largeur_plateau+largeur_boutons)*taille_case or y <= (contour+hauteur_boutons+ecart)*taille_case or y >= (contour+4*hauteur_boutons+3*ecart)*taille_case or (y >= (contour+2*hauteur_boutons+ecart)*taille_case and y <= (contour+3*hauteur_boutons+3*ecart)*taille_case) : 
                
                    evenement = attend_clic_gauche()
                    
                    x, y = evenement[0], evenement[1]
                    
                if x >= (2*contour+largeur_plateau)*taille_case and x <= (2*contour+largeur_plateau+largeur_boutons)*taille_case :
            
                    if y >= (contour+hauteur_boutons+ecart)*taille_case and y <= (contour+2*hauteur_boutons+ecart)*taille_case :
                        
                        nouvelle_partie = True
                        
                    elif y >= (contour+3*hauteur_boutons+3*ecart)*taille_case and y <= (contour+4*hauteur_boutons+3*ecart)*taille_case :
                        
                        etat_fermeture = True
                        
        if nb_joueurs == 2 :  
        
            etat_game_over = game_over_2(serpent, serpent_2)
         
            if etat_game_over[0] == True :
                
                affiche_fond(nb_joueurs)
                
                if etat_game_over[1] == 1 :
                
                    texte((contour+largeur_plateau/2)*taille_case, (contour+hauteur_plateau/2)*taille_case, "Joueur 1 vous avez perdu !", couleur='gold', ancrage='center', police='Helvetica', taille=25)
                    
                if etat_game_over[1] == 2 :
                
                    texte((contour+largeur_plateau/2)*taille_case, (contour+hauteur_plateau/2)*taille_case, "Joueur 2 vous avez perdu !", couleur='gold', ancrage='center', police='Helvetica', taille=25)
                
                evenement = attend_clic_gauche()
                
                x, y = evenement[0], evenement[1]
                
                while x <= (2*contour+largeur_plateau)*taille_case or x >= (2*contour+largeur_plateau+largeur_boutons)*taille_case or y <= (contour+hauteur_boutons+ecart)*taille_case or y >= (contour+4*hauteur_boutons+3*ecart)*taille_case or (y >= (contour+2*hauteur_boutons+ecart)*taille_case and y <= (contour+3*hauteur_boutons+3*ecart)*taille_case) : 
                
                    evenement = attend_clic_gauche()
                    
                    x, y = evenement[0], evenement[1]
                    
                if x >= (2*contour+largeur_plateau)*taille_case and x <= (2*contour+largeur_plateau+largeur_boutons)*taille_case :
            
                    if y >= (contour+hauteur_boutons+ecart)*taille_case and y <= (contour+2*hauteur_boutons+ecart)*taille_case :
                        
                        nouvelle_partie = True
                        
                    elif y >= (contour+3*hauteur_boutons+3*ecart)*taille_case and y <= (contour+4*hauteur_boutons+3*ecart)*taille_case :
                        
                        etat_fermeture = True
            
        mise_a_jour()
    
        # gestion des événements
        
        ev = donne_ev()
        
        ty = type_ev(ev)
        
        if ty == 'Touche':
            
            if nb_joueurs == 1 :
    
                direction = change_direction(direction, touche(ev))
                
            if nb_joueurs == 2 :
                
                direction = change_direction(direction, touche(ev))
                direction_2 = change_direction_2(direction_2, touche(ev))

        # attente avant rafraîchissement
        
        sleep(1/framerate)
            
    if ty == 'ClicGauche' or nouvelle_partie == True :
        
        if ty == 'ClicGauche' :
        
            x, y = abscisse(ev), ordonnee(ev)
            
        else :
            
            x, y = 0, 0
        
        if (x >= (2*contour+largeur_plateau)*taille_case and x <= (2*contour+largeur_plateau+largeur_boutons)*taille_case) or nouvelle_partie == True :
            
            if (y >= (contour+hauteur_boutons+ecart)*taille_case and y <= (contour+2*hauteur_boutons+ecart)*taille_case) or nouvelle_partie == True :
                
                nouvelle_partie = None
                
                valeur_menu = menu()
                
                while valeur_menu == None:
                    
                    valeur_menu = menu()
                    
                nb_joueurs = valeur_menu
                
                if nb_joueurs == 1 :
                
                    serpent = [(contour + ecart, contour + ecart)] 
                    
                    score = 0
                    direction = (0, 0)  # direction initiale du serpent
                        
                    pomme = generer_pomme(serpent)
                    
                    mur = generer_mur(serpent)
                    
                if nb_joueurs == 2 :
                    
                    serpent = [(contour + ecart, contour + ecart)]
                    serpent_2 = [(contour + ecart, contour + 2*ecart)]
                    
                    score = 0
                    direction = (0, 0)  # direction initiale du serpent
                    
                    score_2 = 0
                    direction_2 = (0, 0)  # direction initiale du serpent
                
                    pomme = generer_pomme_2(serpent, serpent_2)
                    
                    mur = generer_mur_2(serpent, serpent_2)
                
                etat_fermeture = None
                
                nouvelle_partie = None

                
            elif y >= (contour+2*hauteur_boutons+2*ecart)*taille_case and y <= (contour+3*hauteur_boutons+2*ecart)*taille_case :
                
                texte((contour+largeur_plateau/2)*taille_case, (contour+hauteur_plateau/2-ecart)*taille_case, "PAUSE", couleur='red', ancrage="center", police='Times New Roman', taille=30)
                texte((contour+largeur_plateau/2)*taille_case, (contour+hauteur_plateau/2+ecart)*taille_case, "(APPUYEZ POUR REPARTIR)", couleur='red', ancrage="center", police='Times New Roman', taille=27)
                
                attend_ev()
                
            elif y >= (contour+3*hauteur_boutons+3*ecart)*taille_case and y <= (contour+4*hauteur_boutons+3*ecart)*taille_case :
                
                etat_fermeture = True
                
                break
                
    if etat_fermeture == True :
        
        break
        

# fermeture et sortie

ferme_fenetre()