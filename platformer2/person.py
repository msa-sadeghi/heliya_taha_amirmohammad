from pygame.sprite import Sprite
from config import *
import os
class Person(Sprite):
    def __init__(self, type_, x,y, ammo, grenades):
        self.alive = True
        self.health = 100
        self.max_health = 100
        self.type = type_
        self.ammo = ammo
        self.grenades = grenades
        self.image_dict = {}
        self.animation_types = os.listdir(f"assets/images/{type_}")
        for animation in self.animation_types:
            temp_list = []
            num_of_images = len(os.listdir(f"assets/images/{type_}/{animation}"))
            for i in range(num_of_images):
                img =pygame.image.load(f"assets/images/{type_}/{animation}/{i}.png")
                img_w = img.get_width()
                img_h = img.get_height()
                img = pygame.transform.scale(img, (img_w * 1.5, img_h * 1.5))
                temp_list.append(img)
                
            self.image_dict[animation] = temp_list
        self.image_number = 0
        self.action = self.animation_types[1]
        self.image = self.image_dict[self.action][0]
        self.rect = self.image.get_rect(topleft=(x,y))
        
    def draw(self, screen)  :
        screen.blit(self.image, self.rect)

            
                
        
        
