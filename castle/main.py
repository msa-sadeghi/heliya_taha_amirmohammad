import pygame
from constants import *
from world import World
from castle import Castle
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
world = World()

castle = Castle(SCREEN_WIDTH - 280, SCREEN_HEIGHT - 340)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    world.draw(screen) 
    castle.draw(screen)       
    pygame.display.update()
    clock.tick(FPS)
    