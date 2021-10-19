#By: ShadowStorm0 / Python47
#Theme: Scale

import pygame, random, secrets, sys
from pygame.constants import *

def main():
    # Starting PyGame
    pygame.init()
    screen = pygame.display.set_mode((800, 400))
    pygame.display.set_caption('Expanding Space')
    clock = pygame.time.Clock()
    game_font = pygame.font.Font('./font/ThaleahFat.ttf', 50)
    game_active = False

    while True:
        for event in pygame.event.get():
            # Exits program with X button
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            # Exits with escape button
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    exit()

  
if __name__ == '__main__':
    main()
else: 
    print("Do Not Import\n")
    exit()