import pygame
import tkinter as tk
import mastermind_inversé
import interface

# Initialiser la  lecture de musique
pygame.mixer.init()
# Charger le fichier audio
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play()

# Définir les couleurs
noir = (0, 0, 0)
blanc = (255, 255, 255)
couleur = (39, 174, 173)
rouge = (255, 0, 0)


class Boutton:
    def __init__(self, text, pos):
        # Charger la police de caractères
        self.font = pygame.font.Font("style.ttf", 70)
        self.text = text
        self.pos = pos
        self.rect = pygame.Rect(pos, (150, 50))

    def draw(self, fenetre):
        # Dessiner le fond du bouton
        pygame.draw.rect(fenetre, blanc, self.rect)

        # bordure noire autour des bouttons
        pygame.draw.rect(fenetre, noir, self.rect, 2)  # Bordure d'épaisseur 2 pixels

        # texte
        surface_texte = self.font.render(self.text, True, noir)
        Dimmensions_texte = surface_texte.get_rect(center=self.rect.center)
        fenetre.blit(surface_texte, Dimmensions_texte)


def game():
    # Initialiser Pygame
    pygame.init()

    # Définir la taille de la fenêtre
    largeur, hauteur = 1000, 700
    fenetre = pygame.display.set_mode((largeur, hauteur))

    # police de caractères
    font = pygame.font.Font("KDA.ttf", 60)  # Police de caractères de taille 60

    # Mastermind
    surface_texte_M = font.render("Mastermind", True, rouge)

    # dimmensions
    Dimmensions_texte = surface_texte_M.get_rect()

    # Modifie la position du texte
    Dimmensions_texte.y = 40  # haut de la fenêtre
    Dimmensions_texte.x = (largeur - Dimmensions_texte.width) // 2  # Centré

    def calcule_position(bouttons, boutton_largeur, boutton_hauteur, Espacement):
        for i, boutton in enumerate(bouttons):
            if boutton.text == "Menu":
                boutton_pos = (675, 600)
                boutton.rect = pygame.Rect(boutton_pos, (300, 80))
            else:
                boutton_x = (largeur - boutton_largeur) // 2
                boutton_y = 200 + i * (boutton_hauteur + Espacement)
                boutton_pos = (boutton_x, boutton_y)
                boutton.rect = pygame.Rect(boutton_pos, (boutton_largeur, boutton_hauteur))

    def changement_musique(lamusique):
        pygame.mixer.music.stop()
        pygame.mixer.music.load(lamusique)
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play()

    def initialiser_fenetre():
        pygame.init()
        pygame.display.set_mode((largeur, hauteur))

    # Créer les boutons
    bouttons = [Boutton("Jouer", (0, 0)), Boutton("Credits", (0, 0)), Boutton("Quitter", (0, 0))]

    calcule_position(bouttons, 300, 75, 80)

    # Boucle principale
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Vérifier si l'utilisateur a cliqué sur un bouton
                for button in bouttons:
                    if button.rect.collidepoint(event.pos):
                        # Action effectuer lorsque le bouton est cliqué
                        if button.text == "Jouer":
                            initialiser_fenetre()
                            bouttons = [Boutton("Mastemind Normal", (0, 0)), Boutton("Mastermind IA", (0, 0)),
                                        Boutton("Menu", (825, 625))]
                            calcule_position(bouttons, 800, 75, 150)
                        elif button.text == "Mastemind Normal":
                            changement_musique(
                                "Puzzles 8 (1 Hour version) - Professor Layton vs. Phoenix Wright Ace Attorney (128 kbps).mp3")
                            interface.surface()
                        elif button.text == "Mastermind IA":

                            initialiser_fenetre()
                            bouttons = [Boutton("Mastermind petit QI", (0, 0)), Boutton("Mastermind moyen QI", (0, 0)),
                                        Boutton("Mastermind gros QI", (0, 0)), Boutton("Menu", (825, 625))]
                            calcule_position(bouttons, 600, 75, 80)
                        elif button.text == "Mastermind petit QI":
                            changement_musique("crab_rave.mp3")
                            mastermind_inversé.surface(0)
                        elif button.text == "Mastermind moyen QI":
                            changement_musique("Thank You for Everything.mp3")
                            mastermind_inversé.surface(1)
                        elif button.text == "Mastermind gros QI":
                            changement_musique("esprits-de-lumieres.mp3")
                            mastermind_inversé.surface((2))
                        elif button.text == "Credits":
                            # Ouvrir une nouvelle fenêtre pour afficher les crédits
                            credits_window = tk.Tk()
                            credits_window.title("Crédits")
                            credits_text = tk.Label(credits_window,
                                                    text="Concepteur :\nTheo Parent\nTheo Duterte--Richardot\nLoick Mornaux\nDroit de conception squirrel monkey corp",
                                                    font=("Arial", 16))
                            credits_text.pack()
                            credits_window.mainloop()
                        elif button.text == "Quitter":
                            running = False
                        elif button.text == "Menu":
                            game()

        # Dessiner la fenêtre
        fenetre.fill(couleur)
        fenetre.blit(surface_texte_M, Dimmensions_texte)  # afficher le texte
        for button in bouttons:
            button.draw(fenetre)  # actualiser l'affichage
        pygame.display.flip()
        pygame.display.set_caption("Mastermind de la squirrel monkey corp")
    # Quitter Pygame
    pygame.quit()


game()
