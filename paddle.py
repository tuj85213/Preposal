#https://www.101computing.net/pong-tutorial-using-pygame-adding-the-paddles/

#paddles

import pygame
black = (0,0,0)

class Paddle(pygame.sprite.Sprite):

    def _init_(self, color, width, height):
        super()._init_()

        self.image = pygame.Surface([width, height])
        self.image.fill(black)
        self.image.set_colorkey(black)

        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.rect = self.image.get_rect()
