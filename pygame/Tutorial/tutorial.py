import pygame
import time
import random

pygame.init()


display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)

bright_green = (102,255,0)
bright_red = (255,0,0)

pug_width = 120

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Dreaming Pug')
clock = pygame.time.Clock()

pug_img = pygame.image.load("pug.jpeg")
nightmare_img_left = pygame.image.load("nightmare.png")
nightmare_img_right = pygame.image.load("nightmare2.png")

def nightmares_dodged(count):
    font = pygame.font.SysFont(None,25)
    text = font.render("Dodged: " + str(count), True, red)
    gameDisplay.blit(text,(0,0))

def nightmares(nightmare_x,nightmare_y,nightmare_w,nightmare_h, color):
    if nightmare_x > display_width//2 - 150:
        gameDisplay.blit(nightmare_img_left,(nightmare_x,nightmare_y))
    else:
        gameDisplay.blit(nightmare_img_right,(nightmare_x,nightmare_y))

def pug(x,y):
    gameDisplay.blit(pug_img,(x,y))

def text_objects(text, font):
    text_surface = font.render(text, True, red)
    return text_surface, text_surface.get_rect()

def text_object_white(text, font):
    text_surface = font.render(text, True, white)
    return text_surface, text_surface.get_rect()

def message_display(text):
    large_text = pygame.font.Font("freesansbold.ttf",80)
    text_surf, text_rect = text_objects(text, large_text)
    text_rect.center =((display_width/2),(display_height/2))
    gameDisplay.blit(text_surf, text_rect)

    pygame.display.update()

    time.sleep(2)
    


def crash():
    message_display("You woke the Pug!")
    game_loop()


def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x,y,w,h))

    small_text = pygame.font.Font("freesansbold.ttf",20)
    text_surf, text_rect = text_object_white(msg, small_text)
    text_rect.center =((x+(w/2)),(y+(h/2)))
    gameDisplay.blit(text_surf,text_rect)
    

def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        large_text = pygame.font.Font("freesansbold.ttf",115)
        text_surf, text_rect = text_objects("Dreaming Pug", large_text)
        text_rect.center =((display_width/2),(display_height/2))
        gameDisplay.blit(text_surf, text_rect)

        button("Go!",150,450,100,50,green,bright_green,game_loop)
        button("Quit",550,450,100,50,red,bright_red,quit)

        pygame.display.update()
        clock.tick(15)

def crash_nightmare():
    message_display("A Nightmare!")
    game_loop()


def game_loop():

    x = (display_width * 0.40)
    y = (display_height * 0.8)

    x_change = 0
    nightmare_start_x = random.randrange(0,display_width)
    nightmare_start_y = -1000
    nightmare_speed = 7
    nightmare_width = 260
    nightmare_height = 280

    dodged = 0

    game_exit = False

    while not game_exit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
    
        gameDisplay.fill(white)
        pug(x,y)
        nightmares(nightmare_start_x,nightmare_start_y,nightmare_width,nightmare_height,black)
        nightmare_start_y += nightmare_speed
        
        nightmares_dodged(dodged)

        if x > display_width - pug_width or x < -20:
            crash()
        
        if nightmare_start_y > display_height:
            nightmare_start_y = 0 - nightmare_height
            nightmare_start_x = random.randrange(0,display_width)
            dodged +=1
            nightmare_speed += .2

        if y < nightmare_start_y+nightmare_height:
            print("y crossover")

            if x > nightmare_start_x and x < nightmare_start_x + nightmare_width:
                print(x)
                print(nightmare_start_x)
                print(nightmare_start_x + nightmare_width)
                crash_nightmare()
            elif x + pug_width > nightmare_start_x and x + pug_width < nightmare_start_x + nightmare_width:
                print(x + pug_width)
                print(nightmare_start_x + nightmare_width)
                crash_nightmare()
                
        pygame.display.update()
        clock.tick(60)

game_intro()
pygame.quit()
quit()