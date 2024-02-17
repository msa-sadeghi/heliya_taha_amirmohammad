from constants import *
from pygame.sprite import Sprite
from playerbullet import PlayerBullet
class Player(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/space.png")
        self.image = pygame.transform.rotate(self.image, 180)
        self.image = pygame.transform.scale(self.image, (64,64))
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH/2
        self.rect.bottom = SCREEN_HEIGHT
    def draw(self):
        screen.blit(self.image, self.rect)
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += 5
            
    def shoot(self, group):
        PlayerBullet(self.rect.centerx, self.rect.top, group)
        
        