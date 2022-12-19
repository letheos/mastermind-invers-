import pygame

pygame.init()

# Définition de la taille de la fenêtre
window_width, window_height = 640, 480

# Création de la fenêtre
screen = pygame.display.set_mode((window_width, window_height))

# Chargement des images des boutons
play_button_image = pygame.image.load("play_button.png")
settings_button_image = pygame.image.load("settings_button.png")
quit_button_image = pygame.image.load("quit_button.png")
credits_button_image = pygame.image.load("credits_button.png")

# Création des boutons
play_button = pygame.Rect(50, 50, 100, 50)  # (x, y, largeur, hauteur)
settings_button = pygame.Rect(50, 110, 100, 50)
quit_button = pygame.Rect(50, 170, 100, 50)
credits_button = pygame.Rect(50, 230, 100, 50)

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Vérification des clics de souris
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if play_button.collidepoint(mouse_x, mouse_y):
                # Code à exécuter lorsque le bouton "Jouer" est cliqué
                pass
            elif settings_button.collidepoint(mouse_x, mouse_y):
                # Code à exécuter lorsque le bouton "Paramètres" est cliqué
                pass
            elif quit_button.collidepoint(mouse_x, mouse_y):
                # Code à exécuter lorsque le bouton "Quitter" est cliqué
                running = False
            elif credits_button.collidepoint(mouse_x, mouse_y):
                # Code à exécuter lorsque le bouton "Crédits" est cliqué
                pass

    # Dessin des boutons sur l'écran
    screen.blit(play_button_image, play_button)
    screen.blit(settings_button_image, settings_button)
    screen.blit(quit_button_image, quit_button)
    screen.blit(credits_button_image, credits_button)

    pygame.display.flip()

pygame.quit()
