import turtle
t = turtle.Turtle()
t.color('brown')
t.speed(-1)
t.width(2)

def drawtree(len, d):
    if d == 0:
        t.color('green','pink')
        t.begin_fill()
        t.circle(10)
        t.end_fill()
        t.color('brown')
        return

    scale = 0.75
    branchlen = len * scale
    t.width(d)
    t.forward(len)
    t.left(30)
    drawtree(branchlen, d-1)
    t.right(60)
    drawtree(branchlen, d-1)
    t.left(30)
    t.backward(len)

t.left(90)
t.backward(250)
drawtree(150, 8)
