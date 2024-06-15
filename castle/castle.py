import pygame
class Castle:
    def __init__(self, x,y):
        
        self.image_100 = pygame.image.load("assets/castle/castle_100.png")
        w = self.image_100.get_width()
        h = self.image_100.get_height()
        self.image_100 = pygame.transform.scale(self.image_100, (w * 0.2, h * 0.2))
        self.image_50 = pygame.image.load("assets/castle/castle_50.png")
        w = self.image_50.get_width()
        h = self.image_50.get_height()
        self.image_50 = pygame.transform.scale(self.image_50, (w * 0.2, h * 0.2))
        self.image_25 = pygame.image.load("assets/castle/castle_25.png")
        w = self.image_25.get_width()
        h = self.image_25.get_height()
        self.image_25 = pygame.transform.scale(self.image_25, (w * 0.2, h * 0.2))
        self.image = self.image_100
        self.rect = self.image.get_rect(topleft = (x,y))
        self.health = 100
        self.max_health = self.health
        self.score = 0
        self.money = 0
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
        