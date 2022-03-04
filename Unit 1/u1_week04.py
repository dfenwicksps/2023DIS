import turtle as t

# Task: Create a face using turtle
# Draw head
# Draw eyes
# Draw nose
# Draw Rosy, red cheeks
# Draw mouth
t.speed(0)


# Move function
def myMove(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


# Eye function
def myCircle(sz, c, pc):  # sz = size, c = colour
    t.fillcolor(c)
    t.pencolor(pc)
    t.begin_fill()
    t.circle(sz)
    t.end_fill()


def mySemiC(sz, c, pc):
    t.fillcolor(c)
    t.pencolor(pc)
    t.begin_fill()
    t.circle(sz, 180)
    t.end_fill()

def shape(fcol, sides, size):
    t.fillcolor(fcol)
    t.begin_fill()
    for i in range(sides):
        t.forward(size)
        t.left(360/sides)
    t.end_fill()

# Function calls below here
# Draw EYES
myCircle(100, "white", "black")
myMove(-50, 100)  # move to create LEFT eye
myCircle(20, "black", "black")
myMove(-45, 120)  # white pupil in LEFT eye
myCircle(8, "white", "black")
myMove(50, 100)  # move to create RIGHT eye
myCircle(20, "black", "black")
myMove(45, 120)  # white pupil in RIGHT eye
myCircle(8, "white", "black")
# Draw NOSE
myMove(0, 75)
#myCircle(25, "black", "black")
t.seth(40)

t.fillcolor("green")
t.begin_fill()
for i in range(2):
    t.circle(30, 90)
    t.circle(30//4, 90)
t.end_fill()

# Draw MOUTH
myMove(-30, 45)
t.seth(270)
mySemiC(30, "black", "black")
t.seth(270)
myMove(-25, 55)
mySemiC(25, "white", "white")

# Draw Rosy, red CHEEKS
myMove(-45, 80)
shape("red", 6, 10)



# always use the following as the last line of code in Pycharm
t.ht()  # hide the turtle
t.Screen().exitonclick()  # keep the canvas open until mouse click
