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
mypen.setposition(-300,-300)
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
# goal = turtle.Turtle()
# player.shape('circle')
# goal.penup()
# goal.setposition(-200,200)

#new code
word = "Здравствуйте"

def makeBlob(x, y, letter):
    b = turtle.Turtle()
    b.speed(0)
    b.penup()
    b.hideturtle()
    b.width(3)
    b.setposition(x, y)
    b.pendown()
    b.color('blue')
    b.circle(20)
    b.color('red')
    b.write(letter, font=("Arial", 34, "normal"), align="center")
    return b

goals = []

def scatterWord(word):
    for letter in word:
        x = random.randint(-250,250)
        y = random.randint(-250,250)
        b = makeBlob(x, y, letter)
        goals.append(b)
        print("l", letter)
    return

scatterWord(word)
# ########

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
    dy = t1.ycor() - t2.ycor()
    d = math.sqrt(dx*dx + dy*dy)
    return (d < 20)

turtle.listen()
turtle.onkey(turnleft,"Left")
turtle.onkey(turnright, "Right")
turtle.onkey(increasespeed, "Up")
turtle.onkey(downspeed, "Down")


while True:
    player.forward(speed)

    for goal in goals:
        if (isCollision(player, goal)):
            rx = random.randint(-300, 300)
            ry = random.randint(-300, 300)
            goal.setposition(rx, ry)

    # Add bounds checking





