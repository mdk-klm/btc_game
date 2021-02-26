import pygame
from game import Game
pygame.init()



# generer la fenêtre du jeu
pygame.display.set_caption("Comet fall game")
screen = pygame.display.set_mode((1080, 720))

# importer l'arriere plan
background = pygame.image.load('assets/bg.jpg')


# charger le jeu
game = Game()
running = True

while running:

    # appliquer arriere plan
    screen.blit(background, (0, -200))

    # appliquer l'image du joueur
    screen.blit(game.player.image, game.player.rect)

    # recupérer les projectiles du joueur
    for projectile in game.player.all_projectiles:
        projectile.move()

    # appliquer image projectile
    game.player.all_projectiles.draw(screen)


    # mettre a jour l'écran
    pygame.display.flip()

    # verifier si le joueur souhaite aller a gauche ou a droite
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

    print(game.player.rect.x)

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
