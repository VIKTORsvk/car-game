import pygame, sys, math
from pygame.locals import *
pygame.init()

################################################################### settings
bg = (255, 255, 255)
game_width = 1440
game_height = 880
screen = pygame.display.set_mode((game_width,game_height ))
#screen = pygame.display.set_mode((game_width, game_height), pygame.FULLSCREEN)
pygame.display.set_caption("Racing game")
screen.fill(bg)

menu_font = pygame.font.SysFont("arial", 35)
menu_text_1 = menu_font.render("START", True, (255, 255, 255))
menu_text_2 = menu_font.render("ABOUT", True, (255, 255, 255))                              
menu_text_3 = menu_font.render("QUIT", True, (255, 255, 255))
about_text_1 = menu_font.render("PLAYER_1  = UP,DOWN,LEFT,RIGHT", True, (255, 255, 255))
about_text_2 = menu_font.render("PLAYER_2  = A,W,S,D", True, (255, 255, 255))
about_text_3 = menu_font.render("VIKTOR ADAMEC", True, (255, 255, 255))
menu_image = pygame.image.load("menuimage.jpg")

color_road = (100, 100, 100)
color_blockade  = (0, 0, 1)
color_finish = (255, 255, 5)

maps = []
loadmap = 1
map_counter = 1
map_number = 0

menu = True
about = False
####################################################################### maps
while loadmap == 1:    
    try:
        exec("maps.append(pygame.image.load('mapy/track_" + str(map_counter) + ".png'))")
    except:
        loadmap = 0
    map_counter += 1

###################################################################### car settings
# player 1
player_1 = pygame.Rect(100, 800, 20, 20)
car_img1 = pygame.image.load("auto_1.png")

forward_1 = False
left_1 = False
right_1 = False
backward_l = False

speed_1 = 0
angle_1 = 0
finish_1 = 0
start_1 = 0

# player 2
player_2 = pygame.Rect(100, 830, 20, 20)
car_img2 = pygame.image.load("auto_2.png")

forward_2 = False
left_2 = False
right_2 = False
backward_2 = False

speed_2 = 0
angle_2 = 0
finish_2 = 0
start_2 = 0

# car speed and turn
max_speed = 10
angle_turn = 4 

clock = pygame.time.Clock()
fps = 50
time_ = 0


###################################################################### game
running = 1
while running == 1:
    if start_1 == 1:
        player_1.x = 100
        player_1.y = 800

    if start_2 == 1:
        player_2.x = 100
        player_2.y = 830
        

# player 1
    if start_1 == 0:
        if forward_1 == True and speed_1 < max_speed:
            speed_1 += 0.25
        if backward_l == True:
            speed_1 -= 0.25

        if left_1 == True and speed_1 > 2:
            angle_1 -= angle_turn
        elif left_1 == True and speed_1 < -2:
            angle_1 += angle_turn
        
        if right_1 == True and speed_1 > 2:
            angle_1 += angle_turn
        elif right_1 == True and speed_1 < -2:
            angle_1 -= angle_turn

        if forward_1 == False and speed_1 > 0:
            speed_1 -= 0.25
        if backward_l == False and speed_1 < 0:
            speed_1 += 0.25


        car_1a = math.cos(math.radians(angle_1)) * speed_1 
        car_1b = math.sin(math.radians(angle_1)) * speed_1
        player_1.x += round(car_1a)
        player_1.y += round(car_1b)

        car_img1_1 = pygame.transform.rotate(car_img1, angle_1*-1)

    else:
        start_1 -= 1

