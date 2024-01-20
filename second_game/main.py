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
bg_rect.topleft = (0, 0)

dog_image = pygame.image.load("assets/d.png")
dog_rect = dog_image.get_rect()
dog_rect.bottom = screen_height
dog_rect.centerx = screen_width / 2
dog_left_image = dog_image
dog_right_image = pygame.transform.flip(dog_left_image, True, False)

bone_image = pygame.image.load("assets/b.png")
bone_rect = bone_image.get_rect()
bone_rect.top = 0
bone_rect.centerx = random.randint(36, screen_width - 36)

START_SPEED_LEVEL = 200
speed_level = START_SPEED_LEVEL

font = pygame.font.SysFont("arial", 22)
speed_level_text = font.render(f"Speed Level:{speed_level}", True, (10,230,245))
speed_level_rect = speed_level_text.get_rect(top=0, centerx=screen_width/2)



NORMAL_SPEED = 5
FAST_SPEED = 15
speed = NORMAL_SPEED
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and dog_rect.top > 100:
        dog_rect.y -= speed
    if keys[pygame.K_DOWN] and dog_rect.bottom < screen_height:
        dog_rect.y += speed
    if keys[pygame.K_LEFT] and dog_rect.left > 0:
        dog_rect.x -= speed
        dog_image = dog_left_image
    if keys[pygame.K_RIGHT] and dog_rect.right < screen_width:
        dog_rect.x += speed
        dog_image = dog_right_image
    if keys[pygame.K_SPACE] and speed_level > 0:
        speed = FAST_SPEED
        speed_level -= 1
        if speed_level < 0:
            speed_level = 0
    if not keys[pygame.K_SPACE] or speed_level <= 0:
        speed = NORMAL_SPEED

    bone_rect.y += 10
    if bone_rect.top >= screen_height:
        bone_rect.top = 0
        bone_rect.centerx = random.randint(36, screen_width - 36)
    speed_level_text = font.render(f"Speed Level:{speed_level}", True, (10, 230, 245))
    screen.blit(bg_image, bg_rect)
    screen.fill((120, 10, 130))
    screen.blit(dog_image, dog_rect)
    screen.blit(bone_image, bone_rect)
    screen.blit(speed_level_text, speed_level_rect)
    pygame.display.update()
    clock.tick(FPS)
