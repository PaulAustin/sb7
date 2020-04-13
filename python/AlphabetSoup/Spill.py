import turtle
import math
import random

word = "Hello"
letters = []

def makeBlob(x, y, letter):
    t = turtle.Turtle('circle')
    t.speed(0)
    t.hideturtle()
    t.penup()
    t.color('blue')
    t.goto(x, y)
    t.pendown()
    t.circle(20)
    t.color('red')
    t.write(letter, font=("Arial", 24, "normal"), align="center")
    return t

def scatter(word):
    for letter in word:
        print("letter is", letter)
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        b = makeBlob(x, y, letter)
        letters.append(b)

def main():
    scatter(word)

main()
