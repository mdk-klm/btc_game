import pygame

class DollaFallEvent:
    # lors du chargment, créer un compteur

    def __init__(self):
        self.percent = 0
        self.percent_speed = 5

    def add_percent(self):
        self.percent += self.percent_speed / 100

    def update_bar(self, surface):

        # ajouter pourcentage a la barre

        self.add_percent()

        # barre noir en arriere-plan
        pygame.draw.rect(surface, (0, 0, 0), [
            0,
            surface.get_height() - 20, # l'axe y
            surface.get_width(), # longueur
            10 # épaisseur
        ])
        # jauge event
        pygame.draw.rect(surface, (187, 11, 11), [
            0,
            surface.get_height() - 20,  # l'axe y
            (surface.get_width() / 100) * self.percent,  # longueur
            10  # épaisseur
        ])