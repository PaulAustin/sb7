import turtle
import math

turtle.tracer(0,0)
t = turtle.Turtle()
t.hideturtle()
t.penup()
t.speed(-1)

size = 200
max = 255
res = 3

def mandelbrot(c, max):
    z = 0.0j
    for i in range(max):
        z = z*z + c
        if abs(z) >= 2:
            return i
    return max

def pixelColor(x, y):
    # scale x and y to a floating point number
    # int the -1 to 1.0 range
    c = complex(x/size-0.5, y/size)

    i = mandelbrot(c, max)

    grey = 1.0 - (i / max)
    return (grey, grey, grey)

for x in range(-size, size+1, res):
    for y in range(-size, size+1, res):
        t.goto(x, y)
        t.dot(res, pixelColor(x, y))
    turtle.update()