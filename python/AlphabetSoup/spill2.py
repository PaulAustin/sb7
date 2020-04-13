import turtle
import random

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

def scatterWord(word):
    for letter in word:
        x = random.randint(-250,250)
        y = random.randint(-250,250)
        b = makeBlob(x, y, letter)
        print("l", letter)
    return

def main():
    scatterWord(word)
    return

main()
