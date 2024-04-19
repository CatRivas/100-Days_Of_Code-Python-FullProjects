# import colorgram

# colors = colorgram.extract('image.jpg', 16)
#print(colors) #returns a list of Color objects

#Getting the first color object from the list of colors
# first_color = colors[0]
# print(first_color) #<colorgram.py Color: Rgb(r=254, g=254, b=253), 85.18112671303761%>

#Extracting ths RGB tuple from the first color object (what we're interested in)
# rgb = first_color.rgb
# print(rgb) #Rgb(r=254, g=254, b=253)

##But I want just the tuple without the letters...
# #ONE WAY
# red = rgb[0]
# print(red) #254

# #ANOTHER WAY (this is the way...)
# redd = rgb.r
# print(redd) #254


#Now extracting red, green and blue from the first color Rgb(r=254, g=254, b=253)
# red = first_color.rgb.r
# green = first_color.rgb.g
# blue = first_color.rgb.b
# print(red, green, blue) #254 254 253


#NOW let's get the complete list of colors from the image
# rgb_colors = []

# for color in colors:
#     red = color.rgb.r
#     green = color.rgb.g
#     blue = color.rgb.b
    
#     rgb_color = (red,green, blue)
#     rgb_colors.append(rgb_color)

# print(rgb_colors) #[(219, 254, 237), (84, 254, 155), (173, 146, 118), (245, 39, 191), (158, 107, 56), (2, 1, 176), (151, 54, 251), (221, 254, 101), (253, 146, 193), (3, 87, 176), (249, 1, 246), (35, 34, 253), (1, 213, 212), (249, 0, 0)]


import turtle as t
import random

color_list = [(219, 254, 237), (84, 254, 155), (173, 146, 118), (245, 39, 191), (158, 107, 56), (2, 1, 176), (151, 54, 251), (221, 254, 101), (253, 146, 193), (3, 87, 176), (249, 1, 246), (35, 34, 253), (1, 213, 212), (249, 0, 0)]

t.colormode(255) #ngl this is super important

#instance of Turtle()
tomy = t.Turtle()

tomy.teleport(-230, -220) #changing the initial position of tomy
# position = tomy.position()
# print(position) #(-230.00,-160.00)

tomy.penup()
tomy.hideturtle()

y = -220

for _ in range (10):
    for _ in range(10):
        tomy.dot(20, random.choice(color_list))
        tomy.forward(50)

    y = y + 50 #Updating the value of 'y'
    tomy.teleport(-230, y)
    

#instance of Screen()
screen = t.Screen()
screen.exitonclick()