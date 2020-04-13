import turtle
import random

word = "文字Operator"

def makeBlob(x, y, letter):
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.penup()
    t.goto(x, y)
    t.color('red')
    t.pendown()
    t.width(2)
    t.circle(20)
    t.color('blue')
    t.write(letter, font=("Arial", 34, "normal"), align="center")
    return t

blobs = []
def scatter(word):
    for letter in word:
        x = random.randint(-300,300)
        y = random.randint(-300,300)
        b = makeBlob(x, y, letter)
        blobs.append(b)

def main():
    scatter(word)
    for b in blobs:
        print('x', b.xcor(), b.ycor())

main()
