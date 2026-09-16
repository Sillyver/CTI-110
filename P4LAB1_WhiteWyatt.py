# Wyatt White
# 9/16/26
# P4LAB1
# Drawing with turtle graphics program

import turtle

# opens the window for turtle graphics and drawing
win = turtle.Screen()
pen = turtle.Turtle()

# sets up the pen
pen.pensize(5)
pen.pencolor("red")
pen.shape("arrow")

# drawing comands
for side in range(4):
    pen.forward(100)
    pen.right(90)

sides = 3
while sides > 0:
    pen.forward(100)
    pen.left(120)
    sides = sides - 1

# keeps window open until manually closed
win.mainloop()