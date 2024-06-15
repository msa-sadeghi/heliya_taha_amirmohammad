from pygame.sprite import Sprite
import pygame
import math
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
class Bullet(Sprite):
    def __init__(self, x,y,direction, group):
        super().__init__()
        self.image = pygame.image.load("assets/bullet.png")
        self.image = pygame.transform.scale(self.image, (16,16))
        self.rect = self.image.get_rect(topleft = (x,y))
        self.direction = direction
        self.speed = 10
        group.add(self)
        
    def update(self):
        self.rect.x += self.speed * math.cos(self.direction)
        self.rect.y += -self.speed * math.sin(self.direction)
        if self.rect.left > SCREEN_WIDTH or self.rect.right < 0 or self.rect.bottom < 0 or self.rect.top > SCREEN_HEIGHT:
            self.kill()
        
        