import random
import pygame
pygame.init()


def game_over():
    global score, lives
    score = 0
    lives = 3
    game_over_text = my_font48.render("Game Over, Press Enter to play again", True, (123,10,245))
    game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    SCREEN.blit(game_over_text, game_over_rect)
    pygame.display.update()

    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    paused = False
            if event.type == pygame.QUIT:
                pass






score = 0
lives = 3

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 780

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
FPS = 60
CLOCK = pygame.time.Clock()
my_font = pygame.font.Font("dragonfont.otf", 72)
welcome_text = my_font.render("Welcome To my Game", True, (170,10,190))
welcome_rect = welcome_text.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

my_font48 = pygame.font.Font("dragonfont.otf", 48)
score_text = my_font48.render(f"Score: {score}", True, (10,230,190))
score_rect = score_text.get_rect(topleft=(0,0))


lives_text = my_font48.render(f"Lives:{lives}", True, (10,230,250))
lives_rect = lives_text.get_rect(topright = (SCREEN_WIDTH, 0))

start_time = pygame.time.get_ticks()

wolf_img = pygame.image.load("wolf.png")
wolf_rect = wolf_img.get_rect()
wolf_rect.bottomright = (SCREEN_WIDTH, SCREEN_HEIGHT)

# load sheep image
sheep_img = pygame.image.load("sheep.png")
sheep_img = pygame.transform.flip(sheep_img, True, False)
sheep_rect = sheep_img.get_rect()
sheep_rect.left = 0
sheep_rect.y = random.randint(100,SCREEN_HEIGHT-100)
sheep_velocity = 5
wolf_velocity = 4


pygame.mixer.music.load("Bad Piggies Theme.mp3")
# pygame.mixer.music.set_volume(0.9)
pygame.mixer.music.play(-1)
loss_sound = pygame.mixer.Sound("loss.wav")
running = True
while running:
    # مدیریت کردن رویدادها
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and wolf_rect.top > 100:
        wolf_rect.y -= wolf_velocity
    if keys[pygame.K_DOWN] and wolf_rect.bottom < SCREEN_HEIGHT:
        wolf_rect.y += wolf_velocity
    if keys[pygame.K_LEFT] and wolf_rect.left > 0:
        wolf_rect.x -= wolf_velocity
    if keys[pygame.K_RIGHT] and wolf_rect.right < SCREEN_WIDTH:
        wolf_rect.x += wolf_velocity
    score_text = my_font48.render(f"Score: {score}", True, (10,230,190))
    lives_text = my_font48.render(f"Lives:{lives}", True, (10,230,250))
    SCREEN.fill((0,0,0))
    if pygame.time.get_ticks() - start_time < 3000:
        SCREEN.blit(welcome_text, welcome_rect)
    else:
        sheep_rect.x += sheep_velocity
        if wolf_rect.colliderect(sheep_rect):
            score += 1
            sheep_rect.left = 0
            sheep_rect.y = random.randint(100,SCREEN_HEIGHT-100)
        if sheep_rect.left >=SCREEN_WIDTH:
            lives -= 1
            loss_sound.play()
            sheep_rect.left = 0
            sheep_rect.y = random.randint(100,SCREEN_HEIGHT-100)

            if lives <= 0:
                game_over()

        SCREEN.blit(score_text, score_rect)
        SCREEN.blit(lives_text, lives_rect)
        SCREEN.blit(wolf_img, wolf_rect)
        SCREEN.blit(sheep_img, sheep_rect)
    
    pygame.display.update()
    CLOCK.tick(FPS)


pygame.quit()


