#!/usr/bin/python3
#
# Making an argument, or rather taking an argument
# taking as many as you want to make

import sys
from turtle import Turtle, Screen
import random
import math

numBubbles = 0
if len(sys.argv) > 1:
    print("argv[1] argument type is", type(sys.argv[1]))
    numBubbles = int(sys.argv[1])
    print("Requested number of bubbles:", numBubbles)
else:
    print("Using default number of bubbles", numBubbles)

# Bubbles on the water, no trails
print("Creating an Ocean")
ocean = Screen()
ocean.title("Let's find Splash")
ocean.setup(800, 800)
ocean.tracer(0)

class Bubble:
    # Special name for the very first method called __init__
    def __init__(self, x, y, color1, color2):

        # Set location and direction
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0

        # Make our own 'private' turtle for drawing
        self.turtle = Turtle()
        self.turtle.color(color1, color2)
        self.turtle.hideturtle()
        self.turtle.up()
        self.turtle.goto(self.x, self.y)
        self.turtle.width(3)

    # A method to simulate the passage of time
    def sim(self):
        # self.turtle.clear()
        self.turtle.goto(self.x, self.y)
        self.turtle.down()
        self.turtle.begin_fill()
        self.turtle.circle(25)
        self.turtle.end_fill()
        self.turtle.up()
        self.x += self.dx
        self.y += self.dy
        self.checkWalls()

    # Give the bubble a random direction
    def randomBump(self):
        dx = (random.randint(0, 7)-3) * 8
        dy = (random.randint(0, 7)-3) * 8
        self.bump(dx, dy)

    def bump(self, dx, dy):
        self.dx = dx
        self.dy = dy

    # Keep the bubble on the pond.
    # How could you make it a circular?
    def checkWalls(self):


        # h = math.sqrt((self.x * self.x) + (self.y * self.y))
        # if (h > 300):
        #    self.dx *= -1

        if ((self.x > 300) or (self.x < -300)):
            self.dx *= -1
        if ((self.y > 300) or (self.y < -300)):
            self.dy *= -1


colors = ['red', 'blue', 'green', 'orange', 'purple', 'black', 'plum']
bubbles = []

def blowBubble(x, y):
    color1 = random.choice(colors)
    color2 = random.choice(colors)
    b = Bubble(x, y, color1, color2)
    b.randomBump()
    bubbles.append(b)
    print('Number of bubbles', len(bubbles))

def tictoc():
    # Simulate the passage of time for each bubbble
    for b in bubbles:
        b.sim()
    ocean.update()
    ocean.ontimer(tictoc, 20)


for i in range(numBubbles):
    blowBubble(random.randint(-50,50), random.randint(-50,50))

ocean.onclick(blowBubble)
ocean.ontimer(tictoc, 20)

# ocean.mainloop()

