import turtle

# Here I have used the turtle method to draw some shapes

def triangles():
    window = turtle.Screen()
    bo = turtle.Turtle()

    bo.penup()
    bo.setposition(0, 50)
    bo.pendown()
    for i in range(0, 3):
        bo.right(120)
        bo.forward(100)

    bo.penup()
    bo.setposition(0, -125)
    bo.pendown()
    for i in range(0, 3):
        bo.left(120)
        bo.forward(100)
    window.exitonclick()
triangles()



def square(x):                              # This functions draws a square
    for i in range(1,5):
        x.forward(100)
        x.right(90)


def circle():
    window = turtle.Screen()
    window.bgcolor("lightblue")

    emma = turtle.Turtle()
    emma.shape("turtle")
    emma.color("white")

    for i in range(1,6):                # This loop repeats the function and tilts the angle for every time
        square(emma)
        emma.right(10)
    window.exitonclick()
circle()








