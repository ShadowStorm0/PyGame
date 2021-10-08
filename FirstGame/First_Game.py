import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('First Game')
clock = pygame.time.Clock()
test_font = pygame.font.Font('./FirstGame/font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('./FirstGame/graphics/Sky.png').convert()
ground_surface = pygame.image.load('./FirstGame/graphics/ground.png').convert()
text_surface = test_font.render('First Game', False, 'Red')

snail_surface = pygame.image.load('./FirstGame/graphics/snail/snail1.png').convert_alpha()
snail_rectangle = snail_surface.get_rect(midbottom = (600, 300))

player_surface = pygame.image.load('./FirstGame/graphics/Player/player_walk_1.png').convert_alpha()
player_rectangle = player_surface.get_rect(midbottom = (80, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 50))
    
    snail_rectangle.x -=4
    if(snail_rectangle.right <= 0): snail_rectangle.left = 800
    screen.blit(snail_surface, snail_rectangle)
    player_rectangle.left += 1
    screen.blit(player_surface, player_rectangle)

    #Draw all elements & Update everything
    pygame.display.update()
    clock.tick(60)