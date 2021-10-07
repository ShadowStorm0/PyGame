import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('First Game')
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    #Draw all elements & Update everything
    pygame.display.update()
    clock.tick(60)