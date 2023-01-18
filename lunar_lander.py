from bibliotheque import *
from time import sleep
from random import randint
import time
from math import *


def affichage_fond():
    """
    Affiche le jeu et les boutons joliment dans la fenêtre.
    """
    
    # Fond
    
    rectangle(0, 0, largeur_fenetre-1, hauteur_fenetre-1, couleur = 'black', remplissage = 'white')
    rectangle(contour, contour, contour+largeur_plateau, contour+hauteur_plateau, couleur = 'grey', remplissage = 'black', epaisseur = 3)
    
    # Boutons
    
    ax = 2*contour+largeur_plateau
    
    texte(ax+largeur_boutons/2, contour+hauteur_boutons/2, "BOUTONS :", ancrage = 'center', police = 'Times New Roman', taille = 16)
    ligne(ax+largeur_boutons/2-4*ecart, contour+hauteur_boutons/2+ecart, ax+largeur_boutons/2+4*ecart, contour+hauteur_boutons/2+ecart, epaisseur = 1)
    rectangle(ax, contour+hauteur_boutons+ecart, ax+largeur_boutons, contour+2*hauteur_boutons+ecart, couleur = 'black', remplissage = '#D8D8D8', epaisseur = 2)
    texte(ax+largeur_boutons/2, contour+ecart+hauteur_boutons*(3/2), "NOUVELLE PARTIE", ancrage = 'center', police = 'Times New Roman', taille = 16)
    rectangle(ax, contour+2*hauteur_boutons+2*ecart, ax+largeur_boutons, contour+3*hauteur_boutons+2*ecart, couleur = 'black', remplissage = '#BFBFBF', epaisseur = 2)
    texte(ax+largeur_boutons/2, contour+2*ecart+hauteur_boutons*(5/2), "PAUSE", ancrage = 'center', police = 'Times New Roman', taille = 16)
    rectangle(ax, contour+3*hauteur_boutons+3*ecart, ax+largeur_boutons, contour+4*hauteur_boutons+3*ecart, couleur = 'black', remplissage = '#7D7D7D', epaisseur = 2)
    texte(ax+largeur_boutons/2, contour+3*ecart+hauteur_boutons*(7/2), "QUITTER", ancrage='center', police = 'Times New Roman', taille = 16)
    


def affichage_sol(points): 
    """
    Prend en argument liste de couples (abscisse, ordonnee) de points, points.
    Affiche le sol (lunaire) du jeu et la zone d'atterrissage (en rouge).
    """
    
    polygone(points, couleur = '#CFCFCF', remplissage = '#CFCFCF', epaisseur = 1)
    
    ligne(zone_atterrissage[0], zone_atterrissage[2], zone_atterrissage[1], zone_atterrissage[2], couleur = 'red', epaisseur = 3)
    
    rectangle(contour, contour, contour+largeur_plateau, contour+hauteur_plateau, couleur = 'grey', epaisseur = 3)
    


def affichage_fusee(fusee, propulsion_active, carburant, temps):
    """
    Prend en argument une liste de listes fusee nous donnant les informations sur la fusée ([[position en x, position en y], [ancienne vitesse verticale, nouvelle vitesse verticale], [ancienne accélération verticale, nouvelle accélération verticale], [ancienne vitesse horizontale, nouvelle vitesse horizontale], [ancienne accélération horizontale, nouvelle accélération horizontale]]). propulsion_active est un booléen, carburant est une valeur représentant le niveau de carburant, temps est le temps de jeu.
    """
    
    t = time.time()-temps
    
    image(fusee[0][0], fusee[0][1], 'fusee.png', ancrage = 'center')

    #fleche(fusee[0][0], fusee[0][1], fusee[0][0]+fusee[3][1], fusee[1][1], couleur = 'red', epaisseur = 5)
    
    texte(contour+ecart, contour+ecart, "Carburant : " + str(carburant), couleur = 'white', ancrage = 'nw', police = 'Helvetica', taille = 10)
    
    texte(largeur_plateau-2*contour, contour+ecart, "Temps: " + str(round(t, 2)), couleur = 'white', ancrage = 'nw', police = 'Helvetica', taille = 10)
    
    texte(contour+ecart, contour+2*ecart, "Vitesse verticale : " + str(round(-fusee[1][1], 3)), couleur = 'white', ancrage = 'nw', police = 'Helvetica', taille = 10)
    
    texte(contour+ecart, contour+3*ecart, "Vitesse horizontale : " + str(abs(round(fusee[3][1], 3))), couleur = 'white', ancrage = 'nw', police = 'Helvetica', taille = 10)



