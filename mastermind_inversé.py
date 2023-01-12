import subprocess
import pygame
import mm2
import random
import time

import copy


# ce code est la propriéte de la SquirrelMonkeyCorp© et a pour but de concrétiser un projet de cours
# pour le moindre problème veuillez nous contacter a l'adresse mail suivante: squirrelmonkeycorp@gmail.com votre demande sera prise en charge
# dans nos délais les plus brefs
# membres de la squirrelMonkey corp:
# président :Theo parent
# salariés:Theo Dutertre-Richardot ,Loïck Morneau
# si vous constatez la présence de babouins dans notre codes ceci est tout a fait normal et ne dois pas etre considéré comme une erreur ou
# une quelconque trace de folie mais comme une signature de notre entreprise pour prouver son unicité dans le monde de la programmaion
# tout les pseudo codes seront écrit en commentaires en dessous de leur fonction correspondante

# une fonction qui mélange une liste et qui la renvoie(utilisée dans un ancien algo , elle est maintenant inutile)
def shuffle_list(liste):
    babouin_liste = liste.copy()
    babouin_liste: list
    for i in range(len(babouin_liste)):
        random_index = random.randint(0, len(babouin_liste) - 1)
        babouin_liste[i], babouin_liste[random_index] = babouin_liste[random_index], babouin_liste[i]
    return babouin_liste


# complexité O(n) car on ne parcours que une seule fois chaque élément de la liste

'''
fonction "shuffle_list" (liste) :
     babouin_liste <- liste.copy()
     babouin_liste : list
     pour chaque i dans la longueur de (longueur (babouin_liste)):
        random_index <- chiffre aléatoire allant de  (0, longueur de (babouin_liste)-1)
        babouin_liste[i], babouin_liste[random_index] <- babouin_liste[random_index], babouin_liste[i]
    renvoyer babouin_liste
fin de la fonction
'''


# une fonction qui permet de générer toutes le combinaisons possibles de couleurs
def toutes_les_listes():
    gigachadlist: list
    gigachadlist = []
    # on fait 5boucles imbriquées pour a chaque fois modifier une combinaison élément par élément et ainsi obtenir toutes les possibilitées de couleurs
    for x in mm2.TabCouleur:
        for y in mm2.TabCouleur:
            for i in mm2.TabCouleur:
                for j in mm2.TabCouleur:
                    for p in mm2.TabCouleur:
                        gigachadlist.append((x, y, i, j, p))
    return gigachadlist


# la complexité de ce code est de O(n^5) parcequ'on pacequ'on parcours 5boucles imbriquées

'''
fonction"toutes les listes():
    gigachadlist <- []
    #on fait 5boucles imbriquées pour a chaque fois modifier une combinaison élément par élément et ainsi obtenir toutes les possibilitées de couleurs
    pour chaque x dans  mm2.TabCouleur:
        pour chaque y dans mm2.TabCouleur:
            pour chaque i dans mm2.TabCouleur:
                pour chaque j dans  mm2.TabCouleur:
                    pour chaque p dans mm2.TabCouleur:
                        ajouter dans gigachadlist((x,y,i,j,p))
    renvoyer gigachadlist
'''


# fonction qui sert a créer aléatoirement un secret (utilisée dans le mode winrate du mastermind)
def le_secret(TabCouleur):
    l = []
    l: list
    TabCouleur: list
    # on crée une boucle qui va faire apprendre a une liste un identifiant rvb aléatoire de la liste des couleurs disponibles au jeu
    for i in range(5):
        l.append(mm2.TabCouleur[random.randint(0, 7)])
    return l


# la complexité de ce code est 0(1) car on ne  fait que une boucle

# on crée la liste qui servira de secret en tant que code dans le sens normal
'''
fonction le_secret(TabCouleur):
    l <- []
    l : list
    TabCouleur : list
    #on crée une boucle qui va faire apprendre a une liste un identifiant rvb aléatoire de la liste des couleurs disponibles au jeu
    pour chaque i allant de 0 à 5:
        ajouter dans l (mm2.TabCouleur[chiffre aléatoire compris entre 0 et 7])
    renvoyer l
'''


# la fonction qui sert à compter le nombre de pions communs au bon emplacement entre l'essai et le secret
def defNoir(res, secret):
    babouin_compteur = 0
    babouin_compteur: int
    res: list
    secret: list
    for x in range(len(res)):
        if res[x] == secret[x]:
            babouin_compteur += 1
    return babouin_compteur


# complexité 0(n) car on ne passe que dans une boucle

'''
fonction defNoir(res,secret):
    babouin_compteur <- 0
    babouin_compteur : int
    res : list
    secret : list
    pour tout x allant de 0 à longueur de la liste res:
        si  res[x] équivaut à secret[x]:
            babouin_compteur augmente de 1
    renvoyer babouin_compteur
'''


# on compare la liste proposée au secret existant et on compte le nombre de pions identiques au meme endroit
# une fonction qui sert a retirer les doublons d'une liste pour ne pas obtenir de mauvais résultat lors du calcul de pions blanc/noirs
def babouinDoublon(prop):
    babouin_liste = []
    prop: list
    babouin_liste: list
    for babouin in prop:
        if babouin not in babouin_liste:
            babouin_liste.append(babouin)
    return babouin_liste


# complexité 0(n) car on ne parcours qu'une seule boucle for
'''
fonction babouinDoublon(prop):
    babouin_liste <- []
    pour chaque babouin dans prop:
        si babouin n'est pas dans babouin_liste:
            ajouter a babouin_liste(babouin)
    renvoyer babouin_liste
'''


# fonction qui compte le nombre de pions blancs entre un secret et une proposition
# on regarde le nombre de pions si ils sont bien/mal placés et on soustrait aux pions noirs et les doublons
# pour obtenir le nombre de pions blancs au total
def Blanc(prop, secret):
    n = defNoir(prop, secret)
    babouin_compteur = 0
    prop: list
    secret: list

    prop = babouinDoublon(prop)
    for x in range(len(prop)):
        for y in range(len(secret)):
            if prop[x] == secret[y]:
                babouin_compteur += 1
    return babouin_compteur - n


# la fonction blanc est de complexité O(n^2)car elle utilise deux boucles imbriquées

'''
fonction Blanc(prop, secret):
    n <- fonction defNoir(prop, secret)
    babouin_compteur <- 0
    prop <- babouinDoublon(prop)
    pour chaque x allant de 0 à longueur (prop):
        pour chaque y allant de 0 à (longueur de secret):
            si  prop[x] équivaut à secret[y]:
                babouin_compteur augmente de 1
    renvoyer babouin_compteur - n
'''


# fonction temporaire présente uniquement pour des test
def Blanc2(prop, secret):
    n = defNoir(prop, secret)
    babouin_compteur = 0
    prop = babouinDoublon(prop)
    for x in range(len(prop)):
        if prop[x] in secret:
            babouin_compteur += 1
    return babouin_compteur - n


# le premier niveau d'intelligence ,elle ne renvoie que des solutions aléatoires (taux de victoire ~0% et 1%)
def babouin_con():
    return (mm2.TabCouleur[random.randint(0, 7)])


