import pygame 
import math
#we modeled off of air hockey source's file paddle.py

class Paddle():    
    def __init__(self, pad_x, pad_y):
        self.x = pad_x
        self.y = pad_y
        self.radius = 40
        self.speed = 400
        self.mass = 2000
        self.angle = 0

    def check_vertical_bounds(self, top, bottom):
        # top
        if self.y -self.radius/2 <= top:
            self.y = self.radius/2
        # bottom
        elif self.y + self.radius/2 > bottom:
            self.y = bottom - self.radius/2

    def check_left_boundary(self, width):
        if self.x - self.radius - 10 <= 0:
            self.x = self.radius + 10
        elif self.x + self.radius > int(width / 2) - 20:
            self.x = int(width / 2) - self.radius - 20

    def check_right_boundary(self, width):
        if self.x + self.radius + 10 > width:
            self.x = width - self.radius -10
        elif self.x - self.radius < int(width / 2) -10:
            self.x = int(width / 2) + self.radius -10
    
    def move(self, up, down, left, right, time_delta):
            dx, dy = self.x, self.y
            self.x += (right - left) * self.speed * time_delta
            self.y += (down - up) * self.speed * time_delta

            dx = self.x - dx
            dy = self.y - dy

            self.angle = math.atan2(dy, dx)
    
    def draw(self, screen, img):
        position = (int(self.x), int(self.y))
        screen.blit(img,position)
        pygame.Surface.blit(img, screen, position)
    
    def get_pos(self):
        return self.x, self.y

    def reset(self, start_x, start_y):
        self.x = start_x
        self.y = start_y
