import pygame
from sys import exit
from pygame.locals import *
from random import randint, choice

def main():
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
                if self.player_index >= len(self.player_walk): self.player_index = 0 # loop back to 0 when reaches 1 [Restart Animation]
                self.image = self.player_walk[int(self.player_index)] # Player walking animation
        
        def update(self):
            self.player_input()
            self.apply_gravity()
            self.animation_state()

    class Obstacle(pygame.sprite.Sprite):
        def __init__(self, type):
            super().__init__()
            
            if type == 'fly':
                fly_1 = pygame.image.load('./graphics/Fly/Fly1.png').convert_alpha()
                fly_2 = pygame.image.load('./graphics/Fly/Fly2.png').convert_alpha()
                self.frames = [fly_1, fly_2]# Animation list
                y_pos = 210
            elif type == 'snail':
                snail_1 = pygame.image.load('./graphics/snail/snail1.png').convert_alpha()
                snail_2 = pygame.image.load('./graphics/snail/snail2.png').convert_alpha()
                self.frames = [snail_1, snail_2]# Animation list 
                y_pos = 300
            elif type == 'blank':
                nothing = pygame.image.load('./graphics/blank.png').convert_alpha()
                self.frames = [nothing]
                y_pos = 0
            
            self.animation_index = 0
            self.image = self.frames[self.animation_index]
            self.rect = self.image.get_rect(midbottom = (randint(900, 1100), y_pos))

        def animation_state(self): 
            self.animation_index += 0.1
            if self.animation_index >= len(self.frames): self.animation_index = 0
            self.image = self.frames[int(self.animation_index)]
            
        def update(self):
            self.animation_state()
            self.rect.x -= 6
            self.destroy()
            
        def destroy(self):
            if self.rect.x <= -100: self.kill()

    def display_Score():
        current_time = int(pygame.time.get_ticks() / 1000) - start_time 
        score_surf = test_font.render(f'Score: {current_time}', False, (64, 64, 64))
        score_rect = score_surf.get_rect(center = (400, 50))
        screen.blit(score_surf, score_rect)
        return current_time

    def collision_sprite():
        if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
            obstacle_group.empty()
            return False
        else: return True
        
    # Starting PyGame  
    pygame.init()
    monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]
    screen = pygame.display.set_mode((800, 400), pygame.RESIZABLE)
    pygame.display.set_caption('First Game')
    clock = pygame.time.Clock()
    test_font = pygame.font.Font('./font/Pixeltype.ttf', 50)
    game_active = False
    start_time = 0
    score = 0
    background_music = pygame.mixer.Sound('./audio/music.wav')
    background_music.play(loops = -1)
    fullscreen = False

    # Groups
    player = pygame.sprite.GroupSingle()
    player.add(Player())
    obstacle_group  = pygame.sprite.Group()

    # Background
    sky_surf = pygame.image.load('./graphics/Sky.png').convert()
    ground_surf = pygame.image.load('./graphics/ground.png').convert()

    # Intro Screen
    player_stand = pygame.image.load('./graphics/Player/player_stand.png').convert_alpha()
    player_stand = pygame.transform.rotozoom(player_stand, 0, 2) #Angle, Zoom
    player_stand_rect = player_stand.get_rect(center = (400, 200))

    game_name = test_font.render('Pixel Runner', False, (111, 196, 169))
    game_name_rect = game_name.get_rect(center = (400, 80))

    game_message = test_font.render('Press space to run', False, (111, 196, 169))
    game_message_rect = game_message.get_rect(center = (400, 320))

    # Timer(s)
    obstacle_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(obstacle_timer, 1500)

    snail_animation_timer = pygame.USEREVENT + 2
    pygame.time.set_timer(snail_animation_timer, 500)

    fly_animation_timer = pygame.USEREVENT + 3
    pygame.time.set_timer(fly_animation_timer, 200)

    while True:         
        for event in pygame.event.get():
            # Closes by 'X' button
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

#            Window resize
            if event.type == WINDOWRESIZED:
                if not FULLSCREEN:
                    screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

            # Closes by escape button
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    pygame.exit
                    
                if event.key == K_f:
                    fullscreen = not fullscreen
                    if fullscreen:
                        screen = pygame.display.set_mode(monitor_size, pygame.FULLSCREEN)
                    else:
                        screen = pygame.display.set_mode((screen.get_width(), screen.get_height()), pygame.RESIZABLE)
                    
            # Start / Restart Game
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: game_active = True
            
            # Selects one in the list to draw
            if game_active:
                if event.type == obstacle_timer:
                    obstacle_group.add(Obstacle(choice(['fly', 'snail', 'snail', 'blank'])))

        # Game Loop
        if game_active:
            # Sky, Ground & Score
            screen.blit(sky_surf, (0, 0))
            screen.blit(ground_surf, (0, 300))
            score = display_Score()
            
            # Player
            player.draw(screen)
            player.update()
            
            # Obstacle(s)
            obstacle_group.draw(screen)
            obstacle_group.update()
            
            # Collision (True / False)
            game_active = collision_sprite()
            
        # Start & Score Message (Start Screen & Game Over)
        else:
            screen.fill((94, 129, 162)) # Background Color
            screen.blit(player_stand, player_stand_rect) # Displays start player model
            start_time = int(pygame.time.get_ticks() / 1000) # Resets time score
            player_gravity = 0 # Reset player gravity
             
            # Game over score                                                       # AA        RBG
            score_message = test_font.render(f'Your Score: {score}', False, (111, 196, 169))
            score_message_rect = score_message.get_rect(center = (400, 330))
            screen.blit(game_name, game_name_rect)# Start screen title
            
            # Logic to if display score on start screen
            if score == 0: screen.blit(game_message, game_message_rect) # 'Press space to run' Message
            else: screen.blit(score_message, score_message_rect)

        # Draw all elements & Update everything
        pygame.display.update()
        clock.tick(60)

#Check if not an import
if __name__ == '__main__':
    main()
else: 
    print("Do Not Import\n")
    exit()