import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('First Game')
clock = pygame.time.Clock()
test_font = pygame.font.Font('./FirstGame/font/Pixeltype.ttf', 50)

sky_surf = pygame.image.load('./FirstGame/graphics/Sky.png').convert()
ground_surf = pygame.image.load('./FirstGame/graphics/ground.png').convert()

score_surf = test_font.render('First Game', False, (64, 64, 64))
score_rect = score_surf.get_rect(center = (400, 50))

snail_surf = pygame.image.load('./FirstGame/graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(midbottom = (600, 300))

player_surf = pygame.image.load('./FirstGame/graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #if event.type == pygame.MOUSEMOTION:
        #    if player_rect.collidepoint(event.pos): print('Collision')
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_SPACE: 
                print('Jump')
        if event.type == pygame.KEYUP: print('Key Up')

    screen.blit(sky_surf, (0, 0))
    screen.blit(ground_surf, (0, 300))
    
    pygame.draw.rect(screen, '#c0e8ec', score_rect)#Width
    pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
    screen.blit(score_surf, score_rect)
    
    snail_rect.x -=4
    if(snail_rect.right <= 0): 
        snail_rect.left = 800  
    screen.blit(snail_surf, snail_rect)  
    
    screen.blit(player_surf, player_rect)
    
    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]: 
    #   print('jump')

    #if player_rect.colliderect(snail_rect): 
    #    print('Collision')
        
    #mouse_position = pygame.mouse.get_pos()
    #if player_rect.collidepoint((mouse_position)): 
    #   print(pygame.mouse.get_pressed())
        
    #Draw all elements & Update everything
    pygame.display.update()
    clock.tick(60)