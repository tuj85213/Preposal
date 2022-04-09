#https://www.101computing.net/pong-tutorial-using-pygame-adding-the-paddles/

import pygame
pygame.init()
from paddle import Paddle

#background

blue = (100, 120, 200)
white = (255, 255, 255)

size = (500, 700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

#paddle

paddleA =Paddle(white, 10, 100)

##it says I have an error?? --> "pygame.sprite.Sprite.add() argument after * must be an iterable, not int File "/Users/siddhivinay/Documents/learningPong.py", line 18, in <module> paddleA =Paddle(white, 10, 100)""

paddleA.rect.x = 20
paddleA.rect.y = 200

paddleB = Paddle(white, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

all_sprites_list = pygame.sprite.Group()

all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
 

carryOn = True

clock = pygame.time.Clock()

#-------Main Program ---------
while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False

        elif event.type == pygame.QUIT:
            if event.key == pygame.K_x: #Pressing the x Key will quit the game
                carryOn = False                

    all_sprites_list.update()
    
    screen.fill(white)
    pygame.draw.line(screen, blue, [0,350], [500, 350], 5)
    
    all_sprites_list.draw(screen)

    pygame.display.flip()


    clock.tick(60)

pygame.quit()