def affichage(fusee, propulsion_active):
    """
    Prend en argument une liste de listes fusee nous donnant les informations sur la fusée ([[position en x, position en y], [ancienne vitesse verticale, nouvelle vitesse verticale], [ancienne accélération verticale, nouvelle accélération verticale], [ancienne vitesse horizontale, nouvelle vitesse horizontale], [ancienne accélération horizontale, nouvelle accélération horizontale]]) et propulsion_active est un booléen.
    Affiche le sol, le sol et la fusée.
    """
    
    efface_tout()
    
    affichage_fond()
    
    affichage_sol(points) 
    
    affichage_fusee(fusee, propulsion_active, carburant, temps)



def maj_p(ancienne_position, vitesse, delta_t):
    """
    Prend en argument une valeur ancienne_position et une valeur delta_t qui correspond à l'intervalle de temps entre l'ancien temps et le nouveau temps.
    Renvoie la nouvelle position verticale de la fusée;
    """
    
    return ancienne_position + vitesse*delta_t
    
    
    
def maj_p_horizontale(ancienne_position_horizontale, delta_t, new_vitesse_horizontale):
    """
    Prend en argument une valeur ancienne_position_horizontale, une valeur delta_t qui correspond à l'intervalle de temps entre l'ancien temps et le nouveau temps et une valeur new_vitesse_horizontale.
    Renvoie la nouvelle position horizontale de la fusée.
    """
    
    return ancienne_position_horizontale + new_vitesse_horizontale*delta_t
    
    
    
def maj_v(ancienne_vitesse, delta_t, new_acc):
    """
    Prend en argument une valeur ancienne_vitesse, une valeur delta_t qui correspond à l'intervalle de temps entre l'ancien temps et le nouveau temps et une valeur new_acc.
    Renvoie la nouvelle vitesse verticale de la fusée.
    """

    return ancienne_vitesse + (calcul_acceleration(propulsion_active, carburant, propulseur_g, propulseur_d,force_propulseur_secondaire)[0])*delta_t
    
    
    
def maj_v_horizontale(ancienne_vitesse_horizontale, delta_t, new_acc_horizontale):
    """
    Prend en argument  une valeur ancienn_vitesse_horizontale, une valeur delta_t qui correspond à l'intervalle de temps entre l'ancien temps et le nouveau temps et une valeur new_acc_horizontale.
    Renvoie la nouvelle vitesse horizontale de la fusée.
    """
    
    return ancienne_vitesse_horizontale + (calcul_acceleration(propulsion_active, carburant, propulseur_g, propulseur_d,force_propulseur_secondaire)[1])*delta_t
    
    
    
def calcul_acceleration(propulsion_active, carburant, propulseur_g, propulseur_d, force_propulseur_secondaire):
    """
    Prend en argument un booléen propulsion_active, une valeur carburant représentant le niveau de carburant de la fusée, 3 valeurs propulseur_g, propulseur_d et force_propulseur_secondaire représentant les forces de propulsions.
    Renvoie la nouvelle accélération verticale et horizontale.
    """
    
    if touche_pressee('Up') == True and carburant > 0:

        return gravite + force_propulseur, 0
        
    if touche_pressee('Left') == True and carburant > 0:
        
        return gravite + force_propulseur_secondaire, propulseur_g
        
    if touche_pressee('Right') == True and carburant > 0:
        
        return gravite + force_propulseur_secondaire, propulseur_d
        
    else :
        
        return  gravite, 0 
        
        
    
