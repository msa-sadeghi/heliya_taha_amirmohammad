from constants import *
from player import Player
from enemy import Enemy
level = 1
enemy_group = pygame.sprite.Group()
player_bullet_group = pygame.sprite.Group()
enemy_bullet_group = pygame.sprite.Group()
def spawn_enemies():
    for i in range(4):
        for j in range(8):
            Enemy(j * 96, i * 96, enemy_group)           
spawn_enemies()

def check_bullet_collisions():
    if pygame.sprite.groupcollide(player_bullet_group, enemy_group, True, True):
        pass


def check_edge_collisions():
    on_edge = False
    for enemy in enemy_group:
        if enemy.rect.left < 0 or enemy.rect.right > SCREEN_WIDTH:
            on_edge = True
            break
    if on_edge:
        for enemy in enemy_group:
            enemy.direction *= -1
            enemy.rect.y += level * 10
player_1 = Player()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                player_1.shoot(player_bullet_group)
    check_edge_collisions()
    check_bullet_collisions()
    screen.fill((0,0,0))  
    enemy_group.draw(screen)         
    enemy_group.update(enemy_bullet_group)
    player_bullet_group.draw(screen)         
    player_bullet_group.update()
    enemy_bullet_group.draw(screen)         
    enemy_bullet_group.update()
    player_1.draw()
    player_1.move()
    pygame.display.update()
    clock.tick(FPS)