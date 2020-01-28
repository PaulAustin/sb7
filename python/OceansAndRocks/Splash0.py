# Throw rocks in a ocean

from turtle import Turtle, Screen

print("Creating an Ocean")
ocean = Screen()
ocean.title("Let's find Splash")

print("Creating a drawing turtle")
bob = Turtle()
bob.color('purple')

def splash(x, y):
    print(x, y)
    bob.goto(x, y)

ocean.onclick(splash)