# la complexité de la fonction babouin_con est de 0(1) car elle ne fait qu'une opération
'''
fonction babouin_con():
    renvoyer(mm2.tabCouleur[chiffre aléatoire compris entre 0 et 7])
'''


# la fonction qui renvoie en proposition une liste aléatoire de couleurs
# babouin_con entièrement fonctionelle , ne surtout pas toucher
def babouin_big_cerveau(listecouleurs, couleursessai, precedents):
    # listecouleurs = la liste des couleurs qui on suppose composent notre code
    # couleursessai = les couleurs par paquet de 4 que nous avons déja essayé de faire
    # precedents = les combinaisons aléatoires de listecouleurs qui n'ont pas marché
    # cas ou on a notre liste pleine donc toutes les couleurs déterminées
    essai: list
    precedents_dict: dict
    listecouleurs: list
    couleursessai: list
    precedents: list
    babouin_try: list
    couleur: tuple
    if len(listecouleurs) == 5:  # quand notre liste de couleurs présentes dans le code est pleine
        essai = random.sample(listecouleurs, 5)  # on crée une combinaison aléatoire de nos éléments de notre code
        precedents_dict = {tuple(combo): None for combo in
                           precedents}  # on génère un dictionnaire qui contiendra toutes les listes qu'on a testé
        while tuple(
                essai) in precedents_dict:  # tant que notre essai est présent dans precedents_dict on recrée des essais pour ne jamais les tester deux fois
            essai = random.sample(listecouleurs, 5)
        precedents.append(essai)
        return [essai, listecouleurs, couleursessai, precedents]
    else:
        babouin_try = []
        couleur = mm2.TabCouleur[random.randint(0, 7)]  # on génère une combinaison aléatoire à partir de mm2.tabcouleur
        while couleur in couleursessai:
            couleur = mm2.TabCouleur[random.randint(0,
                                                    7)]  # si on a déja essayé des couleurs on change jusqu'a avoir une couleur que l'on a pas encore essayé
        couleursessai.append(couleur)
        for babouin_folie in range(5):
            babouin_try.append(couleur)  # on génère une liste de 5fois la couleur que l'on a selectionné précedemment

        return [babouin_try, listecouleurs, couleursessai, precedents]


# la fonction babouin_big_cerveau est 0(n) car nous utilisons une seule boucle et non pas des boucles imbriquées
# de plus comme pour toutes les autres de complexité 0(n) elle dépend de la longueur de la liste avec laquelle elle intéragit
'''
def babouin_big_cerveau(listecouleurs, couleursessai, precedents):
    # listecouleurs <- la liste des couleurs qui on suppose composent notre code
    # couleursessai <- les couleurs par paquet de 4 que nous avons déja essayé de faire
    # precedents <- les combinaisons aléatoires de listecouleurs qui n'ont pas marché
    # cas ou on a notre liste pleine donc toutes les couleurs déterminées
    si la longueur de la liste des couleurs est égale à 5:
        essai <- combinaison aléatoire dans listecouleurs de longueur 5
        precedents_dict <- {tuple(combo): None for combo in precedents}
        tant que tuple(essai) est dans precedents_dict:
            essai <- combinaison aléatoire dans listecouleurs de longueur 5
        ajouter a precedents(essai)
        renvoyer [essai, listecouleurs, couleursessai, precedents]
    else:
        babouin_try <- []
        couleur <- mm2.TabCouleur[nombre aléatoire entre 0 et 7]
        tant qu'il y'a couleur dans couleursessai:
            couleur <- mm2.TabCouleur[nombre aléatoire entre 0 et 7]
        ajouter à couleursessai(essai)
        pour chaque babouin allant de 0 à 5
            ajouter a babouin_couleurs (couleur)
        afficher(babouin_try)
        renvoyer[babouin_try,listecouleurs,couleursessai,precedents]
'''


def babouin_filtre_final(alphachadlist, algo3liste, algo3res):
    betachadlist = []
    babouin = 0
    betachadlist: list
    alphachadlist: list
    babouin: int
    algo3res: list
    algo3liste: list
    while babouin < len(alphachadlist):
        if algo3res[-1] == [Blanc2(alphachadlist[babouin], algo3liste[-1]),
                            defNoir(alphachadlist[babouin], algo3liste[-1])]:
            betachadlist.append(alphachadlist[babouin])
            babouin += 1
        else:
            babouin += 1
    return betachadlist


'''
fonction babouin_filtre_final(alphachadlist,algo3liste,algo3res):
    betachadlist <- []
    babouin <- 0
    betachadlist:list
    alphachadlist:list
    babouin:int
    algo3res:list
    algo3liste:list
    while babouin < len(alphachadlist):
        si algo3res[-1] == [Blanc2(alphachadlist[babouin],algo3liste[-1]),defNoir(alphachadlist[babouin],algo3liste[-1])]:
            ajouter a betachadlist(alphachadlist[babouin])
            babouin +=1
        sinon:
            babouin += 1
    renvoyer betachadlist
'''


def babouin_fou(algo3liste, algo3res, gigachadlist):
    if len(algo3liste) == 0:
        essai = [babouin_con() for x in range(5)]
        return [essai, gigachadlist]
    else:
        gigachadlist = babouin_filtre_final(gigachadlist, algo3liste, algo3res)
        essai = gigachadlist[0]
        return [essai, gigachadlist]


'''
fonction babouin_fou(algo3liste,algo3res,gigachadlist):
    si longueur(algo3liste) == 0:
        essai <- [babouin_con() pour x allant de 0 à 5 ]
        return [essai,gigachadlist]
    sinon:
        gigachadlist <- babouin_filtre_final(gigachadlist,algo3liste,algo3res)
        essai <- gigachadlist[0]
        renvoyer[essai,gigachadlist]
'''


