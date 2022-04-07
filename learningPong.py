import pygame
pygame.init()

blue = (100, 120, 200)
white = (255, 255, 255)

size = (500, 700)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Pong")

carryOn = True

clock = pygame.time.Clock()

while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False

    screen.fill(white)
    pygame.draw.line(screen, blue, [0,350], [500, 350], 5)
    

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
