from pygame.sprite import Sprite
import pygame
class Grenade(Sprite):
    def __init__(self, x,y, group, direction):
        super().__init__()
        self.image = pygame.image.load("./assets/images/icons/grenade.png")
        self.rect = self.image.get_rect(topleft=(x,y))
        
        self.y_vel = -15
        self.timer = 100
        self.direction = direction
        group.add(self)
        
        
    def update(self):
        self.y_vel += 1
        dx = self.direction * 4
        dy = self.y_vel
        if self.rect.bottom + dy > 300:
            dy = 300 - self.rect.bottom
            self.y_vel = 0
            dx = 0
        self.rect.x += dx
        self.rect.y += dy
        
        
        
        