# cette fonction est une fonction de substitution car sa première version ne fonctionnait pas
def babouin_folie2(algo3codes, algo3res, gigachadlist, tour):
    if tour < 5:
        essai = [babouin_con() for x in range(5)]
        return [essai, gigachadlist]
    if tour == 5:
        gigachadlist2 = []
        for babouin_liste in range(len(algo3codes)):
            if algo3res[babouin_liste][1] == 1:
                for x in range(len(gigachadlist)):
                    if defNoir(algo3codes[babouin_liste], gigachadlist[x]) == 1:
                        if gigachadlist[x] not in gigachadlist2:
                            gigachadlist2.append(gigachadlist[x])
            elif algo3res[babouin_liste][1] == 2:
                for x in range(len(gigachadlist)):
                    if defNoir(algo3codes[babouin_liste], gigachadlist[x]) == 2:
                        if gigachadlist[x] not in gigachadlist2:
                            gigachadlist2.append(gigachadlist[x])
            elif algo3res[babouin_liste][1] == 3:
                for x in range(len(gigachadlist)):
                    if defNoir(algo3codes[babouin_liste], gigachadlist[x]) == 3:
                        if gigachadlist[x] not in gigachadlist2:
                            gigachadlist2.append(gigachadlist[x])
            elif algo3res[babouin_liste][1] == 4:
                for x in range(len(gigachadlist)):
                    if defNoir(algo3codes[babouin_liste], gigachadlist[x]) == 4:
                        if gigachadlist[x] not in gigachadlist2:
                            gigachadlist2.append(gigachadlist[x])

            if algo3res[babouin_liste][0] == 1:
                for x in range(len(gigachadlist)):
                    if defNoir(algo3codes[babouin_liste], gigachadlist[x]) == 1:
                        if gigachadlist[x] not in gigachadlist2:
                            gigachadlist2.append(gigachadlist[x])
            elif algo3res[babouin_liste][0] == 2:
                for x in range(len(gigachadlist)):
                    if defNoir(algo3codes[babouin_liste], gigachadlist[x]) == 2:
                        if gigachadlist[x] not in gigachadlist2:
                            gigachadlist2.append(gigachadlist[x])
            elif algo3res[babouin_liste][0] == 3:
                for x in range(len(gigachadlist)):
                    if defNoir(algo3codes[babouin_liste], gigachadlist[x]) == 3:
                        if gigachadlist[x] not in gigachadlist2:
                            gigachadlist2.append(gigachadlist[x])
            elif algo3res[babouin_liste][0] == 4:
                for x in range(len(gigachadlist)):
                    if defNoir(algo3codes[babouin_liste], gigachadlist[x]) == 4:
                        if gigachadlist[x] not in gigachadlist2:
                            gigachadlist2.append(gigachadlist[x])
    else:
        gigachadlist2 = []
        if algo3res[-1][1] == 1:
            for x in range(len(gigachadlist)):
                if defNoir(algo3codes[-1], gigachadlist[x]) == 1:
                    if gigachadlist[x] not in gigachadlist2:
                        gigachadlist2.append(gigachadlist[x])
        elif algo3res[-1][1] == 2:
            for x in range(len(gigachadlist)):
                if defNoir(algo3codes[-1], gigachadlist[x]) == 2:
                    if gigachadlist[x] not in gigachadlist2:
                        gigachadlist2.append(gigachadlist[x])
        elif algo3res[-1][1] == 3:
            for x in range(len(gigachadlist)):
                if defNoir(algo3codes[-1], gigachadlist[x]) == 3:
                    if gigachadlist[x] not in gigachadlist2:
                        gigachadlist2.append(gigachadlist[x])
        elif algo3res[-1][1] == 4:
            for x in range(len(gigachadlist)):
                if defNoir(algo3codes[-1], gigachadlist[x]) == 4:
                    if gigachadlist[x] not in gigachadlist2:
                        gigachadlist2.append(gigachadlist[x])

        if algo3res[-1][0] == 1:
            for x in range(len(gigachadlist)):
                if defNoir(algo3codes[-1], gigachadlist[x]) == 1:
                    if gigachadlist[x] not in gigachadlist2:
                        gigachadlist2.append(gigachadlist[x])
        elif algo3res[-1][0] == 2:
            for x in range(len(gigachadlist)):
                if defNoir(algo3codes[-1], gigachadlist[x]) == 2:
                    if gigachadlist[x] not in gigachadlist2:
                        gigachadlist2.append(gigachadlist[x])
        elif algo3res[-1][0] == 3:
            for x in range(len(gigachadlist)):
                if defNoir(algo3codes[-1], gigachadlist[x]) == 3:
                    if gigachadlist[x] not in gigachadlist2:
                        gigachadlist2.append(gigachadlist[x])
        elif algo3res[-1][0] == 4:
            for x in range(len(gigachadlist)):
                if defNoir(algo3codes[-1], gigachadlist[x]) == 4:
                    if gigachadlist[x] not in gigachadlist2:
                        gigachadlist2.append(gigachadlist[x])
    print(len(gigachadlist2))
    print("gigachadlist2:", gigachadlist2)
    oui = random.randint(0, len(gigachadlist2))
    essai = gigachadlist2[oui]
    return [essai, gigachadlist2]


