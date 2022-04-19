# Import the pygame library and initialise the game engine
# This was built off the pong tutorial but implimented the airhockey source for enhancement
import pygame
from paddle import Paddle
from ball import Ball
from random import randint

# Define some colors
BLUE = (0,0,128)
WHITE = (250,250,250)

# Size of pygame window
width, height = 900, 500

# Setting up the table stuff initial location
paddleA = Paddle(20, height/2)
paddleB = Paddle(width-20, height/2)
puck = Ball(width / 2, height / 2)
goal_width = 150
goal_first_post = height / 2 - goal_width / 2
goal_second_post = height / 2 + goal_width / 2

# Pygame and Sound mixer initialization
pygame.init()
pygame.mixer.init()

# Start pygame window
size = (width, height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Air Hockey")

playerA_randomizer = randint(1,4)
playerB_randomizer = randint(1,4)
puck_randomizer = randint(1,3)
# Define objects and sounds
table = pygame.image.load("hockey_table.jpg")
paddleA_img = pygame.image.load("paddle_" + str(playerA_randomizer) + ".png")
paddleB_img = pygame.image.load("paddle_" + str(playerB_randomizer) + ".png")
puck_img = pygame.image.load("puck_"+ str(puck_randomizer) + ".png")
paddleHit = pygame.mixer.Sound('hit.wav')
goal_whistle = pygame.mixer.Sound('goal.wav')
table_rect = pygame.Rect(5, 5, 900, 490)

# Game time
clock = pygame.time.Clock()
 
# Function that executes when a goal scored
def reset_game(speed, player):
    puck.reset(speed, player)
    paddleA.reset(25, height/ 2)
    paddleB.reset(width - 25, height / 2)

# Function that decides if a goal is scored
def inside_goal(side):
    if side == 0:
        return (puck.x - puck.radius <= 0) and (puck.y >= goal_first_post) and (puck.y <= goal_second_post)

    if side == 1:
        return (puck.x + puck.radius >= width) and (puck.y >= goal_first_post) and (puck.y <= goal_second_post)


 # Game Loop
def game_loop(speed):
    # Score
    scoreA = 0
    scoreB = 0

    pygame.mixer.music.load('background.mp3') 
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(.2)
    
    carryOn = True
    while carryOn:

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # If user clicked close
                pygame.quit()
                carryOn = False # Flag that we are done so we exit this loop
            elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_x: #Pressing the x Key will quit the game
                        pygame.quit()
                        carryOn=False
    
        # Moving the paddles when the use uses the arrow keys (player A) or "W/S" keys (player B) 
        key_presses = pygame.key.get_pressed()

        # Process Player 1 Input
        w = key_presses[pygame.K_w]
        s = key_presses[pygame.K_s]
        d = key_presses[pygame.K_d]
        a = key_presses[pygame.K_a]

        # Process Player 2 Input
        up = key_presses[pygame.K_UP]
        down = key_presses[pygame.K_DOWN]
        right = key_presses[pygame.K_RIGHT]
        left = key_presses[pygame.K_LEFT]

        # time period between two consecutive frames.
        time_delta = clock.get_time() / 1000.0

        # Update PaddleA - left side
        paddleA.move(w, s, a, d, time_delta)
        paddleA.check_vertical_bounds(table_rect.top-10, table_rect.bottom-32)
        paddleA.check_left_boundary(table_rect.width+20)

        # Update PaddleB - right side
        paddleB.move(up, down, left, right, time_delta)
        paddleB.check_vertical_bounds(table_rect.top-10, table_rect.bottom-32)
        paddleB.check_right_boundary(table_rect.width - 36)

        puck.move(time_delta)

        # Goal Player B
        if inside_goal(0):
            # Goal Sound
            pygame.mixer.Sound.play(goal_whistle)  # Added sound for goal
            scoreB += 1
            reset_game(speed, 1)

        # Goal Player A
        if inside_goal(1):
            # Goal Sound
            pygame.mixer.Sound.play(goal_whistle)
            scoreA += 1
            reset_game(speed, 2)

        # Check if paddle is inside the boundaries
        puck.check_boundary(table_rect.width, table_rect.height)

        # Puck hit, play sound when puck gets hit
        if puck.collision_paddle(paddleA):
            pygame.mixer.Sound.play(paddleHit)

        if puck.collision_paddle(paddleB):
            pygame.mixer.Sound.play(paddleHit)

        # Render hockey_table in the center of window
        window = screen.get_rect()
        screen.blit(table, table.get_rect(center=window.center))

        # Show score
        font = pygame.font.Font(None, 74)
        text = font.render(str(scoreA), 1, BLUE)
        screen.blit(text, (300,15))
        text = font.render(str(scoreB), 1, BLUE)
        screen.blit(text, (600,15))

        # drawing the paddle and the puck
        paddleA.draw(screen, paddleA_img)
        paddleB.draw(screen, paddleB_img)
        puck.draw(screen, puck_img)

        # Refresh with 60 frames/second
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

# Run the game with puck's speed 450
game_loop(450)
