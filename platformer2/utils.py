import pygame
image_list = []
ROWS = 16
COLS = 150
TILE_SIZE = 800/ROWS

for i in range(21):
    img = pygame.image.load(f"./assets/images/tile/{i}.png")
    img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
    image_list.append(img)
    
    