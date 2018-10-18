
import turtle

wn = turtle.Screen()
alex = turtle.Turtle()
alex.shape("turtle")
lower = 0
upper = 360
step = 90

while lower < upper:
    print alex.pos()
    alex.forward(step)
    alex.left(step)
    lower += step

print alex.pos()

turtle.exitonclick()
