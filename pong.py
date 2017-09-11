import random
from Tkinter import *

# Initialize global variables
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

# Initalize ball_pos and ball_vel
ball_pos = [WIDTH/2, HEIGHT/2]
ball_vel = [-3,1]

def spawn_ball(direction):
    global ball_pos, ball_vel
    ball_pos = [WIDTH/2, HEIGHT/2] # Puts ball in center
    x = random.randrange(2,4)
    y = random.randrange(1,3)

    if direction == 'RIGHT':
        ball_vel = [x,-y]
    else:
        ball_vel = [-x,-y]

# Event Handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel
    global score1, score2
    paddle1_pos = HEIGHT/2
    paddle2_pos = HEIGHT/2
    score1 = 0
    score2 = 0
    choice = ['LEFT','RIGHT']
    spawn_ball(random.choice(choice))

def draw(canvas):
    global score1, score2
    global paddle1_pos, paddle2_pos
    global ball_pos, ball_vel

    # DRAW GUTTERS AND MIDLINE
    frame.

root = Tk()

frame = Frame(root, width=WIDTH, height=HEIGHT)
root.resizable(width=False, height=False)
root.mainloop()
