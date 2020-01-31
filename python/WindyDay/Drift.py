# A box blowing across the water
# SDG

from turtle import Turtle, Screen

print("Creating an Ocean")
ocean = Screen()
ocean.title("Let's find Splash")
ocean.setup(500, 500)

print("Creating a drawing turtle")

# Get the pen ready
bob = Turtle()
bob.color('plum')
bob.width(3)

# Make the pen fast.
bob.hideturtle()
bob.speed(0)
#ocean.tracer(0)

colors = ['red', 'blue', 'green', 'orange', 'purple', 'black', 'plum']

#Where the paper is 
bx = -1000
by = -1000
    
def throwPaper(x, y):
    global bx, by
    bx = x
    by = y

def tictoc():
    global bx, by
    print('tt', bx, by)
    if (bx > -1000):
        bob.up()
        bob.goto(bx, by)
        bob.down()
        bob.circle(20)
    bx = bx + 10
    ocean.ontimer(tictoc,200)   
    
ocean.onclick(throwPaper)
ocean.ontimer(tictoc, 1000)
