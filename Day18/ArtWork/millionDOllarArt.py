#code to create my million dollar art hehe
# import colorgram 
# colors = colorgram.extract('Day18/ArtWork/image.jpg',30)

# rgb_color = []
# for color in colors:
#     # rgb_color.append(color.rgb)
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_color.append((r,g,b))
# print(rgb_color)
import turtle
import random
zeph = turtle.Turtle()

color_list =[(202, 164, 110),(149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
turtle.colormode(255)
# def gen_color():
#     rgb = color_list[random.randint(0,(len(color_list)-1))]
#     zeph.pencolor(rgb)

# zeph.pensize(20)
# val_y = 50
# for y in range(10):
#     for x in range(10):
#         zeph.pendown()
#         gen_color()
#         zeph.forward(1)
#         zeph.penup()
#         zeph.forward(50)
#     zeph.teleport(x=0,y=val_y)
#     val_y+=50

#angel's version makes use of the dot  function
zeph.ht()#make turtle invisible
val_y = 50
for y in range(10):
    for x in range(10):
        zeph.dot(20,random.choice(color_list))
        zeph.penup()
        zeph.forward(50)
    zeph.teleport(x=0,y=val_y)
    val_y+=50

screen = turtle.Screen()
screen.exitonclick()