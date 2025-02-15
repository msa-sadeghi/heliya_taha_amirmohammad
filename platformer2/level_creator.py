import pygame
pygame.init()

WIDTH = 800
HEIGHT = 640
lower_margin = 100
side_margin = 300
scroll = 0
scroll_speed = 1
scroll_left = False
scroll_right = False
clock = pygame.time.Clock()
FPS = 60
MAX_COLS = 150
ROWS = 15
TILE_SIZE = HEIGHT // ROWS


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


def draw_lines():
    for i in range(MAX_COLS + 1):
        pygame.draw.line(screen, "white", (i * TILE_SIZE - scroll,0), (i * TILE_SIZE - scroll, HEIGHT))
    for i in range(ROWS + 1):
        pygame.draw.line(screen, "white", (0,i * TILE_SIZE), (WIDTH, i * TILE_SIZE))
    

images_list = list()
for i in range(21):
    img = pygame.image.load(f"./assets/images/tile/{i}.png")
    images_list.append(img)

buttons_list = list()
col = 0
row = 0



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
            if event.key == pygame.K_LSHIFT:
                scroll_speed = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                scroll_left = False
            if event.key == pygame.K_RIGHT:
                scroll_right = False
            if event.key == pygame.K_LSHIFT:
                scroll_speed = 1
    if scroll_left and scroll > 0:
        scroll -= 5  * scroll_speed          
    if scroll_right:
        scroll += 5    * scroll_speed        
    draw_bg()
    draw_lines()       
    pygame.draw.rect(screen, "lightgreen", (WIDTH, 0, side_margin, HEIGHT + lower_margin)) 
    pygame.display.update()
    clock.tick(FPS)