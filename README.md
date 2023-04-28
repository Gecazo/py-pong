# Pong Game
This is a simple implementation of the classic Pong game in Python, using the Pygame library.

# Setup
Before running the game, make sure you have installed the Pygame library. 
You can install it using pip:
``` pip install pygame ```

# How to Play
The objective of the game is to score more points than your opponent. Points are scored when the ball hits the opponent's wall. The first player to reach 10 points wins the game.

# Controls
* Player 1 (left): use the "W" key to move the paddle up and the "S" key to move it down.
* Player 2 (right): use the up arrow key to move the paddle up and the down arrow key to move it down.

# Code Overview
  The code is split into several classes:

* Paddle: represents a paddle that can move up and down.
* Ball: represents the ball that moves around the screen and bounces off the walls and paddles.
* draw: function that draws the game elements on the screen.
* handle_collision: function that handles ball-paddle and ball-wall collisions.
* handle_paddle_movement: function that handles paddle movement based on user input.
* main: function that runs the game loop and handles user input.
