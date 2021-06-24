import turtle
x,y = 0,0
turtle.goto(0,0)
for i in range(5):
    x = 0
    for j in range(4):
        turtle.goto(x, y)
        turtle.circle(15)
        x += 50
    y += 50
turtle.done()