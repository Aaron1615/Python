import pygame
import random
import time 

pygame.init()
clock = pygame.time.Clock()
display_width = 800
display_height = 600


white = (255,255,255)
red = (255,0,0)

color1 = (random.randint(0,150),255,random.randint(0,150))
color2 = (random.randint(150,255),random.randint(150,255),random.randint(0,255))
color3 = (random.randint(0,255),random.randint(0,255),255)
color4 = (random.randint(0,255),random.randint(150,255),random.randint(0,255))
color5 = (255,random.randint(0,255),random.randint(0,255))
color6 = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

gameDisplay = pygame.display.set_mode((display_width,display_height))



def game_loop():

    gameExit = False
    gameDisplay.fill(white)

    pygame.draw.circle(gameDisplay, red, (random.randint(0,800),random.randint(0,800)), random.randint(0,50))

    pygame.draw.polygon(gameDisplay, color5, ((random.randint(-100,800),random.randint(0,800)),(random.randint(0,800),random.randint(0,800)),(random.randint(0,500),random.randint(0,500)),(random.randint(0,500),random.randint(0,800)),(random.randint(0,800),random.randint(0,800))))
    pygame.draw.polygon(gameDisplay, color6, ((random.randint(-100,800),random.randint(0,800)),(random.randint(0,800),random.randint(0,800)),(random.randint(0,500),random.randint(0,500)),(random.randint(0,500),random.randint(0,800)),(random.randint(0,800),random.randint(0,800))))

   
    pygame.draw.polygon(gameDisplay, color4, ((random.randint(400,800),random.randint(400,800)),(random.randint(400,500),random.randint(400,800)),(random.randint(400,800),random.randint(400,800)),(random.randint(400,800),random.randint(0,800)),(random.randint(-100,800),random.randint(0,800))))
    
    pygame.draw.line(gameDisplay, color1, (random.randint(0,800),random.randint(-100,800)), (random.randint(0,800),random.randint(0,800)),random.randint(0,50))
    pygame.draw.circle(gameDisplay, color2, (random.randint(0,800),random.randint(0,200)), random.randint(50,200))
    
    
    pygame.display.update()

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()



game_loop()
pygame.quit()
quit()