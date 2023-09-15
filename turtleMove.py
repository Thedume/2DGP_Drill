import turtle

def move():
    turtle.forward(50)
    turtle.stamp()

def moveW():
    turtle.setheading(90)
    move()
   
def moveA():
    turtle.setheading(180)
    move()

def moveS():
    turtle.setheading(270)
    move()

def moveD():
    turtle.setheading(0)
    move()

def reset():
    turtle.reset()