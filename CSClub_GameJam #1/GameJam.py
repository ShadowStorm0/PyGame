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

    # Groups
    
    # Background(s)
    
    # Intro screen
    
    # Timers

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
                    
            # Start and restart game
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True

        #Obstacle selection (use secrets)


        if game_active:
            screen.fill((0,0,255))
            # Draw Sky, and Ground
            
            # Draw Player
            
            # Draw Obstacle(s)
            
            # Collision with Obstacle(s)
        else:
            screen.fill((94, 129, 162))
            
        
        # Draw all elements and update everything
        pygame.display.update()
        clock.tick(60)
            
if __name__ == '__main__':
    main()
else: 
    print("Do Not Import\n")
    exit()