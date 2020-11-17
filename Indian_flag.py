import turtle
turtle.penup()
turtle.goto(-200, 100)
turtle.setup(width=1100, height=700, startx=None, starty=None)

# this will create the orange part for the flag
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor('#FF9933')
turtle.left(90)
turtle.forward(90)
turtle.right(90)
turtle.forward(400)
turtle.right(90)
turtle.forward(90)
turtle.right(90)
turtle.forward(400)
turtle.end_fill()

# to create the white part and Ashok chakra!!!
turtle.left(90)
turtle.forward(90)
turtle.left(90)
turtle.forward(200)
turtle.circle(45)

# to draw the spokes in the chakra

turtle.penup()
turtle.goto(0,55)
turtle.color('blue')
for spoke in range(0,24):
    turtle.goto(0,55)
    turtle.right(15)
    turtle.pendown()
    turtle.forward(45)
    turtle.penup()

turtle.goto(0,10)
turtle.pendown()
turtle.color('black')
turtle.forward(200)
turtle.left(90)
turtle.forward(90)

turtle.penup()
turtle.goto(-200,10)
turtle.right(180)

# this will print the green part
turtle.begin_fill()
turtle.fillcolor('#138808')
turtle.pendown()
turtle.forward(90)
turtle.left(90)
turtle.forward(400)
turtle.left(90)
turtle.forward(90)
turtle.end_fill()

# stick for the flag
turtle.penup()
turtle.goto(-200,-80)
turtle.right(180)
turtle.pendown()
turtle.forward(200)

turtle.penup()
turtle.goto(-150,-170)

turtle.color('deep sky blue')
style= ('Courier', 30, 'italic', 'bold')
turtle.write('HAPPY INDEPENDENCE DAY', font=style, align='left')
turtle.hideturtle()
turtle.done()
