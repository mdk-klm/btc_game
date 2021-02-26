import pygame
from game import Game
import math

pygame.init()

# generer la fenêtre du jeu
pygame.display.set_caption("Comet fall game")
screen = pygame.display.set_mode((1080, 720))

# importer l'arriere plan
background = pygame.image.load('assets/bg.jpg')

# importer la bannière
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

# import bouton pour lancer la partie
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)

# charger le jeu
game = Game()
running = True

while running:

    # appliquer arriere plan
    screen.blit(background, (0, -200))

    #vérifier si le jeu a commencé ou non
    if game.is_playing:
        # declencher les instructions
        game.update(screen)

    # vérifier si le jeu n'a pas commencencé
    else:
        # ajouter ecran accueil
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)


    # mettre a jour l'écran
    pygame.display.flip()


    # si fenetre fermée
    for event in pygame.event.get():
        # que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        # detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # detecter touche espace
            if event.key == pygame.K_SPACE:
                game.player.launch_eth()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # vérification pour savoir si la souris est sur le bouton
            if play_button_rect.collidepoint(event.pos):
                # mettre le jeu en mode "lancé"
                game.start()
