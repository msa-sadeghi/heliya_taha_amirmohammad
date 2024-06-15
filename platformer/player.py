from pygame.sprite import Sprite
import pygame
from constants import *
class Player(Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.right_images = []
        self.left_images = []
        for i in range(1, 5):
            img = pygame.image.load(f"assets/guy{i}.png")
            img = pygame.transform.scale(img, (64, 64))
            self.right_images.append(img)
            img = pygame.transform.flip(img, True, False)
            self.left_images.append(img)
       
        
        self.frame_index = 0
        self.counter = 0
        self.image = self.right_images[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.vel_y = 0
        self.jumped = False
        self.direction = 1
        self.idle = True
        self.inair = False
        self.dead_image = pygame.image.load("assets/ghost.png")
        self.alive = True
        

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
    def update(self, tiles, enemy_group, door_group, game_world):
        dx = 0
        dy = 0        
        if self.alive:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.direction = -1
                self.idle = False
                dx -= 5
            if keys[pygame.K_RIGHT]:
                self.direction = 1
                self.idle = False
                dx += 5
            if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
                self.idle = True
                
            if keys[pygame.K_SPACE]:
                self.vel_y = -15        
                
            dy += self.vel_y
            self.vel_y += 1
            for t in tiles:
                if t[1].colliderect(self.rect.x + dx, self.rect.y , self.rect.width, self.rect.height):
                    dx = 0
                if t[1].colliderect(self.rect.x, self.rect.y + dy, self.rect.width, self.rect.height):
                    self.vel_y = 0
                    dy = 0
            if pygame.sprite.spritecollide(self, enemy_group, True):
                self.alive = False
            if pygame.sprite.spritecollide(self, door_group, False):
                game_world.next_level = True
            self.animation() 
        if not self.alive:
            self.image = self.dead_image
        
        self.rect.x += dx
        self.rect.y += dy
                
        
    def animation(self):
        self.counter += 1
        if self.counter >= 10:
            self.frame_index += 1
            self.counter = 0
        
        if self.frame_index >= len(self.right_images) or self.idle:
            self.frame_index = 0
        if self.direction == 1:
            self.image = self.right_images[self.frame_index]
        elif self.direction == -1:
            self.image = self.left_images[self.frame_index]
        
        
  

      

        