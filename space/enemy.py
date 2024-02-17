from constants import *
from pygame.sprite import Sprite
class Enemy(Sprite):
    def __init__(self, x,y, group):
        super().__init__()
        self.image = pygame.image.load("assets/enemy.png")
        self.rect = self.image.get_rect(topleft=(x,y))
        self.direction = 1
        self.speed = 5
        group.add(self)
        
    def update(self):
        self.rect.x += self.speed * self.direction
        
    
        