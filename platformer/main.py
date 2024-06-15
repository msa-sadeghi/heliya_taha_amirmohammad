import pygame
from constants import *
from world import World
from player import Player
from button import Button
import pickle

f = open("levels\level1", "rb")
world_data = pickle.load(f)


def change_level(level):
    my_player.__init__(100, 300)
    door_group.empty()
    enemy_group.empty()
    f = open(f"levels\level{level}", "rb")
    world_data = pickle.load(f)
    game_world= World(world_data, enemy_group, door_group)
    return game_world
    


pygame.init()
restart_btn = Button(screen_width/2, screen_height/2)
screen = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()
enemy_group = pygame.sprite.Group()
door_group = pygame.sprite.Group()

bg_img = pygame.image.load("assets/sky.png")

game_world= World(world_data, enemy_group, door_group)
my_player = Player(100, 300)
level = 1
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(bg_img, (0,0))
    
    game_world.draw(screen)    
    my_player.draw(screen)  
    my_player.update(game_world.tile_list, enemy_group, door_group, game_world)
    if my_player.alive:
        enemy_group.update()
        if game_world.next_level:
            level += 1
            game_world = change_level(level)
            game_world.next_level = False
            
    enemy_group.draw(screen)
    door_group.draw(screen)
    if not my_player.alive:
        restart_btn.draw(screen)
        if restart_btn.click():
            my_player.__init__(100,300)
            enemy_group.empty()
            door_group.empty()
            game_world= World(world_data, enemy_group, door_group)

    pygame.display.update()
    clock.tick(FPS)

