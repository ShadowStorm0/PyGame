import pygame
from sys import exit
from random import randint

def display_Score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time 
    score_surf = test_font.render(f'Score: {current_time}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center = (400, 50))
    screen.blit(score_surf, score_rect)
    return current_time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5
                   
            if obstacle_rect.bottom == 300: screen.blit(snail_surf, obstacle_rect) #Display snail if on 300 (y ground)
            else: screen.blit(fly_surf, obstacle_rect) #Else Fly

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100] #Delete Rectangle off Screen
        
        return obstacle_list
    else: return []
    
def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect): return False
    return True
                
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('First Game')
clock = pygame.time.Clock()
test_font = pygame.font.Font('./FirstGame/font/Pixeltype.ttf', 50)
game_active = False
start_time = 0
score = 0

#Background
sky_surf = pygame.image.load('./FirstGame/graphics/Sky.png').convert()
ground_surf = pygame.image.load('./FirstGame/graphics/ground.png').convert()

# score_surf = test_font.render('First Game', False, (64, 64, 64))
# score_rect = score_surf.get_rect(center = (400, 50))

#Obstacles
snail_surf = pygame.image.load('./FirstGame/graphics/snail/snail1.png').convert_alpha()
fly_surf = pygame.image.load('./FirstGame/graphics/Fly/Fly1.png').convert_alpha()

obstacle_rect_list = []

#Player
player_surf = pygame.image.load('./FirstGame/graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80, 300))
player_gravity = 0

#Intro Screen
player_stand = pygame.image.load('./FirstGame/graphics/Player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2) #Angle, Zoom
player_stand_rect = player_stand.get_rect(center = (400, 200))

game_name = test_font.render('Pixel Runner', False, (111, 196, 169))
game_name_rect = game_name.get_rect(center = (400, 80))

game_message = test_font.render('Press space to run', False, (111, 196, 169))
game_message_rect = game_message.get_rect(center = (400, 320))

#Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:       #Jump on Floor
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300: 
                    player_gravity = -20
            if event.type == pygame.KEYDOWN:       #Jump on Floor
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300: 
                    player_gravity = -20
        else:
           if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
               game_active = True
               start_time = int(pygame.time.get_ticks() / 1000) #Resets time score
        if event.type == obstacle_timer and game_active:
            if randint(0, 2):
                obstacle_rect_list.append(snail_surf.get_rect(bottomright = (randint(900, 1100), 300)))
            else:
                obstacle_rect_list.append(fly_surf.get_rect(bottomright = (randint(900, 1100), 210)))

    #Game Loop
    if game_active:
        screen.blit(sky_surf, (0, 0))
        screen.blit(ground_surf, (0, 300))
        
        # pygame.draw.rect(screen, '#c0e8ec', score_rect)#Width
        # pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
        # screen.blit(score_surf, score_rect)
        score = display_Score()
        
        # snail_rect.x -=4
        # if(snail_rect.right <= 0): 
        #     snail_rect.left = 800  
        # screen.blit(snail_surf, snail_rect)  
        
        #Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300: #Floor
            player_rect.bottom = 300
        screen.blit(player_surf, player_rect)
        
        #Obstacle Movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)
        
        #Collision
        game_active = collisions(player_rect, obstacle_rect_list)
        
    #Start & Score Message
    else:
        screen.fill((94, 129, 162)) #Background Color
        screen.blit(player_stand, player_stand_rect)
        obstacle_rect_list.clear()
        player_rect.midbottom = (80, 300) #Reset Player Position
        player_gravity = 0 #Reset Player Gravity
        
        score_message = test_font.render(f'Your Score: {score}', False, (111, 196, 169))
        score_message_rect = score_message.get_rect(center = (400, 330))
        screen.blit(game_name, game_name_rect)
        
        if score == 0: screen.blit(game_message, game_message_rect)
        else: screen.blit(score_message, score_message_rect)

    #Draw all elements & Update everything
    pygame.display.update()
    clock.tick(60)