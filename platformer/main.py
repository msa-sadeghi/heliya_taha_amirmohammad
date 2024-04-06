import pygame
from constants import *
from world import World
from player import Player
from button import Button
from levels.level_creator import world_data
pygame.init()
restart_btn = Button(screen_width/2, screen_height/2)
screen = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()
enemy_group = pygame.sprite.Group()

bg_img = pygame.image.load("assets/sky.png")

game_world= World(world_data, enemy_group)
my_player = Player(100, 500)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(bg_img, (0,0))
    
    game_world.draw(screen)    
    my_player.draw(screen)  
    my_player.update(game_world.tile_list, enemy_group)
    if my_player.alive:
        enemy_group.update()
    enemy_group.draw(screen)
    if not my_player.alive:
        restart_btn.draw(screen)

    pygame.display.update()
    clock.tick(FPS)

