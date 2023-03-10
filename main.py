from turtle import Turtle, Screen
import colorgram as cg

my_turtle = Turtle()

screen = Screen()
screen.colormode(255)

my_turtle.shape("circle")

my_turtle.speed("fastest")

my_turtle.setheading(225)

colors = cg.extract("image.jpg",30)

lst_of_color = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_tuple = (r,g,b)
    lst_of_color.append(rgb_tuple)

for rgb_tuple in lst_of_color:
    my_turtle.fillcolor(rgb_tuple)
    my_turtle.pendown()
    my_turtle.forward(5)
    my_turtle.penup()
    my_turtle.forward(5)
    my_turtle.pendown()

screen.exitonclick()