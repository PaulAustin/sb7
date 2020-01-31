# Write your code here :-)
# Lisa Who?, lissajous

from turtle import Turtle, Screen
import random
import math

print("Creating an Ocean")
ocean = Screen()
ocean.title("Let's find Splash")
ocean.setup(500, 500)
#ocean.tracer(0)

print("Creating a drawing turtle")
bob = Turtle()
bob.color('purple')
bob.hideturtle()
bob.speed(0)
bob.width(3)

# Colors help you see the segments.
# The 'curves' are made up of many striaght lines.
colors = ['red', 'blue', 'green', 'orange', 'purple', 'black', 'plum']

def waves(x,y):
    bob.up()
    bob.goto(x, y)
    bob.down()
    for i in range(1, 2000, 4):
        px = i/10.0
        print(px)
        py1 = math.sin(px * 0.33) * 230
        py2 = math.cos(px * 0.97) * 230
        bob.goto(x + py2, y + py1)
        bob.color(random.choice(colors))
    
def splash(x, y):
    print(x, y)
    bob.color(random.choice(colors))
    waves(x, y)

ocean.onclick(splash)
