import pygame
import mm2
import random
TabCouleur = ['Noir','Blanc','Gris','Bleu','Rouge','Vert','Orange','Rose']
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

def le_secret(TabCouleur):
    l=[]
    for i in range(5):
        l.append(mm2.TabCouleur[random.randint(0,7)])
    return l
#on crée la liste qui servira de secret en tant que code dans le sens normal
def defNoir(res,secret):
    babouin_compteur = 0
    for x in range (len(res)):
        if res[x] == secret[x]:
            babouin_compteur += 1
    return babouin_compteur
#on compare la liste proposée au secret existant et on compte le nombre de pions identiques au meme endroit
def babouinDoublon(prop):
    babouin_liste = []
    for babouin in prop:
        if babouin not in babouin_liste:
            babouin_liste.append(babouin)
    return babouin_liste
#fonction qui retire les doublons d'une fonction
def Blanc(prop,secret):
    n = defNoir(prop,secret)
    babouin_compteur = 0
    prop = babouinDoublon(prop)
    for x in range(len(prop)):
        for y in range(len(secret)):
            if prop[x] == secret[y]:
                babouin_compteur += 1
    return babouin_compteur-n

#fonction qui compte le nombre de pions blancs entre un secret et une proposition
#on regarde le nombre de pions si ils sont bien/mal placés et on soustrait aux pions noirs et les doublons
#pour obtenir le nombre de pions blancs au total
def babouin_con():
    return(mm2.TabCouleur[random.randint(0,7)])
#la fonction qui renvoie en proposition une liste aléatoire de couleurs
def babouin_big_cerveau(listecouleurs,couleursessai,précédents):
    #cas ou on a notre liste pleine donc toutes les couleurs déterminées
        babouin_try = [babouin_con()]
        for babouin_compteur in range (4):
            babouin_try.append(babouin_try[0])
        #si la liste a déja été essayé
        if len(listecouleurs) == 5:
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
def surface():
    pygame.init()
    secret = le_secret(mm2.TabCouleur)
    fenetre = pygame.display.set_mode([800,800])
    fenetre.fill(mm2.Blanc)
    mm2.afficherPlateau(fenetre)
    mm2.afficherChoixCouleur(fenetre)
    pygame.display.update()
    myfont = pygame.font.SysFont("monospace",20)
    babouin_constructeur = myfont.render("n = valider bien placé",1,mm2.Noir)
    babouin_constructeur2 = myfont.render ("b = valider mal placé",1,mm2.Noir)
    babouin_validation = myfont.render ("v pour valider les pions actuels",1,mm2.Noir)
    fenetre.blit(babouin_constructeur,[5,5])
    fenetre.blit(babouin_constructeur2,[5,25])
    fenetre.blit(babouin_validation,[5,40])
    pygame.display.update()
    secret = mm2.construireProposition(fenetre,0.5)
    
    print(secret)
    intelligence = 1
    listecouleurs = []
    couleursessai= []
    précédents = []
    for x in range(2,18):
        res = [0,0]
        if x >16:
                myfont = pygame.font.SysFont("monospace", 40)

                if intelligence == 0:
                    lab = myfont.render("l'ia aléatoire a perdu ",1,mm2.Noir)
                elif intelligence == 1:
                    lab = myfont.render("l'ia intelligente a perdu",1,mm2.Noir)
                fenetre.blit(lab,[150,750]) 
                
                
                myfont = pygame.font.SysFont("monospace", 20)
                babouin_redemarrer = myfont.render("espace pour redémarrer",1,mm2.Noir)
                fenetre.blit(babouin_redemarrer,[75,670])
                babouin_quitter = myfont.render("echap pour quitter",1,mm2.Noir)
                
                fenetre.blit(babouin_quitter,[75,690])
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
                    couleur = [mm2.TabCouleur[random.randint(0,7)] for x in range (5)]
                    
                    mm2.afficherCombinaison(fenetre,couleur,x)
        elif intelligence == 1:
            
            
            #listecouleurs = liste des couleurs definies dans le secret
            #couleuressai = les couleurs précédentes essayées
            #précédents = les anciens essais 
            
            
            
            prop = babouin_big_cerveau(listecouleurs,couleursessai,précédents)
            res == [Blanc(prop,secret),defNoir(prop,secret)]
            
                    
            mm2.afficherCombinaison(fenetre,prop,x)
            
                 
            
            
        babouin_infini = True
        while babouin_infini == True:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if res[0]+res[1] == 5:
                    babouin_infini = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_b:
                        res[0] +=1
                        mm2.afficherResultat(fenetre,res,x)
                        pygame.display.update()
                    if event.key == pygame.K_n:
                        res[1] +=1
                        mm2.afficherResultat(fenetre,res,x)
                        pygame.display.update()
                    if event.key == pygame.K_v:
                        babouin_infini = False
        
        if  res[0]+res[1]>=1:
                for x in range(res[0]+res[1]):
                    listecouleurs.append(prop[0])
                print(listecouleurs)
        if res[1] == 5:
                myfont = pygame.font.SysFont("monospace", 40)
                kl ="c'est gagné en "+str(x-1)+" tours"
                        
                lab = myfont.render(kl,1,mm2.Noir)
                fenetre.blit(lab,[200,750])
                myfont = pygame.font.SysFont("monospace", 20)
                babouin_redemarrer = myfont.render("espace pour redémarrer",1,mm2.Noir)
                fenetre.blit(babouin_redemarrer,[75,670])
                babouin_quitter = myfont.render("echap pour quitter",1,mm2.Noir)
                fenetre.blit(babouin_quitter,[75,690])
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
                

                
                
        
        pygame.display.update()
        babouin = False
    
surface()
                    
            
            
                
    
                





