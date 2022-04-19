import pygame
import random
import math
#we referenced the airhockey source's puck.py
 
class Ball():    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 45
        self.speed = 400
        self.mass = 500
        self.angle = 0
        
    def move(self, time_delta):
        self.x += math.sin(self.angle) * self.speed * time_delta
        self.y -= math.cos(self.angle) * self.speed * time_delta

        self.speed *= 0.999

    def check_boundary(self, width, height):
        # right side
        if self.x + self.radius > width:
            self.x = 2 * (width - self.radius) - self.x
            self.angle = -self.angle

        # left side
        elif self.x - self.radius < 0:
            self.x = 2 * self.radius - self.x
            self.angle = -self.angle

        # bottom
        if self.y + self.radius > height:
            self.y = 2 * (height - self.radius) - self.y
            self.angle = math.pi - self.angle

        # top
        elif self.y - 1.5 *self.radius < 0:
            self.y = 3 * self.radius - self.y
            self.angle = math.pi - self.angle

    def add_vectors(self, first, second):
        x = math.sin(first[0]) * first[1] + math.sin(second[0]) * second[1]
        y = math.cos(first[0]) * first[1] + math.cos(second[0]) * second[1]

        length = math.hypot(x, y)
        angle = math.pi / 2 - math.atan2(y, x)
        return angle, length

    def collision_paddle(self, paddle):
        dx = self.x - paddle.x
        dy = self.y - paddle.y

        # distance between the centers of the circle
        distance = math.hypot(dx, dy)

        # no collision takes place
        if distance > self.radius + paddle.radius:
            return False

        # calculates angle of projection.
        tangent = math.atan2(dy, dx)
        temp_angle = math.pi / 2 + tangent
        total_mass = self.mass + paddle.mass

        # The new vector for puck formed after collision
        vec_a = (self.angle, self.speed * (self.mass - paddle.mass) / total_mass)
        vec_b = (temp_angle, 2 * paddle.speed * paddle.mass / total_mass)

        (self.angle, self.speed) = self.add_vectors(vec_a, vec_b)

        # speed should never exceed a certain limit
        if self.speed > 1400:
            self.speed = 1400

        # new vector for paddle without changing the speed
        vec_a = (paddle.angle, paddle.speed * (paddle.mass - self.mass) / total_mass)
        vec_b = (temp_angle + math.pi, 2 * self.speed * self.mass / total_mass)

        temp_speed = paddle.speed
        (paddle.angle, paddle.speed) = self.add_vectors(vec_a, vec_b)
        paddle.speed = temp_speed

        # To prevent puck and paddle from sticking
        offset = 0.5 * (self.radius + paddle.radius - distance + 1)
        self.x += math.sin(temp_angle) * offset
        self.y -= math.cos(temp_angle) * offset
        paddle.x -= math.sin(temp_angle) * offset
        paddle.y += math.cos(temp_angle) * offset
        return True

    def reset(self, speed, player):
        if player == 1:
            self.angle = random.uniform(-math.pi, 0)
        elif player == 2:
            self.angle = random.uniform(0, math.pi)
        self.speed = speed
        self.x = 900 / 2
        self.y = 500 / 2

    def draw(self, screen, img):
        position = (int(self.x-20), int(self.y-20))
        screen.blit(img,position)
        pygame.Surface.blit(img, screen, position)
