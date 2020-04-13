import turtle

def Koch(length, depth):
    if depth == 0:
        t.forward(length)
    else:
        Koch(length/3, depth-1)
        t.right(60)
        Koch(length/3, depth-1)
        t.left(120)
        Koch(length/3, depth-1)
        t.right(60)
        Koch(length/3, depth-1)

t = turtle.Turtle()
t.speed(0); t.width(2); t.color('blue','cyan')
t.penup(); t.goto(-150,-100); t.pendown()

def main():
    t.begin_fill()
    for _ in range(3):
        Koch(300, 3)
        t.left(120)
    t.end_fill()

main()
