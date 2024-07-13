from pygame.sprite import Sprite
import pygame
import os
class Enemy(Sprite):
    def __init__(self, type, x,y, group, speed, health):
        super().__init__()
        self.type = type
        self.speed = speed
        self.health = health
        self.animation_types = ("walk", "attack", "death")
        self.all_images = {}
        for animation in self.animation_types:
            temp_list = []
            # number_of_images = len(os.listdir(f"assets/enemies/{self.type}/{animation}"))
            # print(number_of_images)
            for i in range(20):
                img = pygame.image.load(f"assets/enemies/{self.type}/{animation}/{i}.png")
                img_w = img.get_width()
                img_h = img.get_height()
                img = pygame.transform.scale(img, (img_w * 0.5, img_h * 0.5))
                temp_list.append(img)
            self.all_images[animation] = temp_list
        self.image = self.all_images["walk"][0]
        self.rect = self.image.get_rect(topleft = (x,y))
        self.image_number = 0
        self.action = "walk"
        group.add(self)
    def update(self)         :
        self.move()
        self.animation()
    def move(self):
        self.rect.x += self.speed
    def animation(self):
        pass
            
        
      
