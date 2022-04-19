There are 3 files containing the source code:
- ball.py
- paddle.py
- learningPong.py

In ball.py:
Puck Class 
- init function: ball properties
- move function: moving the ball
- check_boundary function: Checking boundaries in table
- add_vector function: angles in the ball
- collision_paddle function: how the ball moves when gets hit with paddle 
- reset function: reset the ball when goal scored
- draw: paints the ball in the table

In paddle.py:
Paddle Class
- init function: paddle properties
- check_vertical_bounds: top and bottom of table boundaries
- check_left_boundary: left side of table boundaries
- check_right_boundary: right side of table boundaries
- move: how the ball moves
- draw: paints the paddle in the table
- get_pos: position in the table
- reset: resets the paddle at the initial position

In learningPong.py:
Main file contains the game
- setup game stuff (puck, paddles, sounds, table and window size)
- load the images and sounds
- reset_game: resets the game when goal is scored
- inside_goal: checks if someone scores a goal
- gameloop: Here runs the game
    - Load music
    - set keybinds: X and Close windows buttons stop the game
        - ASDW buttons moves player A
        - Arrows buttons moves player B
    - moving the paddles checking vertical center of the table boundaries
    - moving the ball
    - Check if player A or player B scored
        - Reset the game if so
        - Add 1 to player score if so
    - check boundaries for ball(in table)
        - Play sound when ball gets hit
    - Draw the table in window
    - Draw scoreboard on top
    - Draw paddles and puck in table
    - Set 60 frames/second
- Run the game with 450 ball's speed