import pygame
import mm
import random
import subprocess

'''
Cette fonction crée une liste de 5 couleurs aléatoires
Sortie : l de type list
    '''


def le_secret(TabCouleur):
    l = []
    for i in range(5):
        l.append(mm.TabCouleur[random.randint(0, 7)])
    return l


'''
Cette fonction trouve les propositions bien placées en renvoyant un poin noir
Entrées : res , secret de type list
Sortie compteur de type int
    '''


def defNoir(res, secret):
    babouin_compteur = 0
    for x in range(len(res)):
        if res[x] == secret[x]:
            babouin_compteur += 1
    return babouin_compteur


'''
Cette fonction enlève les doubles d'un texte
Entrée : prop de type list
Sortie : liste de type list
    '''


def babouinDoublon(prop):
    babouin_liste = []
    for babouin in prop:
        if babouin not in babouin_liste:
            babouin_liste.append(babouin)
    return babouin_liste


'''
Cette fonction vérifie si des couleurs de la propotions sont mal placées
Entrées : prop,secret de type list
Sortie :compteur de type int
    '''


def Blanc(prop, secret):
    n = defNoir(prop, secret)
    babouin_compteur = 0
    prop = babouinDoublon(prop)

    for x in range(len(prop)):
        for y in range(len(secret)):
            if prop[x] == secret[y]:
                babouin_compteur += 1
    return babouin_compteur - n


'''programme pincipal'''


def surface():
    pygame.init()
    secret = le_secret(mm.TabCouleur)
    fenetre = pygame.display.set_mode([800, 800])
    fenetre.fill(mm.Blanc)
    mm.afficherPlateau(fenetre)
    mm.afficherChoixCouleur(fenetre)

    mm.afficherSecret(fenetre, [(mm.Marron) for x in range(5)])
    pygame.display.update()
    babouin = False
    while not babouin:

        for x in range(2, 18):
            if x > 16:
                myfont = pygame.font.SysFont("monospace", 40)

                lab = myfont.render("c'est terminé mec", 1, mm.Noir)
                fenetre.blit(lab, [250, 750])

                mm.afficherSecret(fenetre, secret)
                myfont = pygame.font.SysFont("monospace", 20)
                babouin_redemarrer = myfont.render("espace pour redémarrer", 1, mm.Noir)
                fenetre.blit(babouin_redemarrer, [75, 670])
                babouin_quitter = myfont.render("echap pour quitter", 1, mm.Noir)
                mm.afficherSecret(fenetre, secret)
                fenetre.blit(babouin_quitter, [75, 690])
                pygame.display.update()
                while not babouin:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                pygame.quit()
                                subprocess.run(["python", "interface_IA_normal.py"])
                            if event.key == pygame.K_SPACE:
                                surface()
                        if event.type == pygame.QUIT:
                            exit()

            mm.afficherChoixCouleur(fenetre)

            prop = mm.construireProposition(fenetre, x)

            a = Blanc(prop, secret)
            res = [a, defNoir(prop, secret)]

            mm.afficherResultat(fenetre, res, x)
            pygame.display.update()
            if res[1] == 5:
                myfont = pygame.font.SysFont("monospace", 40)
                kl = "c'est gagné en " + str(x - 1) + " tours"

                lab = myfont.render(kl, 1, mm.Noir)
                fenetre.blit(lab, [200, 750])

                myfont = pygame.font.SysFont("monospace", 20)
                babouin_redemarrer = myfont.render("espace pour redémarrer", 1, mm.Noir)
                fenetre.blit(babouin_redemarrer, [75, 670])
                babouin_quitter = myfont.render("echap pour quitter", 1, mm.Noir)
                mm.afficherSecret(fenetre, secret)
                fenetre.blit(babouin_quitter, [75, 690])
                pygame.display.update()
                while not babouin:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                pygame.quit()
                                subprocess.run(["python", "interface_IA_normal.py"])
                            if event.key == pygame.K_SPACE:
                                surface()
                        if event.type == pygame.QUIT:
                            exit()


if __name__ == "__main__":
    surface()
