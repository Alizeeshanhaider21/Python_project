# import colorgram

# colors=colorgram.extract('image.jpg', 30)
# rgb_color=[]
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.g
#     my_color=(r,g,b)
#     rgb_color.append(my_color)
# print(rgb_color)
import  turtle as t
t.colormode(255)
import random
color_list = [(239, 239, 239), (220, 226, 226), (180, 7, 7), (243, 235, 235), (234, 242, 242), (157, 97, 97), (22, 95, 95), (193, 158, 158), (244, 215, 215), (216, 146, 146), (177, 201, 201), (69, 154, 154), (127, 45, 45), (93, 50, 50), (69, 54, 54),
              (67, 141, 141), (125, 160, 160), (228, 169, 169), (185, 94, 94), (128, 177, 177), (77, 30, 30), (88, 126, 126), (219, 92, 92), (22, 63, 63), (167, 190, 190), (73, 71, 71), (235, 174, 174), (165, 209, 209), (192, 215, 215), (19, 57, 57)]
timmy = t.Turtle()
timmy.speed('fastest')
timmy.hideturtle()
timmy.penup()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
no_of_dots=100
for dot_count in range(1,101):
    
    timmy.dot(20, random.choice(color_list))
   
    timmy.forward(50)

    timmy.dot(20, random.choice(color_list))
    
    if dot_count%10==0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

my_screen = t.Screen()
my_screen.exitonclick()
