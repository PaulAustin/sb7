# Throw rocks in a ocean

from turtle import Turtle, Screen

print("Creating an Ocean")
ocean = Screen()
ocean.title("Let's find Splash")

print("Creating a drawing turtle")
bob = Turtle()
bob.color('purple')
bob.speed(0)

def splash(x, y):
    print("splash at", x, y)
    bob.color('purple')
    bob.goto(x, y)
    bob.circle(50)
    
ocean.onclick(splash)

bob.ondrag(drag, btn=2)

ocean.listen()

