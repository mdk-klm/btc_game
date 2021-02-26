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
            # quelle touche ?
            if event.key == pygame.K_RIGHT:
                print("droite")
