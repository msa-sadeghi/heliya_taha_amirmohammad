from config import *
from person import Person
clock = pygame.time.Clock()
player_bullet_group = pygame.sprite.Group()
enemy_bullet_group = pygame.sprite.Group()
player_grenade_group = pygame.sprite.Group()
explosion_group = pygame.sprite.Group()
player = Person('player', 100, 300, 60, 10)
moving_left = False
moving_right = False
jump = False
shoot = False

enemy = Person("enemy", 400, 300, 10, 0)



grenade_shoot = False
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
            if event.key == pygame.K_UP:
                jump = True
            if event.key == pygame.K_SPACE:
                shoot = True
            if event.key == pygame.K_g:
                grenade_shoot = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_left = False
            if event.key == pygame.K_RIGHT:
                moving_right = False
            if event.key == pygame.K_UP:
                jump = False
            if event.key == pygame.K_SPACE:
                shoot = False
            if event.key == pygame.K_g:
                grenade_shoot = False
    if player.alive:
        if moving_left or moving_right:
            player.change_animation_type("Run")
        elif jump and player.in_air == False:
            player.vely = -15
            player.in_air = True
            
        else:
            player.change_animation_type("Idle")
        if player.in_air:
            player.change_animation_type("Jump")
        if shoot:
            player.shoot("bullet",player_bullet_group)
        if grenade_shoot:
            player.shoot("grenade",player_grenade_group)
            
    if enemy.idle:
        enemy.change_animation_type("Idle")
    else:
        enemy.change_animation_type("Run")    
    if enemy.shoot_state:
        enemy.shoot("bullet", enemy_bullet_group)
    
    screen.fill((0,0,0))        
    enemy.draw(screen)
    enemy.ai(player)
   
    player.draw(screen)   
    player.move(moving_left, moving_right)    
    player_bullet_group.update()
    player_bullet_group.draw(screen) 
    enemy_bullet_group.update()
    enemy_bullet_group.draw(screen) 
    player_grenade_group.update(explosion_group)
    player_grenade_group.draw(screen) 
    explosion_group.update()
    explosion_group.draw(screen)
    pygame.display.update()
    clock.tick(FPS)