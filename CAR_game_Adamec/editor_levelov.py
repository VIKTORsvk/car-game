import pygame, sys, os
from pygame.locals import *

screen = pygame.display.set_mode((1540, 880))

GREEN = (0, 255, 0)
Menu = (255, 255, 255)
GRAY1 = (100, 100, 100)
BLACK = (0, 0, 1)
RED = (255, 5, 5)
BLUE = (0, 0, 255)
DARK_GRAY = (120, 120, 99)
PINK = (249, 57, 255)
YELLOW = (255, 255, 5)
DARK_GREEN = (58, 158, 73)
WHITE = (255, 255, 255)
DARK_BROWN = (51, 51, 0)
DARK_GREEN_1 = (25, 51, 0)
DARK_GREEN_2 = (0, 51, 0)
DARK_GREEN_3 = (0, 51, 51)
DARK_ORANGE = (102, 51, 0)

pygame.init()
menu_font = pygame.font.SysFont("arial", 17)
clear_text = menu_font.render("  Clear", True, BLACK)
save_text = menu_font.render("  SAVE", True, BLACK)

brush1= menu_font.render("1", True, BLACK)
brush2= menu_font.render("2", True, BLACK)
brush3= menu_font.render("3", True, BLACK)
brush4= menu_font.render("4", True, BLACK)
brush5= menu_font.render("5", True, BLACK)
brush6= menu_font.render("6", True, BLACK)
brush7= menu_font.render("7", True, BLACK)
brush8= menu_font.render("8", True, BLACK)
brush9= menu_font.render("9", True, BLACK)
brush10= menu_font.render("10", True, BLACK)

draw = False
brush_size = 5
brush_color = GREEN


menu_rect = pygame.Rect(0, 0, 100, 880)
screen_rect = pygame.Rect(100, 0, 1450, 880)

###################
gray_rect = pygame.Rect(5, 55, 20, 20)
red_rect = pygame.Rect(27, 55, 20, 20)
blue_rect = pygame.Rect(49, 55, 20, 20)
pink_rect = pygame.Rect(71, 55, 20, 20)
yellow_rect = pygame.Rect(5, 77, 20, 20)
darkgreen1_rect = pygame.Rect(27, 77, 20, 20)
darkgreen2_rect = pygame.Rect(49, 77, 20, 20)
darkgreen3_rect = pygame.Rect(71, 77, 20, 20)
darkbrown_rect = pygame.Rect(5, 99, 20, 20)
darkorange_rect = pygame.Rect(27, 99, 20, 20)
white_rect = pygame.Rect(49, 99, 20, 20)
black_rect = pygame.Rect(71, 99, 20, 20)
#green_rect = pygame.Rect(5, 55, 20, 20)
clear_rect = pygame.Rect(10, 400, 70, 25)

brush_1 = pygame.Rect(5, 185, 20, 20)
brush_2 = pygame.Rect(27, 185, 20, 20)
brush_3 = pygame.Rect(49, 185, 20, 20)
brush_4 = pygame.Rect(71, 185, 20, 20)
brush_5 = pygame.Rect(5, 210, 20, 20)
brush_6 = pygame.Rect(27, 210, 20, 20)
brush_7 = pygame.Rect(49, 210, 20, 20)
brush_8 = pygame.Rect(71, 210, 20, 20)
brush_9 = pygame.Rect(5, 235, 20, 20)
brush_10 = pygame.Rect(27, 235, 20, 20)

