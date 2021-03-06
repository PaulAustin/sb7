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
#x = y = z= 1.0e-200

def setColor(x, y, z):
    r = min(abs(x+0.5), 1.0)
    g = min(abs(y+0.5), 1.0)
    b = min(abs(z+0.5), 1.0)
    rocket.pencolor((r, g, b))

def draw():
    global x, y, z
    dt = 0.01
    dx = (a * (y-x)) * dt;
    dy = (x * (b-z) - y) * dt;
    dz = (x * y - c * z) * dt
    x += dx
    y += dy
    z += dz
    setColor(dx, dy, dz)
    rocket.goto(x*15, z*10-250)

tic = 0.0
def tictoc():
    global tic
    print('iterations', tic)
    tic += 10.0
    for i in range (10):
        draw()
    sky.ontimer(tictoc, 5)

sky.ontimer(tictoc, 5)

