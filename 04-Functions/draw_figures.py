###
# Draws each of the figures (square, triangle, rectangle) twice, in different locations
#

import turtle
import figures

window = turtle.Screen()
window.bgcolor("lightgreen")
turtle.speed(5)

figures.draw_square(100)
turtle.penup()
turtle.goto(-200, 100)
turtle.pendown()
figures.draw_square(100)

turtle.penup()
turtle.goto(100, 0)
turtle.pendown()
figures.draw_trangle(90)
turtle.penup()
turtle.goto(100, 150)
turtle.pendown()
figures.draw_trangle(90)

turtle.penup()
turtle.goto(-200, -150)
turtle.pendown()
figures.draw_rectangle(150, 80)
turtle.penup()
turtle.goto(50, -150)
turtle.pendown()
figures.draw_rectangle(150, 80)

turtle.hideturtle()
turtle.mainloop()