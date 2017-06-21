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
    bo.setposition(0, -125)                 # Before I start drawing the second triangle, I move the pen down the y- axis
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



def leaf(cursor):                            # This function draws a circle
    cursor.circle(60)

def flower():
    window = turtle.Screen()
    window.bgcolor("lightgreen")
    b = turtle.Turtle()
    b.speed(7)

    b.setposition(0,-200)                   # Here, I start with drawing a green stem
    b.color("green")
    b.home()                     
    
    b.color("white", "coral")               # Settings to make a pretty, orange flower
    b.begin_fill()
    for i in range(1,7):                   # In this function I repeat the circle drawing from the previous function
        leaf(b)
        b.right(60)
    b.end_fill()

    window.exitonclick()
flower()




