# A pond with bubbles

from turtle import Turtle, Screen
import random

print("Creating an pond")
ocean = Screen()
ocean.title("Blowing in the wind")
ocean.setup(800, 800)
ocean.tracer(0)

# A Python class
class Bubble:
    # Special name for the very first method called __init__
    def __init__(self, x, y, color):

        # Set location and direction
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0

        # Make our own 'private' turtle for drawing
        self.turtle = Turtle()
        self.turtle.color(color)
        self.turtle.up()
        self.turtle.goto(self.x, self.y)

    # A method to simulate the passage of time
    def sim(self):
        self.turtle.down()
        self.turtle.circle(25)
        self.turtle.up()
        self.x += self.dx
        self.y += self.dy


colors = ['red', 'blue', 'green', 'orange', 'purple', 'black', 'plum']

def blowBubble(x, y):
    color = random.choice(colors)
    b = Bubble(x, y, color)
    # Make it show at least once
    b.sim()
    # what happens to 'b'?

def tictoc():
    # What to add here?
    ocean.ontimer(tictoc, 20)

ocean.onclick(blowBubble)
ocean.ontimer(tictoc, 20)
