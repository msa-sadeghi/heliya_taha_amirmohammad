from constants import *
from pygame.sprite import Sprite
from enemybullet import EnemyBullet
import random
class Enemy(Sprite):
    def __init__(self, x,y, group):
        super().__init__()
        self.image = pygame.image.load("assets/enemy.png")
        self.rect = self.image.get_rect(topleft=(x,y))
        self.direction = 1
        self.speed = 5
        group.add(self)
        
    def update(self,group):
        self.rect.x += self.speed * self.direction
        self.fire(group)
        
    def fire(self, group):
        if random.randint(1, 1000) > 999:
            EnemyBullet(self.rect.centerx, self.rect.bottom, group)
            
        
        
    
        