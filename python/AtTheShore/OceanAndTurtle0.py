# A Turtle in a big pond that knows your voice
# Its a beginning

print("Read the turtle library")
from turtle import Turtle, Screen

print("Creating and Ocean")
ocean = Screen()
ocean.title("Lets find Nemo")

print("Creating a turtle")
bob = Turtle()

print("Defining some commands")
def keyLeft():
    bob.left(45)
    
def keyUp():
    bob.forward(20)

ocean.onkey(keyLeft, "Left")
ocean.onkey(keyUp, "Up")

print("All is done, or is it?")
