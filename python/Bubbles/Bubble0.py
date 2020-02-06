# A Bubble

from turtle import Turtle, Screen
import random
print("Creating an Ocean")
ocean = Screen()
ocean.title("Let's find Splash")
ocean.setup(800, 800)

# Make the pen fast.
ocean.tracer(0)

class Bubble:
    def __init__(self, x, y, color):

        # Set location and direction
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0

        # Make our own turtle fro drawing
        self.turtle = Turtle()
        self.turtle.color(color)
        self.turtle.up()
        self.turtle.goto(self.x, y)

    def sim(self):
        self.turtle.down()
        self.turtle.circle(25)
        self.turtle.up()
        self.x += self.dx
        self.y += self.dy


colors = ['red', 'blue', 'green', 'orange', 'purple', 'black', 'plum']

def throwPaper(x, y):
    color = random.choice(colors)
    b = Bubble(x, y, color)
    b.sim()

def tictoc():
    ocean.ontimer(tictoc, 20)

ocean.onclick(throwPaper)
ocean.ontimer(tictoc, 20)
