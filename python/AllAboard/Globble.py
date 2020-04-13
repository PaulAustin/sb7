#Globble

import turtle
import math
import random

lake = turtle.Screen()
lake.bgcolor('lightblue')

#border
mypen = turtle.Turtle()
mypen.speed(9)
mypen.penup()
mypen.setposition(-300, -300)
mypen.pendown()
mypen.pensize(8)
for side in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()

#create player
player = turtle.Turtle()
player.color('blue')
player.shape('triangle')
player.penup()
player.speed(0)

#create goal
goal = turtle.Turtle()
player.shape('circle')
goal.penup()
goal.setposition(-200, 200)

speed = 0

def turnleft():
    player.left(30)

def turnright():
    player.right(30)

def increasespeed():
    global speed
    speed += 1

def downspeed():
    global speed
    speed -= 1

def isCollision(t1, t2):
    dx = t1.xcor() - t2.xcor()
    dy = t1.xcor() - t2.xcor()
    d = math.sqrt(dx*dx + dy*dy)
    # More work to do here

lake.listen()
lake.onkey(turnleft,"Left")
lake.onkey(turnright, "Right")
lake.onkey(increasespeed, "Up")
lake.onkey(downspeed, "Down")

while True:
    player.forward(speed)

    if (isCollision(player, goal)):
        rx = random.randint(-300,300)
        ry = random.randint(-300,300)
        goal.setposition(rx,ry)

