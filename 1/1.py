import turtle
import math
def drawTriangle(myTurtle, a, b, angle):
    c = math.sqrt(a*a + b*b - 2*a*b*math.cos(math.radians(angle)))
    alpha = math.degrees(math.asin(a / (c/math.sin(math.radians(angle)))))
    print(alpha)
    print(c)
    myTurtle.forward(a)
    myTurtle.right(180-angle)
    myTurtle.forward(b)
    myTurtle.right(180-alpha)
    myTurtle.forward(c)


wn = turtle.Screen()
t = turtle.Turtle()
drawTriangle(t, 100, 150, 40)
wn.exitonclick()