# la version la plus évoluée de l'intelligence , son principe est de filtrer tout les codes possibles afin de n'en garder q'un seul
def babouin_folie(algo3codes, algo3res, gigachadlist, tour):
    algo3zero = []
    gigachadlist2 = []

    if tour < 5:
        essai = [babouin_con() for x in range(5)]
        return [essai, gigachadlist]
    if tour == 5:
        '''for x in range (len(algo3codes)):
            if algo3res[x] == (0,0):
                algo3zero.append(algo3codes[x])'''

        '''for oui in range(len(algo3zero)):
            for y in range(gigachadlist):
                if algo3zero[oui][0] not in gigachadlist[y] and algo3zero[oui][1] not in gigachadlist[y] and algo3zero[oui][2]  not in gigachadlist[y] and algo3zero[oui][3] not in gigachadlist[y] and algo3zero[oui][4] not in gigachadlist[y]:
                    gigachadlist2.append(gigachadlist[y])'''
        algo3codes2 = algo3codes
        algo3res2 = algo3res
        gigachadlist2 = gigachadlist
        # algo3codes2 = tout les codes qui n'ont pas un résultat à (0,0)
        # algo3res2 tout les résultats des codes d'au dessus
        gigachadlist3 = []
        for babouin_listes in range(len(algo3codes2)):
            if algo3res2[babouin_listes][1] == 1:
                print("on est passé dans le noir 1")
                for el in range(len(algo3codes2)):
                    pygame.display.update()
                    for babouin_1 in range(len(gigachadlist2)):
                        if algo3codes2[babouin_listes][el] == gigachadlist2[babouin_1][el]:
                            if gigachadlist2[babouin_1][el] not in gigachadlist3:
                                gigachadlist3.append((gigachadlist2[babouin_1]))
            elif algo3res2[babouin_listes][1] == 2:
                print("on est passé dans le noir 2")
                for babouin in range(4, 0, -1):
                    for baobab in range(babouin):
                        pygame.display.update()
                        for x in range(len(gigachadlist2)):
                            if gigachadlist2[x][babouin] == algo3codes2[babouin_listes][babouin] and gigachadlist2[x][
                                baobab] == algo3codes2[babouin_listes][baobab]:
                                if gigachadlist2[x] not in gigachadlist3:
                                    gigachadlist3.append(gigachadlist2[x])

            elif algo3res2[babouin_listes][1] == 3:
                print("on est passé dans le noir 3")
                liste_iterations = [6, 3, 1]
                for x in liste_iterations:
                    pygame.display.update()
                    for y in range(x):
                        if x == 6:
                            liste_iterations2 = [3, 2, 1]
                        elif x == 3:
                            liste_iterations2 = [2, 1]
                        elif x == 1:
                            liste_iterations2 = [1]
                        for z in liste_iterations2:
                            for i in range(z):
                                if z == 3:
                                    liste_iterations3 = [3, 2, 1]
                                elif z == 2:
                                    liste_iterations3 = [2, 1]
                                elif z == 1:
                                    liste_iterations3 = [1]
                                for oui in liste_iterations3:
                                    for m in range(gigachadlist2):
                                        if algo3codes2[babouin_listes][y] == gigachadlist2[m][y] and \
                                                algo3codes2[babouin_listes][i] == gigachadlist2[m][i] and \
                                                algo3codes2[babouin_listes][oui] == gigachadlist2[m][oui]:
                                            if gigachadlist2[m] not in gigachadlist3:
                                                gigachadlist3.append(gigachadlist2[m])
            elif algo3res2[babouin_listes][1] == 4:
                print("on est passé dans le noir 4")
                for x in range(len(gigachadlist2)):
                    pygame.display.update()
                    if algo3codes2[babouin_listes][0] == gigachadlist2[x][0] and algo3codes2[babouin_listes][1] == \
                            gigachadlist2[x][1] and algo3codes2[babouin_listes][2] == gigachadlist2[x][2] and \
                            algo3codes2[babouin_listes][3] == gigachadlist2[x][3]:
                        if gigachadlist2[x] not in gigachadlist3:
                            gigachadlist3.append(gigachadlist2[x])
                for x in range(len(gigachadlist2)):
                    pygame.display.update()
                    if algo3codes2[babouin_listes][1] == gigachadlist2[x][1] and algo3codes2[babouin_listes][2] == \
                            gigachadlist2[x][2] and algo3codes2[babouin_listes][3] == gigachadlist2[x][3] and \
                            algo3codes2[babouin_listes][4] == gigachadlist2[x][4]:
                        if gigachadlist2[x] not in gigachadlist3:
                            gigachadlist3.append(gigachadlist2[x])
                for x in range(len(gigachadlist2)):
                    pygame.display.update()
                    if algo3codes2[babouin_listes][0] == gigachadlist2[x][0] and algo3codes2[babouin_listes][2] == \
                            gigachadlist2[x][2] and algo3codes2[babouin_listes][3] == gigachadlist2[x][3] and \
                            algo3codes2[babouin_listes][4] == gigachadlist2[x][4]:
                        if gigachadlist2[x] not in gigachadlist3:
                            gigachadlist3.append(gigachadlist2[x])
                for x in range(len(gigachadlist2)):
                    pygame.display.update()
                    if algo3codes2[babouin_listes][0] == gigachadlist2[x][0] and algo3codes2[babouin_listes][1] == \
                            gigachadlist2[x][1] and algo3codes2[babouin_listes][3] == gigachadlist2[x][3] and \
                            algo3codes2[babouin_listes][4] == gigachadlist2[x][4]:
                        if gigachadlist2[x] not in gigachadlist3:
                            gigachadlist3.append(gigachadlist2[x])
                for x in range(len(gigachadlist2)):
                    pygame.display.update()
                    if algo3codes2[babouin_listes][0] == gigachadlist2[x][0] and algo3codes2[babouin_listes][1] == \
                            gigachadlist2[x][1] and algo3codes2[babouin_listes][2] == gigachadlist2[x][2] and \
                            algo3codes2[babouin_listes][4] == gigachadlist2[x][4]:
                        if gigachadlist2[x] not in gigachadlist3:
                            gigachadlist3.append(gigachadlist2[x])

            if algo3codes2[babouin_listes][0] == 1:
                print("on est passé dans le blanc 1")
                for el in range(len(algo3codes2)):
                    for babouin in range(len(gigachadlist2)):
                        pygame.display.update()
                        if algo3codes2[babouin_listes][el] in gigachadlist2[babouin][el]:
                            if gigachadlist2[babouin] not in gigachadlist3:
                                gigachadlist3.append(gigachadlist2[babouin])
            elif algo3res2[babouin_listes][0] == 2:
                print("on est passé dans le blanc 2")
                for babouin in range(4, 0, -1):
                    for baobab in range(babouin):
                        pygame.display.update()
                        for x in range(len(gigachadlist2)):
                            if gigachadlist2[x][babouin] in algo3codes2[babouin_listes] and gigachadlist2[x][baobab] in \
                                    algo3codes2[babouin_listes]:
                                if gigachadlist2[x] not in gigachadlist3:
                                    gigachadlist3.append(gigachadlist2[x])
            elif algo3res2[babouin_listes][0] == 3:
                print("on est passé dans le blanc 3")
                for babouin in range(4, 0, -1):
                    for baobab in range(babouin):
                        pygame.display.update()
                        for oui in range(baobab):
                            for x in range(len(gigachadlist2)):
                                if algo3codes2[babouin_listes][babouin] in gigachadlist2[x] and \
                                        algo3codes2[babouin_listes][baobab] in gigachadlist2[x] and \
                                        algo3codes2[babouin_listes][oui] in gigachadlist2[x]:
                                    if not gigachadlist2[x] in gigachadlist3:
                                        gigachadlist3.append(gigachadlist2)
    elif tour == 6:
        algo3codes2 = algo3codes
        algo3res2 = algo3res
        gigachadlist2 = gigachadlist
        gigachadlist3 = []
        oui = random.randint(0, len(gigachadlist))
        essai = gigachadlist[oui]
        gigachadlist.pop(oui)
        return [essai, gigachadlist]

    else:
        algo3codes2 = algo3codes
        algo3res2 = algo3res
        gigachadlist2 = gigachadlist
        gigachadlist3 = []
        if algo3res2[-1][1] == 1:
            print("on est passé dans le noir 1")
            for el in range(len(algo3codes2)):
                for babouin_1 in range(len(gigachadlist2)):
                    if algo3codes2[-1][el] == gigachadlist2[babouin_1][el]:
                        if gigachadlist2[babouin_1][el] not in gigachadlist3:
                            gigachadlist3.append((gigachadlist2[babouin_1]))
        elif algo3res2[-1][1] == 2:
            print("on est passé dans le noir 2")
            for babouin in range(4, 0, -1):
                for baobab in range(babouin):
                    for x in range(len(gigachadlist2)):
                        if gigachadlist2[x][babouin] == algo3codes2[-1][babouin] and gigachadlist2[x][baobab] == \
                                algo3codes2[-1][baobab]:
                            if gigachadlist2[x] not in gigachadlist3:
                                gigachadlist3.append(gigachadlist2[x])

        elif algo3res2[-1][1] == 3:
            print("on est passé dans le noir 3")
            liste_iterations = [6, 3, 1]
            for x in liste_iterations:
                for y in range(x):
                    if x == 6:
                        liste_iterations2 = [3, 2, 1]
                    elif x == 3:
                        liste_iterations2 = [2, 1]
                    elif x == 1:
                        liste_iterations2 = [1]
                    for z in liste_iterations2:
                        for i in range(z):
                            if z == 3:
                                liste_iterations3 = [3, 2, 1]
                            elif z == 2:
                                liste_iterations3 = [2, 1]
                            elif z == 1:
                                liste_iterations3 = [1]
                            for oui in liste_iterations3:
                                for m in range(gigachadlist2):
                                    if algo3codes2[-1][y] == gigachadlist2[m][y] and \
                                            algo3codes2[-1][i] == gigachadlist2[m][i] and \
                                            algo3codes2[-1][oui] == gigachadlist2[m][oui]:
                                        if gigachadlist2[m] not in gigachadlist3:
                                            gigachadlist3.append(gigachadlist2[m])
        elif algo3res2[-1][1] == 4:
            print("on est passé dans le noir 4")
            for x in range(len(gigachadlist2)):
                if algo3codes2[-1][0] == gigachadlist2[x][0] and algo3codes2[-1][1] == \
                        gigachadlist2[x][1] and algo3codes2[-1][2] == gigachadlist2[x][2] and \
                        algo3codes2[-1][3] == gigachadlist2[x][3]:
                    if gigachadlist2[x] not in gigachadlist3:
                        gigachadlist3.append(gigachadlist2[x])
            for x in range(len(gigachadlist2)):
                if algo3codes2[-1][1] == gigachadlist2[x][1] and algo3codes2[-1][2] == \
                        gigachadlist2[x][2] and algo3codes2[-1][3] == gigachadlist2[x][3] and \
                        algo3codes2[-1][4] == gigachadlist2[x][4]:
                    if gigachadlist2[x] not in gigachadlist3:
                        gigachadlist3.append(gigachadlist2[x])
            for x in range(len(gigachadlist2)):
                if algo3codes2[-1][0] == gigachadlist2[x][0] and algo3codes2[-1][2] == \
                        gigachadlist2[x][2] and algo3codes2[-1][3] == gigachadlist2[x][3] and \
                        algo3codes2[-1][4] == gigachadlist2[x][4]:
                    if gigachadlist2[x] not in gigachadlist3:
                        gigachadlist3.append(gigachadlist2[x])
            for x in range(len(gigachadlist2)):
                if algo3codes2[-1][0] == gigachadlist2[x][0] and algo3codes2[-1][1] == \
                        gigachadlist2[x][1] and algo3codes2[-1][3] == gigachadlist2[x][3] and \
                        algo3codes2[-1][4] == gigachadlist2[x][4]:
                    if gigachadlist2[x] not in gigachadlist3:
                        gigachadlist3.append(gigachadlist2[x])
            for x in range(len(gigachadlist2)):
                if algo3codes2[-1][0] == gigachadlist2[x][0] and algo3codes2[-1][1] == \
                        gigachadlist2[x][1] and algo3codes2[-1][2] == gigachadlist2[x][2] and \
                        algo3codes2[-1][4] == gigachadlist2[x][4]:
                    if gigachadlist2[x] not in gigachadlist3:
                        gigachadlist3.append(gigachadlist2[x])

        if algo3codes2[-1][0] == 1:
            print("on est passé dans le blanc 1")
            for el in range(len(algo3codes2)):
                for babouin in range(len(gigachadlist2)):
                    if algo3codes2[-1][el] in gigachadlist2[babouin][el]:
                        if gigachadlist2[babouin] not in gigachadlist3:
                            gigachadlist3.append(gigachadlist2[babouin])
        elif algo3res2[-1][0] == 2:
            print("on est passé dans le blanc 2")
            for babouin in range(4, 0, -1):
                for baobab in range(babouin):
                    for x in range(len(gigachadlist2)):
                        if gigachadlist2[x][babouin] in algo3codes2[-1] and gigachadlist2[x][baobab] in \
                                algo3codes2[-1]:
                            if gigachadlist2[x] not in gigachadlist3:
                                gigachadlist3.append(gigachadlist2[x])
        elif algo3res2[-1][0] == 3:
            print("on est passé dans le blanc 3")
            for babouin in range(4, 0, -1):
                for baobab in range(babouin):
                    for oui in range(baobab):
                        for x in range(len(gigachadlist2)):
                            if algo3codes2[-1][babouin] in gigachadlist2[x] and algo3codes2[-1][baobab] in \
                                    gigachadlist2[x] and algo3codes2[-1][oui] in gigachadlist2[x]:
                                if not gigachadlist2[x] in gigachadlist3:
                                    gigachadlist3.append(gigachadlist2)
    print(algo3codes2)
    print(algo3res2)
    print("longueur de gigachadlist2:", len(gigachadlist2))
    print("longueur de gigachadlist3:", len(gigachadlist3))
    jesaisplus = random.randint(0, len(gigachadlist3))
    essai = gigachadlist3[jesaisplus]
    return [essai, gigachadlist3]


