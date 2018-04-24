import pygame as pygame
import time
import random

pygame.init()


display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

pug_width = 125

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Pug-ey')
clock = pygame.time.Clock()

pug_img = pygame.image.load("pug.jpeg")
nightmare_img_left = pygame.image.load("nightmare.png")
nightmare_img_right = pygame.image.load("nightmare2.png")


def things(thing_x,thing_y,thing_w,thing_h, color):
    if thing_x > display_width//2 - 150:
        gameDisplay.blit(nightmare_img_left,(thing_x,thing_y))
    else:
        gameDisplay.blit(nightmare_img_right,(thing_x,thing_y))
def pug(x,y):
    gameDisplay.blit(pug_img,(x,y))

def text_objects(text, font):
    text_surface = font.render(text, True, black)
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

def game_loop():

    x = (display_width * 0.40)
    y = (display_height * 0.8)

    x_change = 0
    thing_start_x = random.randrange(0,display_width)
    thing_start_y = -1000
    thing_speed = 7
    thing_width = 300
    thing_height = 300

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
        things(thing_start_x,thing_start_y,thing_width,thing_height,black)
        thing_start_y += thing_speed
        pug(x,y)

        if x > display_width - pug_width or x < -20:
            crash()
        
        if thing_start_y > display_height:
            thing_start_y = 0- thing_height
            thing_start_x = random.randrange(0,display_width)


        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
