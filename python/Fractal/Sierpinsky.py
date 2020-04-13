import turtle

def sierpinski(length, depth):
    if depth==0:
        for i in range(3):
            t.forward(length)
            t.left(120)
    else:
        mid = length / 2
        depth -= 1

        # Bottom left
        sierpinski(mid, depth)

        # Botton right
        t.forward(mid)
        sierpinski(mid, depth)

        # Top
        t.backward(mid)
        t.left(60)
        t.forward(mid)
        t.right(60)
        sierpinski(mid, depth)

        # Back to bottom left corner
        t.left(60)
        t.backward(mid)
        t.right(60)

t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(-200, -200)
t.pendown()

t.color('blue','cyan')
t.begin_fill()
sierpinski(500, 5)
t.end_fill()
t.mainloop()
