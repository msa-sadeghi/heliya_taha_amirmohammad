from pygame.sprite import Sprite
import pygame
class Bullet(Sprite):
    def __init__(self, x,y,owner, group, direction):
        super().__init__()
        self.image = pygame.image.load("assets/images/icons/bullet.png")
        self.rect = self.image.get_rect(topleft=(x,y))
        self.owner = owner
        self.direction = direction
        group.add(self)
        
    def update(self):
        self.rect.x += 4 * self.direction
        if self.rect.x <= 0 or self.rect.x >= 800:
            self.kill()