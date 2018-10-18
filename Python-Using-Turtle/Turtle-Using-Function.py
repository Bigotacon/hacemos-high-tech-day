def create_shape(alex,step):
    start = alex.pos()
    while 1:
        alex.forward(step)
        alex.left(step)

import turtle
wn = turtle.Screen()
alex = turtle.Turtle()
alex.speed(10)
alex.shape("turtle")

create_shape(alex,179.9)


turtle.exitonclick()
