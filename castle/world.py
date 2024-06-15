import pygame
class World:
    def __init__(self) -> None:
        self.image = pygame.image.load("assets/bg.png")
    def draw(self, screen):
        screen.blit(self.image, (0,0))
        