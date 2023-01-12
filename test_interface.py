import pygame

# Initialiser Pygame
pygame.init()

# Définir la taille de la fenêtre
screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Définir les couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
couleur = (39, 174, 173)


class Button:
    def __init__(self, text, pos):
        self.text = text
        self.pos = pos
        self.rect = pygame.Rect(pos, (150, 50))

    def draw(self, screen):
        # Dessiner le fond du bouton
        pygame.draw.rect(screen, WHITE, self.rect)

        # Dessiner le texte du bouton
        text_surface = font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)


# Charger la police de caractères
font = pygame.font.Font(None, 36)

# Créer les boutons
buttons = []
buttons.append(Button("Jouer", (screen_width // 2 - 50, 100)))
buttons.append(Button("Paramètres", (screen_width // 2 - 75, 150)))
buttons.append(Button("Crédits", (screen_width // 2 - 50, 200)))
buttons.append(Button("Quitter", (screen_width // 2 - 60, 250)))

# Calculer la position de chaque bouton
button_width, button_height = 150, 50
for i, button in enumerate(buttons):
    button_x = (screen_width - button_width) // 2
    button_y = 100 + i * 50
    button_pos = (button_x, button_y)
    button.pos = button_pos
    button.rect = pygame.Rect(button_pos, (button_width, button_height))

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
                        print("Jouer")
                    elif button.text == "Paramètres":
                        print("Paramètres")
                    elif button.text == "Quitter":
                        running = False
                    elif button.text == "Crédits":
                        print("Crédits")
    # Dessiner la fenêtre
    screen.fill(couleur)
    for button in buttons:
        button.draw(screen)
    pygame.display.flip()

# Quitter Pygame
pygame.quit()
