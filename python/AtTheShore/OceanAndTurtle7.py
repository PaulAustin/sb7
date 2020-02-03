# Adding conditional control flow (if & elif)
# A turtle who knows you vioce 
# in a big big pond.

from turtle import Turtle, Screen

print("Creating and Ocean")
ocean = Screen()
ocean.title("Lets find Nemo")

swimSpeed = 0
clockPeriod = 75

print("Creating a turtle")
bob = Turtle()
bob.speed(0)

print("Defining some commands")
def keyLeft():
    bob.left(45)
    
def keyRight():
    bob.right(45)

def keyUp():
    global swimSpeed
    swimSpeed += 5

def keyDown():
    global swimSpeed
    swimSpeed -= 5

def keyHome():
    global swimSpeed
    swimSpeed = 0
    bob.goto(0, 0)
    
def swim():
    bob.forward(swimSpeed)
    pos = bob.pos()
    # The turtle library puts the x,y location in a 'tuple'
    # to access an element of a tuple it is 'indexed'
    # using square brackets.
    x = pos[0] # First element. It's X
    y = pos[1] # Second element It's Y
    #print("position", pos, x, y)
    
    if (x > 100) : 
        bob.left(180)
    elif (x < -100) : 
        bob.left(170)
    elif (y > 100) : 
        bob.left(160)
    elif (y < -100) : 
        bob.left(150)
    
    ocean.ontimer(swim, clockPeriod)
    
ocean.onkey(keyLeft, "Left")
ocean.onkey(keyRight, "Right")
ocean.onkey(keyUp, "Up")
ocean.onkey(keyDown, "Down")
ocean.onkey(keyHome, "h")

print("Awake the ocean")
ocean.listen()

ocean.ontimer(swim, clockPeriod)

print("Now Rest")
ocean.mainloop()

print("All is done")
