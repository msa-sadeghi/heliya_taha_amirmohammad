import pygame

class Button:
    def __init__(self, x,y, image):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect(topleft=(x,y))
        self.clicked = False
        
        
    def draw(self,screen):
        action = False
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                action = True
                self.clicked = True
        if not pygame.mouse.get_pressed()[0]:
            self.clicked = False
            
        screen.blit(self.image, self.rect) 
        return action   