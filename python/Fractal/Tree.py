import turtle
def tree(length, n):
    if length < (length/n):
        return
    else:
        sublen = length/n
        t.color('brown')
        t.forward(length)
        t.left(50)
        tree(length * 0.5, sublen)
        t.left(20)
        tree(length * 0.5, sublen)
        t.left(25)
        tree(length * 0.5, sublen)
        t.color('green')
        t.right(80)
        tree(length * 0.5, sublen)
        t.right(20)
        tree(length * 0.5, sublen)
        t.right(25)
        tree(length * 0.5, sublen)
        t.left(30)
        t.backward(length)
    return

t = turtle.Turtle()
t.speed(-1)
t.left(90)
t.backward(100)

tree(300,2)
