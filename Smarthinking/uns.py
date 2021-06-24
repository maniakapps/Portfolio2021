import turtle
turtle.left(60)
y = 0
for lines in range(4):
    turtle.goto(0, y)
    for zigzag in range(3):
        turtle.forward(100)
        turtle.right(120)
        turtle.forward(100)
        turtle.left(120)
    y += 60
    turtle.end_fill()

turtle.done()
