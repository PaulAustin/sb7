# Throw two rocks in a ocean

from turtle import Turtle, Screen
import random

print("Creating an Ocean")
ocean = Screen()
ocean.title("Let's find Splash")

print("Creating a drawing turtle")
bob = Turtle()
bob.color('purple')
bob.hideturtle()
bob.speed(0)
bob.width(5)

colors = ['red','blue','orange','purple','black']

def rings(x,y):
    for i in range(20, 180, 10):
        bob.up()
        bob.goto(x, y-i)
        bob.down()
        bob.circle(i)
    
def splash(x, y):
    print(x, y)

    bob.color(random.choice(colors))
    rings(x, y)
    rings(x+10, y)    

ocean.onclick(splash)
