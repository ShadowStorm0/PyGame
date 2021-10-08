import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('First Game')
clock = pygame.time.Clock()
test_font = pygame.font.Font('./FirstGame/font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('./FirstGame/graphics/Sky.png')
ground_surface = pygame.image.load('./FirstGame/graphics/ground.png')
text_surface = test_font.render('First Game', False, 'Red')

snail_surface = pygame.image.load('./FirstGame/graphics/snail/snail1.png')
snail_x_pos = 600

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 50))
    
    snail_x_pos -= 4
    if snail_x_pos < -100:
        snail_x_pos = 800
    screen.blit(snail_surface, (snail_x_pos, 250))

    #Draw all elements & Update everything
    pygame.display.update()
    clock.tick(60)