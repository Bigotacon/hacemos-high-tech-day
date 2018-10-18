
import turtle
#import tkinter

wn = turtle.Screen()
alex = turtle.Turtle()
alex.shape("turtle")

lower = 0
upper = 360
step = 90

while lower < upper:
    print "step %d" % (step)
    alex.forward(step)
    alex.left(step)
    lower += step


turtle.exitonclick()