def maj_fusee(fusee, propulsion_active, temps_prec, new_vitesse, new_acc, new_vitesse_horizontale, new_acc_horizontale) :
    """
    Prend en argument une liste de listes fusee nous donnant les informations sur la fusée ([[position en x, position en y], [ancienne vitesse verticale, nouvelle vitesse verticale], [ancienne accélération verticale, nouvelle accélération verticale], [ancienne vitesse horizontale, nouvelle vitesse horizontale], [ancienne accélération horizontale, nouvelle accélération horizontale]]) et propulsion_active est un booléen. Une valeur temps_prec représentant le temps précédent, 2 valeurs new_vitesse et new_vitesse_horizontale représentant la vitesse verticale et horizontale de la fusée et 2 valeurs new_acc et new_acc_horizontale représentant l'accélération verticale et horizontale de la fusée. 
    Renvoie la liste de listes fusee composé de ses nouvelles valeurs et le nouveau temps.
    """
    
    fusee[1][0] = new_vitesse
    
    fusee[2][0] = new_acc
    
    fusee[3][0] = new_vitesse_horizontale
    
    fusee[4][0] = new_acc_horizontale
    
    ancienne_position = fusee[0][1]
    
    ancienne_position_horizontale = fusee[0][0]
    
    ancienne_vitesse = fusee[1][1]
    
    ancienne_acc = fusee[2][1]
    
    ancienne_vitesse_horizontale = fusee[3][1]
    
    anicenne_acc_horizontale = fusee[4][1]
    
    temps_actu = time.time()
    
    delta_t = temps_actu - temps_prec
    
    new_acc = calcul_acceleration(propulsion_active, carburant, propulseur_g, propulseur_d,force_propulseur_secondaire)[0]
    
    new_acc_horizontale = calcul_acceleration(propulsion_active, carburant, propulseur_g, propulseur_d,force_propulseur_secondaire)[1]
    
    new_vitesse = maj_v(ancienne_vitesse, delta_t, new_acc)
    
    new_vitesse_horizontale = maj_v_horizontale(ancienne_vitesse_horizontale, delta_t, new_acc_horizontale)
    
    new_position = maj_p(ancienne_position, new_vitesse, delta_t)
    
    new_position_horizontale = maj_p_horizontale(ancienne_position_horizontale, delta_t, new_vitesse_horizontale)
    
    fusee[0][1] = new_position
    
    fusee[0][0] = new_position_horizontale
    
    fusee[1][1] = new_vitesse
    
    fusee[2][1] = new_acc
    
    fusee[3][1] = new_vitesse_horizontale
    
    fusee[4][1] = new_acc_horizontale
    
    return fusee, temps_actu



def atterrissage_reussi(fusee):
    """
    Prend en argument une liste de listes fusee nous donnant les informations sur la fusée ([[position en x, position en y], [ancienne vitesse verticale, nouvelle vitesse verticale], [ancienne accélération verticale, nouvelle accélération verticale], [ancienne vitesse horizontale, nouvelle vitesse horizontale], [ancienne accélération horizontale, nouvelle accélération horizontale]]).
    Renvoie True si les conditions d'attérrissage sont respectées, c'est_à_dire si la vitesse verticale est inférieure ou égale à 10 et si la fusée est considérée comme au sol.
    """
    
    if fusee[1][1] <= 10 and au_sol(fusee) == True : 

        return True


def au_sol(fusee):
    """
    Prend en argument une liste de listes fusee nous donnant les informations sur la fusée ([[position en x, position en y], [ancienne vitesse verticale, nouvelle vitesse verticale], [ancienne accélération verticale, nouvelle accélération verticale], [ancienne vitesse horizontale, nouvelle vitesse horizontale], [ancienne accélération horizontale, nouvelle accélération horizontale]]).
    Renvoie True si la fusée est au sol dans la zone d'attérrissage.
    """
    
    if fusee[0][0] >= zone_atterrissage[0] and fusee[0][0] <= zone_atterrissage[1] and int(fusee[0][1])+dimension_fusee[1]/2 >= zone_atterrissage[2]-2  : 

        return True


