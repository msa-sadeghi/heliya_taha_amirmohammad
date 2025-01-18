from pygame.sprite import Sprite
import pygame
from explosion import Explosion
class Grenade(Sprite):
    def __init__(self, x,y, group, direction):
        super().__init__()
        self.image = pygame.image.load("./assets/images/icons/grenade.png")
        self.rect = self.image.get_rect(topleft=(x,y))
        
        self.y_vel = -15
        self.timer = 100
        self.direction = direction
        group.add(self)        
    def update(self, explosion_group):
        self.y_vel += 1
        dx = self.direction * 4
        dy = self.y_vel
        if self.rect.bottom + dy > 300:
            dy = 300 - self.rect.bottom
            self.y_vel = 0
            dx = 0            
        self.timer -= 1
        if self.timer <= 0:
            self.kill()
            exp = Explosion(self.rect.x , self.rect.y)
            explosion_group.add(exp)
            # TODO implement Damage
        self.rect.x += dx
        self.rect.y += dy
        
        
        
        