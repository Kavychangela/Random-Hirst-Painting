import random
import turtle
from turtle import Screen

color_list=[(233, 225, 209), (216, 217, 222), (108, 110, 126), (209, 155, 98), (140, 141, 152), (186, 62, 31), (225, 213, 111), (233, 214, 224), (207, 148, 178), (102, 110, 172), (177, 157, 44), (222, 230, 223), (28, 27, 68), (29, 46, 28), (38, 41, 19), (194, 20, 7), (225, 169, 197), (209, 88, 63), (44, 46, 103), (234, 173, 160), (129, 80, 90), (157, 167, 159), (182, 184, 214), (84, 97, 85), (208, 80, 105), (183, 15, 22), (47, 28, 48), (70, 71, 42), (223, 205, 26), (52, 71, 54), (185, 197, 186), (120, 134, 120), (179, 196, 202), (113, 134, 141), (49, 68, 75)]
timmy=turtle
timmy.colormode(255)
timmy.hideturtle()
timmy.shape("turtle")
timmy.color("green")
timmy.speed("fastest")
timmy.penup()
timmy.setposition(-300, -300)
number_of_dots=100
def row():
    for dot_count in range(1, number_of_dots+1):
            timmy.dot(20, random.choice(color_list))
            timmy.penup()
            timmy.forward(50)
            if dot_count%10==0:
                timmy.pendown()
                timmy.penup()
                timmy.setheading(90)
                timmy.forward(50)
                timmy.setheading(180)
                timmy.forward(500)
                timmy.setheading(0)


row()
screen=Screen()
screen.exitonclick()