# une fonction qui permet de faire plusieurs choses , en premier temps elle va appeller en boucle secret avec un certain nombre d'itérations pour pouvoir collecter des
# informations sur les victoires et les defaites de l'ia passé en paramètre, on utilise également un compteur por déterminer combien de temps nos itérations ont été faites
# en second temps la fonction crée/ouvre un fichier nommé test(numéro de l'ia) puis ajoute toutes les informations nécéssaires a un test , nottament la date de la réalisation
# le numéro de l'ia ,mais aussi le nombre d'itérations faites et le pourcentage de victoire de l'ia
def winrate(intelligence, iterations):
    intelligence: int
    iterations: int
    start = time.perf_counter()
    if intelligence != 1 and intelligence != 2 and intelligence != 0:  # on vérifie si l'ia rentrée n'est pas une ia incorrecte
        return None
    résultats = 0

    for x in range(
            iterations):  # on additionne tout les résultats de notre ia pour povoir calculer le pourcentage de victoire
        résultats = résultats + surface(intelligence, 1, le_secret(mm2.TabCouleur))
    print("nombe de victoires de l'ia en %", intelligence, ":", (
                résultats / iterations) * 100)  # on print le pourcentage de victoire de notre ia sur le nombre d'itérations données
    end = time.perf_counter()
    print("temps d'exécution : " + str(end - start))  # on affiche le temps d'exécution de nos itérations
    nom_fichier = ("tests" + str(intelligence))  # on détermine selon le numéro de l'ia un fichier a créer

    # Ouvrir le fichier en mode écriture
    with open(nom_fichier + ".txt",
              "a") as f:  # on ouvre en mode ajout notre fichier qui correspond a notre numéro d'ia
        # Écrire du texte dans le fichier
        f.write("test ia numéro " + str(intelligence) + "\n")  # on écrit dans le fichier les lignes
        now = time.localtime()
        date_heure = time.strftime("%Y-%m-%d %H:%M:%S",
                                   now)  # on récupère nos données concernant l'heure de la fin du test
        f.write("test réalisé à " + str(date_heure) + "avec " + str(
            iterations) + " itérations\n")  # on écrit dans le fichier correspondant la date du test et le nombre d'itérations de l'ia
        f.write("pourcentage de victoire de l'ia :" + str(
            (résultats / iterations) * 100) + "\n")  # on écrit le pourcentage de victoire de l'ia
        f.write("\n")
    return résultats


