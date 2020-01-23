# A turtle in a big pond that knows your voice

from turtle import Turtle, Screen

print("Creating and Ocean")
ocean = Screen()
ocean.title("Lets find Nemo")

swimSpeed = 0

print("Creating a turtle")
bob = Turtle()

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
    swimSpeed = 0
    bob.goto(0, 0)
    
def swim():
    bob.forward(swimSpeed)
    pos = bob.pos()
    x = pos[0]
    y = pos[1]
    print("pos", pos, x, y)
    ocean.ontimer(swim, 200)
    
ocean.onkey(keyLeft, "Left")
ocean.onkey(keyRight, "Right")
ocean.onkey(keyUp, "Up")
ocean.onkey(keyDown, "Down")
#ocean.onkey(keyHome, "h")
ocean.onkey((lambda: bob.goto(0,0)), "h")

print("Awake the ocean")
ocean.listen()

ocean.ontimer(swim, 200)

print("Now Rest")
ocean.mainloop()

print("All is done")
