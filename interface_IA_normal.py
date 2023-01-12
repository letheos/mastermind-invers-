import pygame
import pygame.freetype
import tkinter as tk

# Initialiser Pygame et le module de lecture de musique
pygame.init()
pygame.mixer.init()

# Charger le fichier audio dans votre programme
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play()

# Définir la taille de la fenêtre
largeur, hauteur = 1000, 700
fenetre = pygame.display.set_mode((largeur, hauteur))

# Définir les couleurs
noir = (0, 0, 0)
blanc = (255, 255, 255)
couleur = (39, 174, 173)
rouge  = (255, 0, 0)

# Créer la police de caractères
font = pygame.font.Font("KDA.ttf", 60)  # Police de caractères de taille 36

# Créer la surface de texte contenant le mot "Mastermind"
surface_texte_M = font.render("Mastermind", True, rouge)

# Obtenir les dimensions de la surface de texte
Dimmensions_texte = surface_texte_M.get_rect()

# Modifier la position de la surface de texte pour qu'elle soit tout en haut et centrée horizontalement de la fenêtre
Dimmensions_texte.y = 40  # Tout en haut de la fenêtre
Dimmensions_texte.x = (largeur - Dimmensions_texte.width) // 2  # Centré horizontalement

class Button:
    def __init__(self, text, pos):
        # Charger la police de caractères
        self.font = pygame.font.Font("style.ttf", 70)
        self.text = text
        self.pos = pos
        self.rect = pygame.Rect(pos, (150, 50))

    def draw(self, fenetre):
        # Dessiner le fond du bouton
        pygame.draw.rect(fenetre, blanc, self.rect)

        # Dessiner la bordure noire autour du bouton
        pygame.draw.rect(fenetre, noir, self.rect, 2)  # Bordure d'épaisseur 2 pixels

        # Dessiner le texte du bouton en utilisant la police de caractères chargée
        surface_texte = self.font.render(self.text, True, noir)
        Dimmensions_texte = surface_texte.get_rect(center=self.rect.center)
        fenetre.blit(surface_texte, Dimmensions_texte)


# Créer les boutons
buttons = []
buttons.append(Button("Jouer", (0, 0)))
buttons.append(Button("Credits", (0, 0)))
buttons.append(Button("Quitter", (0, 0)))

# Calculer la position de chaque bouton
button_width, button_height = 300, 75
vertical_spacing = 80  # Espacement vertical entre les boutons
for i, button in enumerate(buttons):
    button_x = (largeur - button_width) // 2
    button_y = 200 + i * (button_height + vertical_spacing)  # Modification ici
    button_pos = (button_x, button_y)
    button.rect = pygame.Rect(button_pos, (button_width, button_height))
    # Initialiser la police pour les crédits
    credits_font = pygame.freetype.Font("style.ttf", 16)

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Vérifier si l'utilisateur a cliqué sur un bouton
            for button in buttons:
                if button.rect.collidepoint(event.pos):
                    # Action à effectuer lorsque le bouton est cliqué
                    if button.text == "Jouer":
                        # Initialize Pygame
                        pygame.init()
                        fenetre = pygame.display.set_mode((largeur, hauteur))

                        # Create the buttons
                        buttons = []
                        buttons.append(Button("Mastemind Normal", (0,0)))
                        buttons.append(Button("Mastermind IA", (0,0)))

                        # Calculer la position de chaque bouton
                        button_width, button_height = 800, 75
                        vertical_spacing = 150  # Espacement vertical entre les boutons
                        for i, button in enumerate(buttons):
                            button_x = (largeur - button_width) // 2
                            button_y = 200 + i * (button_height + vertical_spacing)
                            button_pos = (button_x, button_y)
                            button.rect = pygame.Rect(button_pos, (button_width, button_height))
                    elif button.text == "Mastemind Normal":
                        pygame.mixer.music.stop()
                        pygame.mixer.music.load()
                        pygame.mixer.music.set_volume(0.1)
                        pygame.mixer.music.play()
                    elif button.text == "Mastermind IA":
                        # Initialize Pygame
                        pygame.init()
                        fenetre = pygame.display.set_mode((largeur, hauteur))

                        # Create the buttons
                        buttons = []
                        buttons.append(Button("Mastermind petit QI", (0,0)))
                        buttons.append(Button("Mastermind moyen QI", (0,0)))
                        buttons.append(Button("Mastermind gros QI", (0,0)))

                        # Calculer la position de chaque bouton
                        button_width, button_height = 600, 75
                        vertical_spacing = 100  # Espacement vertical entre les boutons
                        for i, button in enumerate(buttons):
                            button_x = (largeur - button_width) // 2
                            button_y = 200 + i * (button_height + vertical_spacing)
                            button_pos = (button_x, button_y)
                            button.rect = pygame.Rect(button_pos, (button_width, button_height))

                    elif button.text == "Mastermind petit QI":
                        pygame.mixer.music.stop()
                        pygame.mixer.music.load()
                        pygame.mixer.music.set_volume(0.1)
                        pygame.mixer.music.play()
                    elif button.text == "Mastermind moyen QI":
                        pygame.mixer.music.stop()
                        pygame.mixer.music.load()
                        pygame.mixer.music.set_volume(0.1)
                        pygame.mixer.music.play()
                    elif button.text == "Mastermind gros QI":
                        pygame.mixer.music.stop()
                        pygame.mixer.music.load()
                        pygame.mixer.music.set_volume(0.1)
                        pygame.mixer.music.play()
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

    # Dessiner la fenêtre
    fenetre.fill(couleur)
    fenetre.blit(surface_texte_M, Dimmensions_texte)  #afficher le texte
    for button in buttons:
        button.draw(fenetre)  # actualiser l'affichage
    pygame.display.flip()
    pygame.display.set_caption("Mastermind de la squirrel monkey corp")
# Quitter Pygame
pygame.quit()
