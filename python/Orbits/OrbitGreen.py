# Turtles in space
import turtle

sky = turtle.Screen()
sky.tracer(0)
sky.bgcolor('black')
rocket = turtle.Turtle()
rocket.speed(0)
rocket.color('green')

a = 10.0
b = 28.0
c = 8.0/3.0
x = y = z= 1.0e-1

def draw():
    global x, y, z
    dt = 0.01
    dx = (a * (y-x)) * dt;
    dy = (x * (b-z) - y) * dt;
    dz = (x * y - c * z) * dt
    x += dx
    y += dy
    z += dz
    rocket.goto(x*15, z*10-250)

def tictoc():
    for i in range (10):
        draw()
    sky.ontimer(tictoc, 5)

sky.ontimer(tictoc, 5)

