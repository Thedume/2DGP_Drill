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


turtle.shape('turtle')
turtle.onkey(moveW, 'w')
turtle.listen()
turtle.onkey(moveA, 'a')
turtle.listen()
turtle.onkey(moveS, 's')
turtle.listen()
turtle.onkey(moveD, 'd')
turtle.listen()
turtle.onkey(reset, 'Escape')
turtle.listen()

turtle.exitonclick()