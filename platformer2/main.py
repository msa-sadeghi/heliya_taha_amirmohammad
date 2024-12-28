from config import *
from person import Person
clock = pygame.time.Clock()

player = Person('player', 100, 300, 60, 10)
moving_left = False
moving_right = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moving_left = True
            if event.key == pygame.K_RIGHT:
                moving_right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_left = False
            if event.key == pygame.K_RIGHT:
                moving_right = False
    if player.alive:
        if moving_left or moving_right:
            player.change_animation_type("Run")
        else:
            player.change_animation_type("Idle")
        
    
    screen.fill((0,0,0))        
    player.draw(screen)   
    player.move(moving_left, moving_right)     
    pygame.display.update()
    clock.tick(FPS)