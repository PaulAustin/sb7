import turtle

t = turtle.Turtle()
t.speed(-1)
t.width(2)
t.color('blue','cyan')

def Koch(l, depth):
    if depth == 0:
        t.forward(l)
    else:
        l /= 3.0
        Koch(l, depth - 1)
        t.right(60)
        Koch(l, depth - 1)
        t.left(120)
        Koch(l, depth - 1)
        t.right(60)
        Koch(l, depth - 1)

t.penup()
t.goto(0,200)
t.backward(300)
t.pendown()
t.begin_fill()
for i in range(6):
    Koch(200, 2)
    t.right(60)
t.end_fill()
