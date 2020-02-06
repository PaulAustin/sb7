# Bubbles on the water

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

        # Make our own 'private' turtle for drawing
        self.turtle = Turtle()
        self.turtle.color(color)
        self.turtle.up()
        self.turtle.goto(self.x, self.y)

    def sim(self):
        self.turtle.goto(self.x, self.y)
        self.turtle.down()
        self.turtle.circle(25)
        self.turtle.up()
        self.x += self.dx
        self.y += self.dy
        self.checkWalls()

    def randomBump(self):
        dx = (random.randint(0, 7)-3) * 10
        dy = (random.randint(0, 7)-3) * 10
        self.bump(dx, dy)

    def bump(self, dx, dy):
        self.dx = dx
        self.dy = dy

    def checkWalls(self):
        if ((self.x > 300) or (self.x < -300)):
            self.dx *= -1
        if ((self.y > 300) or (self.y < -300)):
            self.dy *= -1


colors = ['red', 'blue', 'green', 'orange', 'purple', 'black', 'plum']
bubbles = []

def blowBubble(x, y):
    color = random.choice(colors)
    b = Bubble(x, y, color)
    b.randomBump()
    bubbles.append(b)

def tictoc():
    # Simulate the passage of time for each bubbble
    for b in bubbles:
        print('sim b')
        b.sim()
    ocean.ontimer(tictoc, 20)

ocean.onclick(blowBubble)
ocean.ontimer(tictoc, 20)