# la complexité de cette fonction est de 0(n*itérations) car nous allons effectuer "itérations" fois les calculs
'''
fonction winrate(intelligence,iterations):
    start <- time.perf_counter()
    if intelligence != 1 and  intelligence !=2 and intelligence != 0:#on vérifie si l'ia rentrée n'est pas une ia incorrecte
        return None
    résultats <- 0

    pour chaque x allant de 0 à itérations
        résultats = résultats + fonction surface(intelligence,1,le_secret(mm2.TabCouleur))
    afficher("nombe de victoires de l'ia en %", intelligence, ":", (résultats/iterations)*100)
    end <- time.perf_counter()
    afficher("temps d'exécution : "+str(end - start))
    nom_fichier <- ("tests"+str(intelligence)) 
    # Ouvrir le fichier en mode écriture
    avec comme fichier ouvert(nom_fichier+".txt", "a") en tant que f
        f.écrire("test ia numéro " + str(intelligence)+"\n")#on écrit dans le fichier les lignes
        now <- time.localtime()
        date_heure = time.strftime("%Y-%m-%d %H:%M:%S", now) #on récupère nos données concernant l'heure de la fin du test
        f.écrire("test réalisé à " + str(date_heure) +"avec "+str(iterations)+" itérations\n")#on écrit dans le fichier correspondant la date du test et le nombre d'itérations de l'ia
        f.écrire("pourcentage de victoire de l'ia :" + str((résultats/iterations)*100)+"\n") 
        f.écrire("\n")
    renvoyer résultats
'''


# une fonction qui fait une moyenne d'une liste
def moyenne(winrates):
    total = 0
    total: int
    winrates: list
    for x in range(len(winrates)):
        total += winrates[x]
    res = total / len(winrates)

    return (res)


# la complexité de la fonction moyenne est 0(n) car nous ne passons que dans une seule boucle
'''
fonction moyenne(winrates):
    pour chaque x allant de 0 à longueur de (winrates)
        total <- total+winrates[x]
    res <- total/longueur(winrates)
    afficher res 
    renvoyer res
'''


# une fonction qui va nous permettre de récupérer toutes les données d'un des fichiers des ia pour pouvoir récupérer toutes leurs informations
# concernant le pourcentage de victoire de l'ia concernée
def recuperation(intelligence):
    intelligence: int
    nomfichier = ("tests" + str(
        intelligence) + ".txt")  # on récupère en str le nom du fichier en utilisant la variable intelligence
    with open(nomfichier, "r") as f:  # on ouvre le fichier en mode read
        lines = f.readlines()  # on lit toutes les lignes du texte
    winrates = []
    for line in lines:
        if line.startswith(
                "pourcentage de victoire de l'ia :"):  # on récupère toutes les listes qui commencent par la phrase "pourcentage de victoire de l'ia :
            parts = line.split(" ")  # on sépare toutes les informations du texte
            winrate = parts[
                -1]  # on récupère la fin du texte splitté , dans notre cas on aura quelquechose sous cette forme ":(taux de victoire)\n"
            # Convertir le taux de victoire en un nombre flottant
            winrate = winrate.replace(":",
                                      "")  # on utilise replace pour enlever les ":" et les "\n" par des caractères vides
            winrate = winrate.replace("\n", "")  # on peut donc convertir ce qui nous reste en float
            winrate = float(winrate)
            winrates.append(
                winrate)  # on ajoute le winrate a une liste de plusieurs winrates dont on va faire une moyenne juste après

    oui = moyenne(winrates)

    print("Moyenne des taux de victoires :" + str(
        oui))  # on affiche  la moyenne des taux de victoire calculés dans la fonction d'au dessus


# complexitée 0(n) car on ne fait qu'une boucle qui parcours un fichier de la même manière qu'une liste

'''
fonction (intelligence):
    nomfichier <- ("tests"+str(intelligence)+".txt") 

    with open(nomfichier, "r") as f:#on ouvre le fichier en mode read
        lines <- f.readlines() #on lit toutes les lignes du texte
    winrates <- []
    for pour chaque ligne dans lignes:
        if ligne commence par("pourcentage de victoire de l'ia :"):
            parts <- line.split(" ")
            winrate <- parts[-1] 
            winrate <- winrate.replace(":", "")
            winrate <- winrate.replace("\n","")
            winrate <- float(winrate)
            winrates.append(winrate) #on ajoute le winrate a une liste de plusieurs winrates dont on va faire une moyenne juste après

    oui <- moyenne(winrates)


    afficher("Moyenne des taux de victoires :" + str(oui))
'''


# la fonction principale de tout le code , elle sert a gérer une partie tour par tour
def surface(intelligence=1, modetest=0, babouin_secret=0, essai_max=18):
    intelligence: int
    modetest: int
    pygame.init()
    secret = le_secret(mm2.TabCouleur)
    fenetre = pygame.display.set_mode([800, 800])
    fenetre.fill(mm2.Blanc)
    mm2.afficherPlateau(fenetre)
    mm2.afficherChoixCouleur(fenetre)
    pygame.display.update()

    if modetest == 0:
        secret = mm2.construireProposition(fenetre, 0.5)
    elif modetest == 1:
        secret = le_secret(mm2.TabCouleur)
        mm2.afficherSecret(fenetre, secret)

    listecouleurs = []
    couleursessai = []
    précédents = []
    algo3list = []
    marque = 0
    algo3codes = []
    algo3res = []
    if intelligence == 2:
        gigachadlist = toutes_les_listes()

    for x in range(2, essai_max):
        res = [0, 0]
        if x > essai_max - 2:

            myfont = pygame.font.SysFont("monospace", 40)

            if intelligence == 0:
                lab = myfont.render("l'ia aléatoire a perdu ", 1, mm2.Noir)
            elif intelligence == 1:
                lab = myfont.render("l'ia intelligente a perdu", 1, mm2.Noir)

            elif intelligence == 2:
                lab = myfont.render("l'ia folle a perdu", 1, mm2.Noir)
            fenetre.blit(lab, [150, 750])

            myfont = pygame.font.SysFont("monospace", 20)
            babouin_redemarrer = myfont.render("espace pour redémarrer", 1, mm2.Noir)
            fenetre.blit(babouin_redemarrer, [75, 670])
            babouin_quitter = myfont.render("echap pour quitter", 1, mm2.Noir)

            fenetre.blit(babouin_quitter, [75, 690])
            pygame.display.update()
            if modetest == 1:
                return 0
            while not babouin:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            pygame.quit()
                            subprocess.run(["python", "interface_IA_normal.py"])
                        if event.key == pygame.K_SPACE:
                            surface(intelligence)
                    if event.type == pygame.QUIT:
                        exit()

        elif intelligence == 0:
            essai = [mm2.TabCouleur[random.randint(0, 7)] for x in range(5)]
            mm2.afficherCombinaison(fenetre, essai, x)
        elif intelligence == 1:
            # listecouleurs = liste des couleurs definies dans le secret
            # couleuressai = les couleurs précédentes essayées
            # précédents = les anciens essais

            total = babouin_big_cerveau(listecouleurs, couleursessai, précédents)
            essai = total[0]
            listecouleurs = total[1]
            couleursessai = total[2]
            précédents = total[3]
            mm2.afficherCombinaison(fenetre, essai, x)

        elif intelligence == 2:
            total = babouin_fou(algo3list, algo3res, gigachadlist)
            essai = total[0]
            gigachadlist = total[1]
            algo3list.append(essai)
        mm2.afficherCombinaison(fenetre, essai, x)
        if intelligence == 1:
            a = Blanc(essai, secret)
        else:
            a = Blanc2(essai, secret)
        res = [a, defNoir(essai, secret)]
        mm2.afficherResultat(fenetre, res, x)
        pygame.display.update()
        algo3res.append(res)
        if res[1] == 5:

            myfont = pygame.font.SysFont("monospace", 40)
            kl = "c'est gagné en " + str(x - 1) + " tours"
            if essai_max != 18:
                return x - 2
            lab = myfont.render(kl, 1, mm2.Noir)
            fenetre.blit(lab, [200, 750])
            myfont = pygame.font.SysFont("monospace", 20)
            babouin_redemarrer = myfont.render("espace pour redémarrer", 1, mm2.Noir)
            fenetre.blit(babouin_redemarrer, [75, 670])
            babouin_quitter = myfont.render("echap pour quitter", 1, mm2.Noir)
            fenetre.blit(babouin_quitter, [75, 690])
            pygame.display.update()
            babouin = False
            if modetest == 1:
                return 1
            while not babouin:

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            pygame.quit()
                            subprocess.run(["python", "interface_IA_normal.py"])
                        if event.key == pygame.K_SPACE:
                            exit()
                    if event.type == pygame.QUIT:
                        exit()
        elif res[0] + res[1] >= 1 and len(listecouleurs) == 5:
            None
        elif res[0] + res[1] >= 1:
            for x in range(res[0] + res[1]):
                listecouleurs.append(essai[0])

        if modetest == 0:
            time.sleep(0.3)
        pygame.display.update()
        babouin = False