def game_over(fusee):
    """
    Prend en argument une liste de listes fusee nous donnant les informations sur la fusée ([[position en x, position en y], [ancienne vitesse verticale, nouvelle vitesse verticale], [ancienne accélération verticale, nouvelle accélération verticale], [ancienne vitesse horizontale, nouvelle vitesse horizontale], [ancienne accélération horizontale, nouvelle accélération horizontale]]).
    Renvoie True si la fusée sort de la fenêtre ou si elle touche le sol.
    """
  
    if fusee[0][0] < dimension_fusee[0]+contour or fusee[0][1] < dimension_fusee[0]+contour or fusee[0][0] > contour+largeur_plateau-dimension_fusee[0] or int(fusee[0][1])+(dimension_fusee[1]/2) >= min(lst[int(fusee[0][0])-contour-10 : int(fusee[0][0])-contour+10]) :

        return True
        
        
def parametres(difficulte) :
    """
    Prend en argument une valeur difficulte qui correspond a l'écart en x entre chaque point du polygone (Plus la valeur est petite moins le sol sera plat).
    Renvoie une liste de couple de coordonnées pour le polygone formant le sol. De plus, elle renvoie une liste de valeurs, lst, la liste est de la taille de la fenêtre de jeu et elle est nécessaire pour former le sol du jeu. La position dans la liste correspond au coordonnée en x dans la fenêtre et sa valeur correspond au coordonnée en y dans la fenêtre. Renvoie aussi un triplet correspondant à la zone d'atterrissage (position en x du début de la zone, position en x de la fin de la zone, position en y de la zone)
    """
    
    x_point = contour
    y_point = hauteur_plateau
    
    distance_plateau = contour
    
    points = [(contour, contour+hauteur_plateau), (x_point, y_point)]

    lst = []
    
    zone_atterrissage = randint(0, int(largeur_plateau/difficulte)-1) 
    
    compteur = 0
    cpt = 0
    
    # Création de la liste de couple, points
    
    while distance_plateau < contour + largeur_plateau :
        
        x_point_precedent = x_point
        
        x_point = x_point + difficulte  #  Modifier pour changer la difficulté
        
        y_point_precedent = y_point
    
        if cpt == zone_atterrissage :
            
            y_point = y_point 
            
            zone_atterrissage = (x_point_precedent, x_point, y_point)
    
        else :
        
            y_point = randint(contour + hauteur_plateau - epaisseur_sol, hauteur_plateau + contour - 3)
        
        difference_hauteur = abs(y_point_precedent - y_point)
        
        augmentation = difference_hauteur / difficulte
        
        # Création de la liste des coordonnées de la surface du sol, lst
        
        while compteur < difficulte :
            
            if y_point_precedent >= y_point :
                
                y_point_precedent -= augmentation
                
            else :
                
                y_point_precedent += augmentation
            
            lst.append(y_point_precedent)
    
            compteur +=1
            
        compteur = 0
            
        points.append((x_point, y_point))
        
        distance_plateau += difficulte #  Modifier pour changer la difficulté
        
        cpt += 1
        
    y_fin = points[-1][1]
    
    points.pop(-1)
    
    points.append((contour + largeur_plateau, y_fin))
        
    if distance_plateau >= contour + largeur_plateau:
        
        y_point = contour + hauteur_plateau
        
        points.append((contour + largeur_plateau, y_point))
           
    return points, lst, zone_atterrissage
    
    
    
