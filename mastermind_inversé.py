import pygame
import mm2
import random
import time
def shuffle_list(lst):
    # Créer une copie de la liste
    shuffled_list = lst.copy()

    # Mélanger la copie de la liste de manière aléatoire
    for i in range(len(shuffled_list)):
        # Générer un index aléatoire
        random_index = random.randint(0, len(shuffled_list)-1)

        # Échanger les éléments à l'index actuel et à l'index aléatoire
        shuffled_list[i], shuffled_list[random_index] = shuffled_list[random_index], shuffled_list[i]

    # Renvoyer la copie de la liste mélangée aléatoirement
    return shuffled_list

TabCouleur = ['Noir', 'Blanc', 'Gris', 'Bleu', 'Rouge', 'Vert', 'Orange', 'Rose']
'''gigachadlist = []
dernièreliste = [0,0,0,0,0]
def toutes_les_listes():
    for x in TabCouleur:
        for y in TabCouleur:
            for i in TabCouleur:
                for j in TabCouleur:
                    for p in TabCouleur:
                        gigachadlist.append((x,y,i,j,p))
    return gigachadlist



print(toutes_les_listes())'''
# la liste qui contiendra toutes les couleurs supposées dans le code dans un ordre aléatoire
la_base = []


def le_secret(TabCouleur):
    l = []
    for i in range(5):
        l.append(mm2.TabCouleur[random.randint(0, 7)])
    return l


# on crée la liste qui servira de secret en tant que code dans le sens normal
def defNoir(res, secret):
    babouin_compteur = 0
    for x in range(len(res)):
        if res[x] == secret[x]:
            babouin_compteur += 1
    return babouin_compteur


# on compare la liste proposée au secret existant et on compte le nombre de pions identiques au meme endroit
def babouinDoublon(prop):
    babouin_liste = []
    for babouin in prop:
        if babouin not in babouin_liste:
            babouin_liste.append(babouin)
    return babouin_liste


# fonction qui retire les doublons d'une fonction
def Blanc(prop, secret):
    n = defNoir(prop, secret)
    babouin_compteur = 0
    prop = babouinDoublon(prop)
    for x in range(len(prop)):
        for y in range(len(secret)):
            if prop[x] == secret[y]:
                babouin_compteur += 1
    return babouin_compteur - n


# fonction qui compte le nombre de pions blancs entre un secret et une proposition
# on regarde le nombre de pions si ils sont bien/mal placés et on soustrait aux pions noirs et les doublons
# pour obtenir le nombre de pions blancs au total
def babouin_con():
    return (mm2.TabCouleur[random.randint(0, 7)])


# la fonction qui renvoie en proposition une liste aléatoire de couleurs
# babouin_con entièrement fonctionelle , ne surtout pas toucher
def babouin_big_cerveau(listecouleurs, couleursessai, precedents):
    # listecouleurs = la liste des couleurs qui on suppose composent notre code
    # couleursessai = les couleurs par paquet de 4 que nous avons déja essayé de faire
    # precedents = les combinaisons aléatoires de listecouleurs qui n'ont pas marché
    # cas ou on a notre liste pleine donc toutes les couleurs déterminées
    if len(listecouleurs) == 5:
        essai = shuffle_list(listecouleurs)
        while essai in precedents:
            essai = shuffle_list(listecouleurs)
        precedents.append(essai)
        print([essai,listecouleurs, couleursessai, precedents])
        return [essai,listecouleurs, couleursessai, precedents]
    else:
        babouin_try = []
        couleur = mm2.TabCouleur[random.randint(0, 7)]
        while couleur in couleursessai:
            couleur = mm2.TabCouleur[random.randint(0, 7)]
        couleursessai.append(couleur)
        for babouin_folie in range(5):
            babouin_try.append(couleur)
        print(babouin_try)
        return[babouin_try,listecouleurs,couleursessai,precedents]


'''
babouin_big_cerveau([(0, 0, 0),(0, 0, 0),(128,128,128),(128,128,128),(0,0,255)], [], [])


        #si la liste a déja été essayé
        if len(listecouleurs) == 5:
            babouin_try = listecouleurs
            while babouin_try in precedents:

                babouin_try= random.shuffle(listecouleurs)
        if babouin_try in précédents:
            return babouin_big_cerveau(listecouleurs,couleuressai,précédents)
        for x in range (len(couleursessai)):
            if couleursessai[x] in babouin_try:
                return babouin_big_cerveau(listecouleur,couleuressai,précédents)
        else:
            return babouin_try
        #si la couleur a déja été essayé
        if couleur[0] in couleursessai:
            return babouin_big_cerveau(listecouleurs,couleuressai,précédents)
        else:
            return babouin_try
            #faut rajouter la couleur dans couleuressai dans le prog principal
'''