# dans sa version la plus basique la fonction surface effectuera 0(n) calculs avec son algorithme aléatoire , dans sa version la plus complexe elle
# est de complexité 0(n^4) car elle utilise

'''
fonction surface(intelligence=1, modetest=0, babouin_secret=0):
    pygame.init()
    secret <- le_secret(mm2.TabCouleur)
    fenetre <- pygame.display.set_mode([800, 800])
    fenetre.fill(mm2.Blanc)
    mm2.afficherPlateau(fenetre)
    mm2.afficherChoixCouleur(fenetre)
    pygame.display.update()

    if modetest == 0:
        secret <- mm2.construireProposition(fenetre, 0.5)
    elif modetest == 1:
        secret <- le_secret(mm2.TabCouleur)
        mm2.afficherSecret(fenetre, secret)

    listecouleurs <- []
    couleursessai <- []
    précédents <- []
    algo_3list <- []
    marque <- 0
    algo3codes <- []
    algo3res <- []
    gigachadlist <- fonction toutes_les_listes()

    pour chaque x allant de (2, 18):
        res <- [0, 0]
        si x > 16:

            myfont <- pygame.font.SysFont("monospace", 40)

            si intelligence == 0:
                lab <- myfont.render("l'ia aléatoire a perdu ", 1, mm2.Noir)
            sinon si  intelligence == 1:
                lab <- myfont.render("l'ia intelligente a perdu", 1, mm2.Noir)

            sinon si  intelligence == 2:
                lab <- myfont.render("l'ia folle a perdu", 1, mm2.Noir)
            fenetre.blit(lab, [150, 750])

            myfont <- pygame.font.SysFont("monospace", 20)
            babouin_redemarrer <- myfont.render("espace pour redémarrer", 1, mm2.Noir)
            fenetre.blit(babouin_redemarrer, [75, 670])
            babouin_quitter <- myfont.render("echap pour quitter", 1, mm2.Noir)

            fenetre.blit(babouin_quitter, [75, 690])
            pygame.display.update()
            si modetest == 1:
                return 0
            tanque que babouin est Faux:
                pour chaque event dans pygame.event.get():
                    si event.type == pygame.KEYDOWN:
                        si event.key == pygame.K_ESCAPE:
                            exit()
                        si event.key == pygame.K_SPACE:
                            surface(intelligence)
                    if event.type == pygame.QUIT:
                        exit()

        sinon si  intelligence == 0:
            essai <- [mm2.TabCouleur[random.randint(0, 7)] pour chaque x allant de 0 à 5]
            mm2.afficherCombinaison(fenetre, essai, x)
        sinon si intelligence == 1:
            # listecouleurs <- liste des couleurs definies dans le secret
            # couleuressai <- les couleurs précédentes essayées
            # précédents <- les anciens essais

            total <- babouin_big_cerveau(listecouleurs, couleursessai, précédents)
            essai <- total[0]
            listecouleurs <-total[1]
            couleursessai <- total[2]
            précédents <- total[3]
            mm2.afficherCombinaison(fenetre, essai, x)
        
        sinon si  intelligence == 2:
            total <- babouin_folie(algo3codes, algo3res, gigachadlist, x)
            essai <- total[0]
            gigachadlist = total[1]
            ajouter a algo3codes(essai)
            afficher(essai)

        mm2.afficherCombinaison(fenetre, essai, x)

        a <- Blanc(essai, secret)
        res <- [a, defNoir(essai, secret)]
        mm2.afficherResultat(fenetre, res, x)
        pygame.display.update()
        ajouter à algo3res(res)
        si res[1] == 5:

            myfont = pygame.font.SysFont("monospace", 40)
            kl <- "c'est gagné en " + str(x - 1) + " tours"

            lab <- myfont.render(kl, 1, mm2.Noir)
            fenetre.blit(lab, [200, 750])
            myfont <- pygame.font.SysFont("monospace", 20)
            babouin_redemarrer <- myfont.render("espace pour redémarrer", 1, mm2.Noir)
            fenetre.blit(babouin_redemarrer, [75, 670])
            babouin_quitter <- myfont.render("echap pour quitter", 1, mm2.Noir)
            fenetre.blit(babouin_quitter, [75, 690])
            pygame.display.update()
            babouin <- False
            si == 1:
                renvoyer 1
            tant que babouin est faux :

                pour chaque  event in pygame.event.get():
                    si event.type == pygame.KEYDOWN:
                        si event.key == pygame.K_ESCAPE:
                            exit()
                        si event.key == pygame.K_SPACE:
                            surface(intelligence)
                    si event.type == pygame.QUIT:
                        exit()
        sinon si  res[0] + res[1] >= 1 and len(listecouleurs) == 5:
            None
        sinon si  res[0] + res[1] >= 1:
            pour chaque x allant de 0 à (res[0] + res[1]):
                listecouleurs.append(essai[0])

        si modetest == 0:
            time.sleep(0.3)
        pygame.display.update()
        babouin = False
'''


