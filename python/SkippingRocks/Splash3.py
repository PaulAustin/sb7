# Throw rocks in a ocean

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
bob.width(2)

colors = ['red','blue','green','yellow','orange','purple']

def splash(x, y):
    print(x, y)
    bob.up()

    bob.color(random.choice(colors))

    bob.goto(x, y-20)
    for i in range(20, 80, 4):
        bob.goto(x, y-i)
        bob.down()
        bob.circle(i)
        bob.up()
    
ocean.onclick(splash)
