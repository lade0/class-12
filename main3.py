#making a spiral
import turtle
turtle.Screen().bgcolor("beige")
turtle.Screen().setup(300,400)
spiral=turtle.Turtle()
size=0
count=0
while count<=10:
    for i in range(4):
        spiral.fd(size+1)
        spiral.left(90)
        size=size-5
    size=size+1
    count=count+1
turtle.done()
        