def menu():
    """
    Affiche le menu joliment.
    """
    
    x = largeur_fenetre/2
    
    # Fond du menu
    
    rectangle(0, 0, largeur_fenetre-1, hauteur_fenetre-1, couleur = 'black', remplissage = 'white', epaisseur = 3)    
    texte(x, 2*contour, "LUNAR LANDER", couleur = "red", ancrage = 'center', police = 'Times New Roman', taille = 26)
    ligne(12*contour, 3*contour, largeur_fenetre-12*contour, 3*contour, couleur = "red", epaisseur = 2)
    
    # Boutons

    texte(x, (11/2)*contour, "CHOISIR LE NIVEAU DE DIFFICULTÉ :", ancrage = 'center', police = 'Times New Roman', taille = 19)
    ligne(11*contour, (11/2)*contour+ecart, largeur_fenetre-11*contour, (11/2)*contour+ecart, couleur = 'black', epaisseur = 1)
    
    rectangle(x-largeur_boutons/2, 8*contour, x+largeur_boutons/2, 8*contour+hauteur_boutons, couleur = 'black', remplissage = '#CDCDCD', epaisseur = 2)
    texte(x, 8*contour+hauteur_boutons/2, "FACILE", ancrage = 'center', police = 'Times New Roman', taille = 17)
    rectangle(x-largeur_boutons/2, 8*contour+hauteur_boutons+ecart, x+largeur_boutons/2, 8*contour+2*hauteur_boutons+ecart, couleur = 'black', remplissage = '#AAAAAA', epaisseur = 2)
    texte(x, 8*contour+hauteur_boutons*(3/2)+ecart, "MOYENNE", ancrage = 'center', police = 'Times New Roman', taille = 17)
    rectangle(x-largeur_boutons/2, 8*contour+2*hauteur_boutons+2*ecart, x+largeur_boutons/2, 8*contour+3*hauteur_boutons+2*ecart, remplissage = '#898989', epaisseur = 2)
    texte(x, 8*contour+(5/2)*hauteur_boutons+2*ecart, "DIFFICILE", ancrage = 'center', police = 'Times New Roman', taille = 17)
    rectangle(x-largeur_boutons/2, 8*contour+3*hauteur_boutons+3*ecart, x+largeur_boutons/2, 8*contour+4*hauteur_boutons+3*ecart, couleur = 'black', remplissage = '#5F5F5F', epaisseur = 2)
    texte(x, 8*contour+(7/2)*hauteur_boutons+3*ecart, "TRÈS DIFFICILE", ancrage = 'center', police = 'Times New Roman', taille = 17)
    
    # Définition de la grille en fonction du clic
    
    x, y = attend_clic_gauche()
    
    difficulte = None
    
    if x >= largeur_fenetre/2-largeur_boutons/2 and x <= largeur_fenetre/2+largeur_boutons/2 :
        
        if y >= 8*contour and y <= 8*contour+hauteur_boutons :
            
            difficulte = 50
            
        elif y >= 8*contour+hauteur_boutons+ecart and y <= 8*contour+2*hauteur_boutons+ecart :
            
            difficulte = 40
                
        elif y >= 8*contour+2*hauteur_boutons+2*ecart and y <= 8*contour+3*hauteur_boutons+2*ecart :
            
            difficulte = 30
            
        elif y >= 8*contour+3*hauteur_boutons+3*ecart and y <= 8*contour+4*hauteur_boutons+3*ecart :
            
            difficulte = 20
                      
    return difficulte
            
            
    
    
# INITIALISATION


largeur_fenetre = 1090 
hauteur_fenetre = 600

largeur_plateau = 800
hauteur_plateau = 540
epaisseur_sol = 100

contour = 30
ecart = 15

largeur_boutons = 200
nb_boutons = 8
hauteur_boutons = (hauteur_plateau-(ecart*(nb_boutons-1)))/nb_boutons

dimension_fusee = (20,28)

temps = time.time()

framerate = 500

new_vitesse = 0
new_acc = 0
new_vitesse_horizontale = 0
new_acc_horizontale = 0

carburant = 1000

propulsion_active = False

force_propulseur = -4
force_propulseur_secondaire = -2

propulseur_d = 1
propulseur_g = -1

gravite = 1.62

fusee = [[contour+largeur_plateau/2, contour+ecart+(dimension_fusee[1]/2)], [0, 0], [0, 0], [0, 0], [0, 0]]

cree_fenetre(largeur_fenetre, hauteur_fenetre)

valeur_menu = menu()

while valeur_menu == None:
    
    valeur_menu = menu()
    
difficulte = valeur_menu

points, lst, zone_atterrissage = parametres(difficulte)

temps = time.time()


etat_fermeture = None

valeur = False

nouvelle_partie = None


