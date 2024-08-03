import pygame
from constants import *
from world import World
from castle import Castle
from game import Game
from enemy import Enemy
import random
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
world = World()
bullet_group = pygame.sprite.Group()
castle = Castle(SCREEN_WIDTH - 280, SCREEN_HEIGHT - 340)
enemy_group = pygame.sprite.Group()

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    world.draw(screen)
    
    if Game.level_difficulty < Game.max_difficulty and pygame.time.get_ticks() - Game.enemy_spawn_time > 2000:
        
        e_type = random.randrange(len(Game.enemy_types))
        Enemy(Game.enemy_types[e_type],
              0, 
              SCREEN_HEIGHT / 2, 
              enemy_group, 
              Game.enemy_speeds[e_type],
              Game.enemy_healths[e_type]
              )
        Game.level_difficulty += Game.enemy_healths[e_type]
        Game.enemy_spawn_time = pygame.time.get_ticks()
    
    
    enemy_group.draw(screen)
    enemy_group.update(castle)
    castle.shoot(bullet_group) 
    castle.draw(screen)   
    bullet_group.update()    
    bullet_group.draw(screen)
    pygame.display.update()
    clock.tick(FPS)
    