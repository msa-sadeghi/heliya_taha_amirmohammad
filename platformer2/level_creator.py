import pygame
pygame.init()

WIDTH = 800
HEIGHT = 640
lower_margin = 100
side_margin = 300
scroll = 0
scroll_sp
scroll_left = False
scroll_right = False
clock = pygame.time.Clock()
FPS = 60
screen = pygame.display.set_mode((WIDTH + side_margin, HEIGHT + lower_margin))

pine1_image = pygame.image.load("./assets/images/background/pine1.png")
pine2_image = pygame.image.load("./assets/images/background/pine2.png")
mountain_image = pygame.image.load("./assets/images/background/mountain.png")
sky_image = pygame.image.load("./assets/images/background/sky_cloud.png")

def draw_bg():
    screen.fill("green")
    sky_width = sky_image.get_width()
    for i in range(4):
        screen.blit(sky_image, (i * sky_width  - scroll* 0.3,0))
        screen.blit(mountain_image, (i * sky_width  - scroll* 0.4,HEIGHT - mountain_image.get_height() - 300))
        screen.blit(pine1_image, (i * sky_width - scroll * 0.5,HEIGHT - pine1_image.get_height() - 150))
        screen.blit(pine2_image, (i * sky_width - scroll * 0.6,HEIGHT - pine2_image.get_height()))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                scroll_left = True
            if event.key == pygame.K_RIGHT:
                scroll_right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                scroll_left = False
            if event.key == pygame.K_RIGHT:
                scroll_right = False
    if scroll_left and scroll > 0:
        scroll -= 5            
    if scroll_right:
        scroll += 5            
    draw_bg()        
    pygame.display.update()
    clock.tick(FPS)