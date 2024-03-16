import pygame
from constants import *
from world import World
from player import Player
from levels.level_creator import world_data
pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()


bg_img = pygame.image.load("assets/sky.png")

game_world= World(world_data)
my_player = Player(100, 500)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(bg_img, (0,0))
    
    game_world.draw(screen)    
    my_player.draw(screen)  
    my_player.update()


    pygame.display.update()
    clock.tick(FPS)

