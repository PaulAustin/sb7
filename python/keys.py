# A turtle in a big pond that knows your voice

from turtle import Turtle, Screen

print("Creating and Ocean")
ocean = Screen()
ocean.title("Lets find Nemo")

print("Creating a turtle")
bob = Turtle()

print("Defining some commands")
def keyLeft():
    bob.left(45)
    
def keyRight():
    bob.left(10)

def keyUp():
    bob.forward(20)

def keyDown():
    bob.backward(20)

ocean.onkey(keyLeft, "Left")
ocean.onkey(keyRight, "Right")
ocean.onkey(keyUp, "Up")
ocean.onkey(keyDown, "Down")

print("Awake the ocean")
ocean.listen()

print("Now Rest")
ocean.mainloop()

print("All is done")