save_rect = pygame.Rect(5, 450, 90, 25)
save = False
file_number = 1

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            draw = True
        if event.type == MOUSEBUTTONUP:
            draw = False

    mouse_pos = pygame.mouse.get_pos()
    if draw == True and mouse_pos[0] > 100 :
        pygame.draw.circle(screen, brush_color, mouse_pos, brush_size)
        save = False
  
    if draw == True:    
        if gray_rect.collidepoint(mouse_pos):
            brush_color = GRAY1
            
        if red_rect.collidepoint(mouse_pos):
            brush_color = RED
            
        if blue_rect.collidepoint(mouse_pos):
            brush_color = BLUE
            
        if pink_rect.collidepoint(mouse_pos):
            brush_color = PINK
            
        if yellow_rect.collidepoint(mouse_pos):
            brush_color = YELLOW
            
        if darkgreen1_rect.collidepoint(mouse_pos):
            brush_color = DARK_GREEN_1
            
        if darkgreen2_rect.collidepoint(mouse_pos):
            brush_color = DARK_GREEN_2
            
        if darkgreen3_rect.collidepoint(mouse_pos):
            brush_color = DARK_GREEN_3
            
        if darkbrown_rect.collidepoint(mouse_pos):
            brush_color = DARK_BROWN
            
        if darkorange_rect.collidepoint(mouse_pos):
            brush_color = DARK_ORANGE
            
        if white_rect.collidepoint(mouse_pos):
            brush_color = WHITE
            
        if black_rect.collidepoint(mouse_pos):
            brush_color = BLACK
            


    if draw == True:
        if clear_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, BLACK, screen_rect)
            
    pygame.draw.rect(screen, Menu, menu_rect)
    pygame.draw.line(screen, BLACK, (0, 40), (100, 40))
    pygame.draw.line(screen, BLACK, (0, 45), (100, 45))
    pygame.draw.rect(screen, DARK_GRAY, clear_rect)
    screen.blit(clear_text, (19, 403))
    pygame.draw.line(screen, BLACK, (0, 180), (100, 180))
    pygame.draw.rect(screen, DARK_GRAY, save_rect)
    screen.blit(save_text, (20, 453))

    if draw == True and save == False:
        if save_rect.collidepoint(mouse_pos):
            z= os.listdir('mapy/')
            print(" saved")
            save_surface = pygame.Surface((1450, 880))
            save_surface.blit(screen, (0, 0), (100, 0, 1450, 880))
            
            try:
                with open("mapy/track_" + str(len(z)) + ".png"):
                    print(" already saved")
                    file_number = file_number + 1
                    save = True
            except IOError:
                save = True
                
            pygame.image.save(save_surface, "mapy/track_" + str(len(z)+1) + ".png")
            
    if draw == True:
        if brush_1.collidepoint(mouse_pos):
            brush_size = 1
        if brush_2.collidepoint(mouse_pos):
            brush_size = 3
        if brush_3.collidepoint(mouse_pos):
            brush_size = 5
        if brush_4.collidepoint(mouse_pos):
            brush_size = 10
        if brush_5.collidepoint(mouse_pos):
            brush_size = 15
        if brush_6.collidepoint(mouse_pos):
            brush_size = 20
        if brush_7.collidepoint(mouse_pos):
            brush_size = 30
        if brush_8.collidepoint(mouse_pos):
            brush_size = 40
        if brush_9.collidepoint(mouse_pos):
            brush_size = 50
        if brush_10.collidepoint(mouse_pos):
            brush_size = 100


    
    

    pygame.draw.rect(screen, GRAY1, gray_rect)
    if brush_color == GRAY1:
        border = 3
    else:
        border = 1
    pygame.draw.rect(screen, BLACK, gray_rect, border)
    
    
    
    pygame.draw.rect(screen, RED, red_rect)
    if brush_color == RED:
        border = 3
    else:
        border = 1
    pygame.draw.rect(screen, BLACK, red_rect, border)
    
    
    
    pygame.draw.rect(screen, BLUE, blue_rect)
    if brush_color == BLUE:
        border = 3
    else:
        border = 1
    pygame.draw.rect(screen, BLACK, blue_rect, border)

    pygame.draw.rect(screen, PINK, pink_rect)
    if brush_color == PINK:
        border = 3
    else:
        border = 1
    pygame.draw.rect(screen, BLACK, pink_rect, border)



    pygame.draw.rect(screen, YELLOW, yellow_rect)
    if brush_color == YELLOW:
        border = 3
    else:
        border = 1
    pygame.draw.rect(screen, BLACK, yellow_rect, border)

    pygame.draw.rect(screen, DARK_GREEN_1, darkgreen1_rect)
    if brush_color == DARK_GREEN_1:
        border = 3
    else:
        border = 1
    pygame.draw.rect(screen, BLACK, darkgreen1_rect, border)

    pygame.draw.rect(screen, DARK_GREEN_2, darkgreen2_rect)
    if brush_color == DARK_GREEN_2:
        border = 3
    else:
        border = 1
    pygame.draw.rect(screen, BLACK, darkgreen2_rect, border)
    
    pygame.draw.rect(screen, DARK_GREEN_3, darkgreen3_rect)
    if brush_color == DARK_GREEN_3:
        border = 3
    else:
        border = 1
    pygame.draw.rect(screen, BLACK, darkgreen3_rect, border)
    
    pygame.draw.rect(screen, DARK_BROWN, darkbrown_rect)
    if brush_color == DARK_BROWN:
        border = 3
    else:
        border = 1
    pygame.draw.rect(screen, BLACK, darkbrown_rect, border)
    
    pygame.draw.rect(screen, DARK_ORANGE, darkorange_rect)
    if brush_color == DARK_ORANGE:
        border = 3
    else:
        border = 1
    pygame.draw.rect(screen, BLACK, darkorange_rect, border)
    
    pygame.draw.rect(screen, WHITE, white_rect)
    if brush_color == WHITE:
        border = 3
    else:
        border = 1
    pygame.draw.rect(screen, BLACK, white_rect, border)
    
    pygame.draw.rect(screen, BLACK, black_rect)
    if brush_color == BLACK:
        border = 3
    else:
        border = 1
    pygame.draw.rect(screen, BLACK, black_rect, border)
    
   
