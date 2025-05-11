import turtle 
turtle.bgcolor("lightblue")
turtle.pensize(4)
turtle.color("darkgreen")
for i in range(4):
    print("Side:",i+1)
    turtle.forward(100)
    turtle.right(90)
turtle.hideturtle()
turtle.done()