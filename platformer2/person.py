from pygame.sprite import Sprite
from config import *
import os


class Person(Sprite):
    def __init__(self, type_, x, y, ammo, grenades):
        super().__init__()
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
            num_of_images = len(os.listdir(
                f"assets/images/{type_}/{animation}"))
            for i in range(num_of_images):
                img = pygame.image.load(
                    f"assets/images/{type_}/{animation}/{i}.png")
                img_w = img.get_width()
                img_h = img.get_height()
                img = pygame.transform.scale(img, (img_w * 1.8, img_h * 1.8))
                temp_list.append(img)

            self.image_dict[animation] = temp_list
        self.image_number = 0
        self.action = self.animation_types[1]
        self.image = self.image_dict[self.action][0]
        self.rect = self.image.get_rect(topleft=(x, y))
        self.last_image_change_time = 0
        self.firection = 1
        self.flip = False
        self.vely = 0
        self.in_air = False
        

    def draw(self, screen):
        self.animation()
        img = self.image_dict[self.action][self.image_number]
        img = pygame.transform.flip(img, self.flip, False)
        screen.blit(img, self.rect)

    def animation(self):
        if pygame.time.get_ticks() - self.last_image_change_time > 100:
            self.last_image_change_time = pygame.time.get_ticks()
            self.image_number += 1
            if self.image_number >= len(self.image_dict[self.action]):
                self.image_number = 0

    def move(self, moving_left, moving_right):
        dx = 0
        dy = 0
        if moving_left:
            self.direction = -1
            self.flip = True
            dx -= 5
        elif moving_right:
            self.direction = 1
            self.flip = False
            dx += 5
        
        if self.rect.bottom + dy > 300:
            dy = 300 - self.rect.bottom
            self.vely = 0
            self.in_air = False
        
        
        dy += self.vely
        self.vely += 1
        self.rect.y += dy
        self.rect.x += dx

    def change_animation_type(self, new_type):
        if new_type != self.action:
            self.action = new_type
            self.image_number = 0
            self.last_image_change_time = 0
            
            
    def shoot(self):
        #TODO
        pass
