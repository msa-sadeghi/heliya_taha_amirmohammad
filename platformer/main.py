import pygame
from constants import *
from world import World

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()


bg_img = pygame.image.load("assets/sky.png")



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(bg_img, (0,0))
    
    


            
           
        


    pygame.display.update()
    clock.tick(FPS)

