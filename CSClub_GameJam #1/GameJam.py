#By: ShadowStorm0 / Python47
#Theme: Scale (Weight or Amount of enemies)

from random import randint, choice
import pygame, secrets, sys
from pygame.constants import *
from pygame.time import Clock

def main():
    # Spirtes
    class Player(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            
            player_walk_1 = pygame.image.load('./graphics/Player/player_walk_1.png').convert_alpha()
            player_walk_2 = pygame.image.load('./graphics/Player/player_walk_2.png').convert_alpha()
            self.player_walk = [player_walk_1, player_walk_2]
            self.player_index = 0
            self.player_jump = pygame.image.load('./graphics/Player/jump.png').convert_alpha()
            
            self.image = self.player_walk[self.player_index]
            self.rect = self.image.get_rect(midbottom = (80, 300)) 
            self.gravity = 0
            
            self.jump_sound = pygame.mixer.Sound('./audio/jump.wav')
            self.jump_sound.set_volume(5)

        def player_input(self):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
                self.gravity = -20
                self.jump_sound.play()
        
        def apply_gravity(self):
            self.gravity += 1
            self.rect.y += self.gravity
            if self.rect.bottom >= 300: self.rect.bottom = 300 # Floor
        
        def animation_state(self):        
            # Display walking animation when player is on floor
            # Display the jump surface when player is not on floor
            if self.rect.bottom < 300: # Check if player is not on ground
                self.image = self.player_jump # Jumping animation
            else:
                self.player_index += 0.1
                if self.player_index >= len(self.player_walk): 
                    self.player_index = 0 # loop back to 0 when reaches 1 [Restart Animation]
                self.image = self.player_walk[int(self.player_index)] # Player walking animation
        
        def update(self):
            self.player_input()
            self.apply_gravity()
            self.animation_state()
    class Enemies(pygame.sprite.Sprite):
        def __init__(self, type):
            super().__init__()
            
            if type == 'slime':
                slime_1 = pygame.image.load('./graphics/Slime/slime-move-0.png').convert_alpha()
                slime_2 = pygame.image.load('./graphics/Slime/slime-move-1.png').convert_alpha()
                slime_3 = pygame.image.load('./graphics/Slime/slime-move-2.png').convert_alpha()
                slime_4 = pygame.image.load('./graphics/Slime/slime-move-3.png').convert_alpha()
                self.frames = [slime_1, slime_2, slime_3, slime_4] # Animation list
                y_pos = 300
                
            elif type == 'snail':
                snail_1 = pygame.image.load('./graphics/Snail/snail1.png').convert_alpha()
                snail_2 = pygame.image.load('./graphics/Snail/snail2.png').convert_alpha()
                self.frames = [snail_1, snail_2] # Animation list 
                y_pos = 300
                
            elif type == 'fly':
                fly_1 = pygame.image.load('./graphics/Fly/Fly1.png').convert_alpha()
                fly_2 = pygame.image.load('./graphics/Fly/Fly2.png').convert_alpha()
                self.frames = [fly_1, fly_2] # Animation list
                y_pos = 210 
                
            else:
                blank = pygame.image.load('./graphics/blank.png').convert_alpha()
                self.frames = [blank]
                y_pos = 0
            
            self.animation_index = 0
            self.image = self.frames[self.animation_index]
            self.rect = self.image.get_rect(midbottom = (randint(900, 1100), y_pos))

        def animation_state(self): 
            self.animation_index += 0.1
            if self.animation_index >= len(self.frames): 
                self.animation_index = 0
            self.image = self.frames[int(self.animation_index)]
            
        def update(self):
            self.animation_state()
            self.rect.x -= 6
            self.destroy()
            
        def destroy(self):
            if self.rect.x <= -100: self.kill()

    # Methods
    def draw_text(text, font, color, surface, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft  = (x, y)
        surface.blit(textobj, textrect)
    
    # def display_Score():
    #     current_time = int(pygame.time.get_ticks() / 1000) - start_time 
    #     score_surf = game_font.render(f'Score: {current_time}', False, (64, 64, 64))
    #     score_rect = score_surf.get_rect(center = (400, 50))
    #     screen.blit(score_surf, score_rect)
    #     return current_time

    def level():
            level_message = game_font.render(f'Your Level: {level}', False, (111, 196, 169))
            level_message_rect = level_message.get_rect(center = (400, 330))
            screen.blit(level_message, level_message_rect)# Start screen title
            return level

    def collision_sprite():
        if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
            #obstacle_group.empty()
            return False
        else: 
            return True
    
    # Starting PyGame
    pygame.init()
    Clock = pygame.time.Clock()
    screen = pygame.display.set_mode((800, 400))
    pygame.display.set_caption('Crushing Scales')
    game_font = pygame.font.Font('./font/ThaleahFat.ttf', 50)
    background_music = pygame.mixer.Sound('./audio/music.wav')
    background_music.play(loops = -1)
    width = screen.get_width()
    height = screen.get_height()

    # Groups
    player = pygame.sprite.GroupSingle()
    player.add(Player())
    obstacle_group = pygame.sprite.Group()

    # Background
    sky_surf = pygame.image.load('./graphics/Sky.png').convert_alpha()
    ground_surf = pygame.image.load('./graphics/ground.png').convert_alpha()
    
    # Intro Screen
    player_stand = pygame.image.load('./graphics/Player/player_stand.png').convert_alpha()
    player_stand = pygame.transform.rotozoom(player_stand, 0, 2) #Angle, Zoom
    player_stand_rect = player_stand.get_rect(center = (400, 270))
    
    over_player_stand = pygame.image.load('./graphics/Player/player_stand.png').convert_alpha()
    over_player_stand = pygame.transform.rotozoom(over_player_stand, 0, 2) #Angle, Zoom
    over_player_stand_rect = over_player_stand.get_rect(center = (400, 200))

    game_name = game_font.render('Pixel Runner', False, (111, 196, 169))
    game_name_rect = game_name.get_rect(center = (400, 70))

    game_name = game_font.render('Pixel Runner', False, (111, 196, 169))
    game_name_rect = game_name.get_rect(center = (400, 70))

    over_game_message = game_font.render('Press space to restart', False, (111, 196, 169))
    over_game_message_rect = over_game_message.get_rect(center = (400, 300))
    
    start_game_message = game_font.render('Press space to run', False, (111, 196, 169))
    start_game_message_rect = start_game_message.get_rect(center = (400, 150))

    # Timer(s)
    obstacle_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(obstacle_timer, 1500)

    snail_animation_timer = pygame.USEREVENT + 2
    pygame.time.set_timer(snail_animation_timer, 300)

    fly_animation_timer = pygame.USEREVENT + 3
    pygame.time.set_timer(fly_animation_timer, 200)
    
    slime_animation_timer = pygame.USEREVENT + 4
    pygame.time.set_timer(slime_animation_timer, 500)
               
    def main_menu():
        click = False
        while True:
            screen.fill((94, 129, 162))
            draw_text('Main Menu', game_font, (255, 255, 255), screen, 300, 10)
              
            mx, my = pygame.mouse.get_pos()
                            
            button_1 = pygame.Rect(300, 100, 200, 50)
            button_2 = pygame.Rect(300, 200, 200, 50)
            button_3 = pygame.Rect(300, 300, 200, 50)
            
            if button_1.collidepoint((mx, my)):
                if click:
                    game()
            if button_2.collidepoint((mx, my)):
                if click:
                    options()
            if button_3.collidepoint((mx, my)):
                if click:
                    quit()
                    
            pygame.draw.rect(screen, (255, 0, 0), button_1)
            pygame.draw.rect(screen, (255, 0, 0), button_2)
            pygame.draw.rect(screen, (255, 0, 0), button_3)
            draw_text('Start Game', game_font, (255, 255, 255), screen, 280, 100)
            draw_text('Options', game_font, (255, 255, 255), screen, 320, 200)
            draw_text('Quit', game_font, (255, 255, 255), screen, 350, 300)

            click = False
            for event in pygame.event.get():
                # Exits program with X button
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                                    
                # Exits with escape button
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                                
                # Click event
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True       
                    
            # Draw all elements and update everything
            pygame.display.update()
            Clock.tick(60)            

    def game():
        level_count = 1
        lives = 3
        game_active = False
        running = True
        enemies_counter = 10
        enemies = 10
        level_left = 10
        current_level = 0
        
        while running:
            screen.fill((0, 0, 0))
            screen.blit(start_game_message, start_game_message_rect)
            screen.blit(player_stand, player_stand_rect)
            screen.blit(game_name, game_name_rect)
            
            for event in pygame.event.get():
                # Exits program with X button
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                                  
                # Exits with escape button
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pause()

                # Start / Restart Game
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: 
                    game_active = True 

                # Selects one in the list to draw
                if game_active:
                    if event.type == obstacle_timer:
                        obstacle_group.add(Enemies(choice(['fly', 'snail', 'slime', 'blank'])))
                        enemies_counter -= 1;

            # Game Loop
            if game_active:  
                # Sky and Ground and 
                screen.blit(sky_surf, (0, 0))
                screen.blit(ground_surf, (0, 300))
                
                enemies_left_surf = game_font.render(f'Enemies Left: {enemies}', False, (64, 64, 64))
                enemies_left_rect = enemies_left_surf.get_rect(center = (400, 150))
                screen.blit(enemies_left_surf, enemies_left_rect)

                # if (enemies < 1):
                #     current_level += 1
                #     enemies -= 1
                level_surf = game_font.render(f'Level: {level}', False, (64, 64, 64))
                level_rect = level_surf.get_rect(center = (400, 50))
                screen.blit(level_surf, level_rect)

                if(enemies < 1):
                    level_left -= 1
                    enemies -=1
                level_left_surf = game_font.render(f'Levels Left: {level_left}', False, (64, 64, 64))
                level_left_rect = level_left_surf.get_rect(center = (400, 100))
                screen.blit(level_left_surf, level_left_rect)

                # level_left_message = game_font.render(f'Levels Left: {left}', False, (111, 196, 169))
                # level_left_message_rect = level_left_message.get_rect(center = (400, 100))
                # screen.blit(level_left_message, level_left_message_rect)
                
                # Player
                player.draw(screen)
                player.update()
                
                # Enemies
                obstacle_group.draw(screen)
                obstacle_group.update()
                enemies -= 1
                
                # # Collision (True / False)
                # game_active = collision_sprite() 
                
                if enemies_counter == 0:
                    level_count += 1;
                    enemies_counter = 10
                    
                if level_count == 10:
                    game_over()

                if collision_sprite() == False:
                    lives -= 1
                    game_active = False
                    if lives < 1:
                        #game_active = False
                        game_over()
            
            # Draw all elements and update everything
            pygame.display.update()
            Clock.tick(60)
                            
    def options():
        running = True
        while running:
            screen.fill((0, 0, 0))
            draw_text('Options', game_font, (255, 255, 255), screen, 400, 200)
            for event in pygame.event.get():
                # Exits program with X button
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                     
                # Exits with escape button
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                                        
            # Draw all elements and update everything
            pygame.display.update()
            Clock.tick(60)
            
    def pause():
        running = False
        while running:
            screen.fill((0, 0, 0))
            draw_text('Pause', game_font, (255, 255, 255), screen, 400, 200)
            for event in pygame.event.get():
                # Exits program with X button
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                                
                # Exits with escape button
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
             
            # Draw all elements and update everything
            pygame.display.update()
            Clock.tick(60)
        
    def game_over():
        obstacle_group.empty()
        while True:
            screen.fill((0, 0, 0))
            draw_text('Game Over', game_font, (255, 255, 255), screen, 400, 400)
            for event in pygame.event.get():
                # Exits program with X button
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                                
                # Exits with escape button
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    main_menu();
                   
            screen.fill((94, 129, 162)) # Background Color
            screen.blit(over_player_stand, over_player_stand_rect) # Displays start player model
            #start_time = int(pygame.time.get_ticks() / 1000) # Resets time score
            player_gravity = 0 # Reset player gravity
                
            # Game Over Message
            game_over_message = game_font.render('Game Over', True, (255, 255, 255))
            game_over_message_rect = game_over_message.get_rect(center = (400, 100))
            screen.blit(game_over_message, game_over_message_rect)
             
            screen.blit(over_game_message, over_game_message_rect)
            
            # Game over score                                    # AA        RBG
            level_over_message = game_font.render(f'Your Level: {level}', False, (111, 196, 169))
            level_over_message_rect = level_over_message.get_rect(center = (400, 330))
            screen.blit(game_name, game_name_rect)# Start screen title
  
            # Logic to if display score on start screen
            if level == 0: screen.blit(game_over_message, game_over_message_rect) # 'Press space to run' Message
            else: screen.blit(level_over_message, level_over_message_rect)   
                                           
            # Draw all elements and update everything
            pygame.display.update()
            Clock.tick(60)
               
    def quit():
        running = True
        while running:
            pygame.quit()
            sys.exit()
           
    #Runs Main Menu             
    main_menu()   
                
if __name__ == '__main__':
    main()
else: 
    print("Do Not Import!\n")
    sys.exit()