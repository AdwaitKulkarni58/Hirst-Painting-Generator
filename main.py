import colorgram as cg

colors = cg.extract("image.jpg",30)

lst_of_color = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_tuple = (r,g,b)
    lst_of_color.append(rgb_tuple)

print(lst_of_color)