def surface():
    pygame.init()
    secret = le_secret(mm2.TabCouleur)
    fenetre = pygame.display.set_mode([800, 800])
    fenetre.fill(mm2.Blanc)
    mm2.afficherPlateau(fenetre)
    mm2.afficherChoixCouleur(fenetre)
    pygame.display.update()
    myfont = pygame.font.SysFont("monospace", 20)
    babouin_constructeur = myfont.render("n = valider bien placé", 1, mm2.Noir)
    babouin_constructeur2 = myfont.render("b = valider mal placé", 1, mm2.Noir)
    babouin_validation = myfont.render("v pour valider les pions actuels", 1, mm2.Noir)
    fenetre.blit(babouin_constructeur, [5, 5])
    fenetre.blit(babouin_constructeur2, [5, 25])
    fenetre.blit(babouin_validation, [5, 40])
    pygame.display.update()
    secret = mm2.construireProposition(fenetre, 0.5)

    print(secret)
    intelligence = 1
    listecouleurs = []
    couleursessai = []
    précédents = []
    for x in range(2, 18):
        res = [0, 0]
        if x > 16:
            myfont = pygame.font.SysFont("monospace", 40)

            if intelligence == 0:
                lab = myfont.render("l'ia aléatoire a perdu ", 1, mm2.Noir)
            elif intelligence == 1:
                lab = myfont.render("l'ia intelligente a perdu", 1, mm2.Noir)
            fenetre.blit(lab, [150, 750])

            myfont = pygame.font.SysFont("monospace", 20)
            babouin_redemarrer = myfont.render("espace pour redémarrer", 1, mm2.Noir)
            fenetre.blit(babouin_redemarrer, [75, 670])
            babouin_quitter = myfont.render("echap pour quitter", 1, mm2.Noir)

            fenetre.blit(babouin_quitter, [75, 690])
            pygame.display.update()

            while not babouin:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            exit()
                        if event.key == pygame.K_SPACE:
                            surface()
                    if event.type == pygame.QUIT:
                        exit()

        if intelligence == 0:
            essai = [mm2.TabCouleur[random.randint(0, 7)] for x in range(5)]
            mm2.afficherCombinaison(fenetre, essai, x)
        elif intelligence == 1:
            # listecouleurs = liste des couleurs definies dans le secret
            # couleuressai = les couleurs précédentes essayées
            # précédents = les anciens essais
            print((listecouleurs, couleursessai, précédents))
            total = babouin_big_cerveau(listecouleurs, couleursessai, précédents)
            essai = total[0]
            listecouleurs = total[1]
            couleursessai = total[2]
            précédents = total[3]
            mm2.afficherCombinaison(fenetre,essai, x)
        elif intelligence == 3:
            None
        '''babouin_infini = True
        while babouin_infini == True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if res[0] + res[1] == 5:
                    babouin_infini = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_b:
                        res[0] += 1
                        mm2.afficherResultat(fenetre, res, x)
                        pygame.display.update()
                    if event.key == pygame.K_n:
                        res[1] += 1
                        mm2.afficherResultat(fenetre, res, x)
                        pygame.display.update()
                    if event.key == pygame.K_v:
                        babouin_infini = False'''
        a = Blanc(essai, secret)
        res = [a, defNoir(essai, secret)]
        mm2.afficherResultat(fenetre, res, x)
        pygame.display.update()
        if res[1] == 5:
            myfont = pygame.font.SysFont("monospace", 40)
            kl = "c'est gagné en " + str(x - 1) + " tours"

            lab = myfont.render(kl, 1, mm2.Noir)
            fenetre.blit(lab, [200, 750])
            myfont = pygame.font.SysFont("monospace", 20)
            babouin_redemarrer = myfont.render("espace pour redémarrer", 1, mm2.Noir)
            fenetre.blit(babouin_redemarrer, [75, 670])
            babouin_quitter = myfont.render("echap pour quitter", 1, mm2.Noir)
            fenetre.blit(babouin_quitter, [75, 690])
            pygame.display.update()
            babouin = False
            while not babouin:

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            exit()
                        if event.key == pygame.K_SPACE:
                            surface()
                    if event.type == pygame.QUIT:
                        exit()
        elif res[0] + res[1] >= 1 and len(listecouleurs)==5 :
            None
        elif res[0] + res[1] >= 1:
            for x in range(res[0] + res[1]):
                listecouleurs.append(essai[0])
            print(listecouleurs)


        pygame.display.update()
        babouin = False
        time.sleep(0.5)
surface()