# fonction qui sert a déterminer combien d'itérations en moyenne une ia a besoin pour trouver la solution , tout les
# résultats sont stockés dans les fichiers  iterations_max(numéro de l'ia)
def iterations_max(intelligence, itérations=100):
    nombre_essais = 0
    temps_total = 0
    nombre_essais: int
    temps_total: int
    intelligence: int
    nom_fichier: str
    start_time: float
    end_time: float
    temps_total: float
    for x in range(
            itérations):  # on fait faire a l'ia un nombre de partie très important de manière à savoir en combien de coups l'ia pourrais gagner
        start_time = time.time()  # on commence un timer qu'on termine 2lignes plus tard pour povoir calculer le temps que met la fonction à trouver le secret
        nombre_essais += surface(intelligence, 1, 0, 1000000000000)
        end_time = time.time()
        temps_total += end_time - start_time
    print("nombre d'essais en moyenne pour que l'ia ", intelligence, "gagne", nombre_essais / x)
    print("temps moyen pour que l'ia gagne", temps_total / x)
    nom_fichier = ("iterations_max" + str(intelligence))  # on détermine le nom du fichier selon le numéro de l'ia
    with open(nom_fichier + ".txt",
              "a") as f:  # on ouvre en mode ajout notre fichier qui correspond a notre numéro d'ia
        # Écrire du texte dans le fichier
        f.write("test ia numéro " + str(intelligence) + "\n")  # on écrit dans le fichier les lignes
        now = time.localtime()
        date_heure = time.strftime("%Y-%m-%d %H:%M:%S",
                                   now)  # on récupère nos données concernant l'heure de la fin du test
        f.write("test réalisé à " + str(
            date_heure))  # on écrit dans le fichier correspondant la date du test et le nombre d'itérations de l'ia
        f.write("\n")
        f.write("moyenne d'essais de l'ia pour gagner :" + str(
            nombre_essais / x) + "\n")  # on écrit le nombre d'essais nécéssaires à l'ia
        f.write("temps moyen pour que l'ia gagne:" + str(
            temps_total / x))  # on écrit le temps moyen de l'ia pour gagner une partie
        f.write("\n")
        f.write("\n")


'''
fonction iterations_max(intelligence):
    nombre_essais =0
    temps_total = 0
    nombre_essais : int
    temps_total :int 
    intelligence :int
    nom_fichier :str
    start_time : float
    end_time :float 
    temps_total :float
    pour chaque x allant de 0 à 100:
        start_time <- time.time()
        nombre_essais += fonction surface(intelligence ,1,0,1000000000000)
        end_time <- time.time()
        temps_total += end_time-start_time
    afficher("nombre d'essais en moyenne pour que l'ia ",intelligence,"gagne",nombre_essais/x)
    afficher("temps moyen pour que l'ia gagne",temps_total/x)
    nom_fichier <- ("iterations_max" + str(intelligence))
    with open(nom_fichier + ".txt","a") as f:  # on ouvre en mode ajout notre fichier qui correspond a notre numéro d'ia
        # Écrire du texte dans le fichier
        f.ecrire("test ia numéro " + str(intelligence) + "\n")  # on écrit dans le fichier les lignes
        now <- time.localtime()
        date_heure <- time.strftime("%Y-%m-%d %H:%M:%S",now)  # on récupère nos données concernant l'heure de la fin du test
        f.ecrire("test réalisé à " + str(date_heure))  # on écrit dans le fichier correspondant la date du test et le nombre d'itérations de l'ia
        f.ecrire("\n")
        f.ecrire("moyenne d'essais de l'ia pour gagner :" + str(nombre_essais/x) + "\n")  # on écrit le pourcentage de victoire de l'ia
        f.ecrire("temps moyen pour que l'ia gagne:"+str(temps_total/x))
        f.ecrire("\n")
        f.ecrire("\n")
'''


# une fonction qui permet de récupérer toutes les données d'une ia mise en entrée puis qui renvoie ses statistiques concernant le nombre
# d'itérations dont elle a besoin en moyenne pour réussir une partie et ses statistiques en moyenne pour résoudre une partie de mastermind
def recuperation_iterations(intelligence):
    nom_fichier: str
    nombre_essaistotal: list
    temps_total: list
    line: str
    lines: list
    temps: float
    moyenne_temps: float
    moyenne_essais: float

    nom_fichier = ("iterations_max" + str(
        intelligence))  # on détermine le nom du fichier selon le numéro de l'ia correspondante
    nombre_essaistotal = []
    temps_total = []
    with open(nom_fichier + ".txt",
              "r") as f:  # on ouvre le fichier en mode read car on a juste besoin de lire les informations
        lines = f.readlines()
    for line in lines:  # on fait une boucle pour visiter le fichier ligne par ligne
        if line.startswith(
                "moyenne d'essais de l'ia pour gagner :"):  # si notre ligne commence par la condition on respecte le if
            parts = line.split(" ")
            nombre_essais = parts[-1]

            nombre_essais = nombre_essais.replace(":", "")
            nombre_essais = nombre_essais.replace("\n",
                                                  "")  # on sépare les informations puis on remplace les éléments qui sont inutiles
            nombre_essais = float(nombre_essais)  # on repasse notre taux de str à float
            nombre_essaistotal.append(nombre_essais)
    for line in lines:
        if line.startswith("temps moyen pour que l'ia gagne:"):
            parts = line.split(" ")
            temps = parts[-1]
            temps = temps.replace(":", "")
            temps = temps.replace("\n", "")
            temps = temps.replace("gagne", "")  # meme principe que le if du dessus
            temps = float(temps)
            temps_total.append(temps)
    moyenne_temps = moyenne(temps_total)
    moyenne_essais = moyenne(nombre_essaistotal)
    print("moyenne du nombre d'essais nécéssaires pour que l'ia ", intelligence, "gagne:", moyenne_essais)
    print("moyenne du temps de nécéssaire pour que l'ia ", intelligence, "gagne ", moyenne_temps)


'''
fonction recuperation_iterations(intelligence):
    nom_fichier <- ("iterations_max" + str(intelligence))
    nombre_essaistotal <- []
    temps_total <- []
    with open(nom_fichier + ".txt", "r") as f:
        lines <- f.readlines()
    pour chaque line dans lignes:
        si line.commence avec("moyenne d'essais de l'ia pour gagner :"):
            parts <- line.split(" ")  
            nombre_essais <- parts[-1] 
           
            nombre_essais <- nombre_essais.replace(":", "")  
            nombre_essais <- nombre_essais.replace("\n", "") 
            nombre_essais <- float(nombre_essais)
            nombre_essaistotal.append(nombre_essais)
    for line in lines:
        if line.startswith("temps moyen pour que l'ia gagne:"):
            parts <- line.split(" ")  
            temps <- parts[-1]  
            # Convertir le taux de victoire en un nombre flottant
            temps <- temps.replace(":", "")  
            temps <- temps.replace("\n", "")  
            temps <- temps.replace("gagne","")
            temps <- float(temps)
            temps_total.append(temps)
    moyenne_temps <- moyenne(temps_total)
    moyenne_essais <- moyenne(nombre_essaistotal)
    afficher("moyenne du nombre d'essais nécéssaires pour que l'ia ",intelligence,"gagne:",moyenne_essais)
    afficher("moyenne du temps de nécéssaire pour que l'ia ",intelligence,"gagne ",moyenne_temps)
'''

recuperation_iterations(0)
