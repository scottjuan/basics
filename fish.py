import pygame
class fish:
    def __init__(self, pos):
        self.image = pygame.image.load("fish.png")
        self.image_rect = fish.get_rect()
        self.speed= pygame.math.Vector2(65, 53)
