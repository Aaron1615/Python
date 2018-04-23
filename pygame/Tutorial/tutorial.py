import pygame as pygame
import time

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

        if x > display_width - pug_width or x < -20:
            crash()


        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
