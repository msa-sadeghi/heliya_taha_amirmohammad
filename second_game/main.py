import random
import pygame
pygame.init()
FPS = 60
clock = pygame.time.Clock()
screen = pygame.display.set_mode()
screen_width = screen.get_width()
screen_height = screen.get_height()
bg_image = pygame.image.load("assets/bg.png")
bg_image = pygame.transform.scale(bg_image, (screen_width, screen_height))
bg_rect = bg_image.get_rect()
bg_rect.topleft = (0,0)
dog_image = pygame.image.load("assets/d.png")
dog_rect = dog_image.get_rect()
dog_rect.bottom = screen_height
dog_rect.centerx = screen_width/2
bone_image = pygame.image.load("assets/b.png")
bone_rect = bone_image.get_rect()
bone_rect.top = 0
bone_rect.centerx = random.randint(36, screen_width-36)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    bone_rect.y += 10
    if bone_rect.top >= screen_height:
        bone_rect.top = 0
        bone_rect.centerx = random.randint(36, screen_width-36)
    screen.blit(bg_image, bg_rect)
    screen.blit(dog_image, dog_rect)
    screen.blit(bone_image, bone_rect)
    pygame.display.update()
    clock.tick(FPS)