##    pygame.draw.rect(screen, GREEN, green_rect)
##    if brush_color == GREEN:
##        border = 3
##    else:
##        border = 1
##    pygame.draw.rect(screen, BLACK, green_rect, border)
##    
##        
    


    
    if brush_size == 1:
        brush_border = 3
    else:
        brush_border = 1
    pygame.draw.rect(screen, BLACK, brush_1, brush_border)
    pygame.draw.rect(screen, BLACK, brush_1, brush_border)
    screen.blit(brush1, (10,185))    
    
    if brush_size == 3:
        brush_border = 3
    else:
        brush_border = 1
    pygame.draw.rect(screen, BLACK, brush_2, brush_border)
    pygame.draw.rect(screen, BLACK, brush_2, brush_border)
    screen.blit(brush2, (32,185))   
    
    if brush_size == 5:
        brush_border = 3
    else:
        brush_border = 1
    pygame.draw.rect(screen, BLACK, brush_3, brush_border)
    pygame.draw.rect(screen, BLACK, brush_3, brush_border)
    screen.blit(brush3, (54,185))   
    
    if brush_size == 10:
        brush_border = 3
    else:
        brush_border = 1
    pygame.draw.rect(screen, BLACK, brush_4, brush_border)
    pygame.draw.rect(screen, BLACK, brush_4, brush_border)
    screen.blit(brush4, (76,185))   

    if brush_size == 15:
        brush_border = 3
    else:
        brush_border = 1
    pygame.draw.rect(screen, BLACK, brush_5, brush_border)
    pygame.draw.rect(screen, BLACK, brush_5, brush_border)
    screen.blit(brush5, (11,210))

    if brush_size == 20:
        brush_border = 3
    else:
        brush_border = 1
    pygame.draw.rect(screen, BLACK, brush_6, brush_border)
    pygame.draw.rect(screen, BLACK, brush_6, brush_border)
    screen.blit(brush6, (33,210))

    if brush_size == 30:
        brush_border = 3
    else:
        brush_border = 1
    pygame.draw.rect(screen, BLACK, brush_7, brush_border)
    pygame.draw.rect(screen, BLACK, brush_7, brush_border)
    screen.blit(brush7, (55,210))

    if brush_size == 40:
        brush_border = 3
    else:
        brush_border = 1
    pygame.draw.rect(screen, BLACK, brush_8, brush_border)
    pygame.draw.rect(screen, BLACK, brush_8, brush_border)
    screen.blit(brush8, (77,210))

    if brush_size == 50:
        brush_border = 3
    else:
        brush_border = 1
    pygame.draw.rect(screen, BLACK, brush_9, brush_border)
    pygame.draw.rect(screen, BLACK, brush_9, brush_border)
    screen.blit(brush9, (10,235))

    if brush_size == 100:
        brush_border = 3
    else:
        brush_border = 1
    pygame.draw.rect(screen, BLACK, brush_10, brush_border)
    pygame.draw.rect(screen, BLACK, brush_10, brush_border)
    screen.blit(brush10, (28,235))


    pygame.display.update()
