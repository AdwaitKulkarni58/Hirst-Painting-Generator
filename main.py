from turtle import Turtle, Screen
import colorgram as cg

my_turtle = Turtle()

screen = Screen()
screen.colormode(255)

my_turtle.shape("circle")

size_of_turtle = 20

my_turtle.speed(1)

screen.screensize(400, 400, "yellow")

my_turtle.goto(-400, 400)

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
    my_turtle.forward(10)

screen.exitonclick()