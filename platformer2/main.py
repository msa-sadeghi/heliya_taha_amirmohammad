from config import *
from person import Person
clock = pygame.time.Clock()

player = Person('player', 100, 300, 60, 10)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    player.draw(screen)        
    pygame.display.update()
    clock.tick(FPS)