# BOUCLE PRINCIPALE

      
while True:
    
    ev = donne_ev()
    
    ty = type_ev(ev)
    
    if ty == None or ty == 'Touche' :
        
        temps_prec = time.time()
        
        affichage(fusee, propulsion_active)
    
        if touche_pressee('Up') == True or touche_pressee('Left') == True or touche_pressee('Right') == True :
            
            carburant -= 1
            
            if carburant <= 0 :
                
                carburant = 0
                
        if atterrissage_reussi(fusee) == True :
            
            affichage_fond()
            
            texte(contour+largeur_plateau/2, contour+hauteur_plateau/2, "Gagné !", couleur = 'gold', ancrage = 'center', police = 'Helvetica', taille = 100)
    
            valeur = True
            
        elif game_over(fusee) == True :
            
            affichage_fond()
            
            if valeur == True :
                
                texte(contour+largeur_plateau/2, contour+hauteur_plateau/2, "Gagné !", couleur = 'gold', ancrage = 'center', police = 'Helvetica', taille = 100)
                
            else :
            
                texte(contour+largeur_plateau/2, contour+hauteur_plateau/2, "Perdu !", couleur = 'gold', ancrage = 'center', police = 'Helvetica', taille = 100)
            
            evenement = attend_clic_gauche()
            
            x, y = evenement[0], evenement[1]
            
            while x <= 2*contour+largeur_plateau or x >= 2*contour+largeur_plateau+largeur_boutons or y <= contour+hauteur_boutons+ecart or y >= contour+4*hauteur_boutons+3*ecart or (y >= contour+2*hauteur_boutons+ecart and y <= contour+3*hauteur_boutons+3*ecart) : 
            
                evenement = attend_clic_gauche()
                
                x, y = evenement[0], evenement[1]
                
            if x >= 2*contour+largeur_plateau and x <= 2*contour+largeur_plateau+largeur_boutons :
        
                if y >= contour+hauteur_boutons+ecart and y <= contour+2*hauteur_boutons+ecart :
                    
                    nouvelle_partie = True
                    
                elif y >= contour+3*hauteur_boutons+3*ecart and y <= contour+4*hauteur_boutons+3*ecart :
                    
                    etat_fermeture = True
            
        mise_a_jour()
        
        fusee, temps_prec = maj_fusee(fusee, propulsion_active, temps_prec, new_vitesse, new_acc, new_vitesse_horizontale, new_acc_horizontale)
        
        # Attente avant rafraîchissement
        
        sleep(1/framerate)
        
        ev = donne_ev()
        
        ty = type_ev(ev)
    
    if ty == 'ClicGauche' or nouvelle_partie == True :
        
        if ty == 'ClicGauche' :
        
            x, y = abscisse(ev), ordonnee(ev)
            
        else :
            
            x, y = 0, 0
        
        if (x >= 2*contour+largeur_plateau and x <= 2*contour+largeur_plateau+largeur_boutons) or nouvelle_partie == True :
            
            if (y >= contour+hauteur_boutons+ecart and y <= contour+2*hauteur_boutons+ecart) or nouvelle_partie == True :
                
                nouvelle_partie = None
                
                valeur_menu = menu()
                
                while valeur_menu == None:
                    
                    valeur_menu = menu()
                    
                difficulte = valeur_menu
                
                new_vitesse = 0
                new_acc = 0
                new_vitesse_horizontale = 0
                new_acc_horizontale = 0
                
                temps = time.time()
                
                carburant = 1000
                
                propulsion_active = False
                
                fusee = [[contour+largeur_plateau/2, contour+ecart+(dimension_fusee[1]/2)], [0, 0], [0, 0], [0, 0], [0, 0]]

                points, lst, zone_atterrissage = parametres(difficulte)
                
                temps_prec = time.time()
                
            elif y >= contour+2*hauteur_boutons+2*ecart and y <= contour+3*hauteur_boutons+2*ecart :
                
                ancien_temps = time.time()-temps

                texte(contour+largeur_plateau/2, contour+hauteur_plateau/2-ecart, "PAUSE", couleur = 'red', ancrage = "center", police = 'Times New Roman', taille = 30)
                texte(contour+largeur_plateau/2, contour+hauteur_plateau/2+ecart, "(APPUYEZ POUR REPARTIR)", couleur = 'red', ancrage = "center", police = 'Times New Roman', taille = 27)
                
                attend_ev()
                
                temps = time.time()-ancien_temps
                
            elif y >= contour+3*hauteur_boutons+3*ecart and y <= contour+4*hauteur_boutons+3*ecart :
                
                etat_fermeture = True
                
                break
                
    if etat_fermeture == True :
        
        break
     
# Fermeture et sortie

ferme_fenetre()


