# draw polygon using turtle
import turtle
turtle.Screen().bgcolor("green")
turtle.Screen().setup(300,400)
polygon=turtle.Turtle()

side_num=6
length=70
angle=360.0/side_num

for i in range(side_num):
    polygon.forward(length)
    polygon.right(angle)
turtle.done()