# player 2
    if start_2 == 0:
        if forward_2 == True and speed_2 < max_speed:
            speed_2 += 0.25
        if backward_2 == True:
            speed_2 -= 0.25

        if left_2 == True and speed_2 > 2:
            angle_2 -= angle_turn
        elif left_2 == True and speed_2 < -2:
            angle_2 += angle_turn
        
        if right_2 == True and speed_2 > 2:
            angle_2 += angle_turn
        elif right_2 == True and speed_2 < -2:
            angle_2 -= angle_turn


        if forward_2 == False and speed_2 > 0:
            speed_2 -= 0.25
        if backward_2 == False and speed_2 < 0:
            speed_2 += 0.25    

        car_2a = math.cos(math.radians(angle_2)) * speed_2 
        car_2b = math.sin(math.radians(angle_2)) * speed_2
        player_2.x += round(car_2a)
        player_2.y += round(car_2b)
        car_img2_2 = pygame.transform.rotate(car_img2, angle_2*-1)

    else:
        start_2 -=1
        
    mouse = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            #pygame.quit()
            running = 0
            #sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 100 <= mouse[0] <= 240 and game_height/2 <= mouse[1] <= game_height/2+40: 
                 menu= False
            if 100 <= mouse[0] <= 240 and game_height/2 +100 <= mouse[1] <= game_height/2+140: 
                 about = True
            if 100 <= mouse[0] <= 240 and game_height/2 +200 <= mouse[1] <= game_height/2+240: 
                 running = 0
        
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = 0
                
            if event.key == K_RETURN:
                map_number += 1
                player_1.x = 100
                player_1.y = 800
                angle_1 = 0

                player_2.x = 100
                player_2.y = 830
                angle_2 = 0
                
                if map_number >= len(maps):
                    map_number = 0                    
                
            if event.key == K_UP:
                forward_1 = True
            if event.key == K_LEFT:
                left_1 = True
            if event.key == K_RIGHT:
                right_1 = True
            if event.key == K_DOWN:
                backward_l = True

            if event.key == K_w:
                forward_2 = True
            if event.key == K_a:
                left_2 = True
            if event.key == K_d:
                right_2 = True
            if event.key == K_s:
                backward_2 = True


        if event.type == KEYUP:
            if event.key == K_UP:
                forward_1 = False
            if event.key == K_LEFT:
                left_1 = False
            if event.key == K_RIGHT:
                right_1 = False
            if event.key == K_DOWN:
                backward_l = False

            if event.key == K_w:
                forward_2 = False
            if event.key == K_a:
                left_2 = False
            if event.key == K_d:
                right_2 = False
            if event.key == K_s:
                backward_2 = False

    screen.fill((0, 0, 0))
    screen.blit(maps[map_number], (0, 0))

    if start_1 == 0:
        try:
            if not screen.get_at((player_1.x + 10, player_1.y + 10)) == color_road:
  
                if speed_1 > 3:
                    speed_1 = 2
                if speed_1 < -3:
                    speed_1 = -2

            if screen.get_at((player_1.x + 10, player_1.y + 10)) == color_blockade:
                if speed_1 > 0:
                    speed_1 = -1


            if screen.get_at((player_1.x + 10, player_1.y + 10)) == color_finish:
                finish_1 = 1
                map_number += 1
            
        except:
            finish_1 = 1

        if finish_1 == 0:
            screen.blit(car_img1_1, player_1)

    else:
        screen.blit(car_img1_1, player_1)


#  2 
    if start_2 == 0:
        try:
            if not screen.get_at((player_2.x + 10, player_2.y + 10)) == color_road:
                if speed_2 > 3: 
                    speed_2 = 2
                if speed_2 < -3:
                    speed_2 = -2


            if screen.get_at((player_2.x + 10, player_2.y + 10)) == color_blockade:
                if speed_2 > 0:
                    speed_2 = -1
                    
            if screen.get_at((player_2.x + 10, player_2.y + 10)) == color_finish:
                finish_2 = 1
                map_number += 1

        except:
            finish_2 = 1
    
        if finish_2 == 0:
            screen.blit(car_img2_2, player_2)

    else:
        screen.blit(car_img2_2, player_2)


    if finish_1 == 1:
        screen.blit(car_img1_1, player_1)
        screen.blit(car_img2_2, player_2)
        pygame.display.update()
        finish_1 = 0
        angle_1 = 0
        finish_2 = 0
        angle_2 = 0
        speed_1= 0
        speed_2= 0
        start_1 = 1
        start_2 = 1
        

    if finish_2 == 1:
        screen.blit(car_img1_1, player_1)
        screen.blit(car_img2_2, player_2)
        pygame.display.update()
        finish_1 = 0
        angle_1 = 0
        finish_2 = 0
        angle_2 = 0
        speed_1= 0
        speed_2= 0
        start_1 = 1
        start_2 = 1

    if menu == True:
        pygame.draw.rect(screen,(0,0,0),[0 ,830,1600,50])
        screen.blit(menu_image, (0,0))
        pygame.draw.rect(screen,(0,0,0),[100 ,game_height/2,140,40])
        pygame.draw.rect(screen,(0,0,0),[100,game_height/2 +100,140,40])
        pygame.draw.rect(screen,(0,0,0),[100,game_height/2 +200,140,40])
        screen.blit(menu_text_1 , (125,game_height/2))
        screen.blit(menu_text_2 , (125,game_height/2+100))
        screen.blit(menu_text_3 , (135,game_height/2+200))
        if about == True:
            pygame.draw.rect(screen,(0,0,0),[850 ,300,550,400])
            screen.blit(about_text_1 , (900,350))
            screen.blit(about_text_2 , (900,400))
            screen.blit(about_text_3 , (900,600))
            
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
