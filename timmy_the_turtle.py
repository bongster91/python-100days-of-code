import turtle as t
import random

timmy = t.Turtle()
timmy.shape('turtle')
t.colormode(255)
# draw a square
# for i in range(0, 4):
#     timmy.forward(100)
#     timmy.right(90)

# draw a dashed line
# for _ in range(0, 10):
#     timmy.pendown()
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)

# draw a pentagon with random colors
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# timmy.pendown()

# def draw_shape(number_of_sides):
#     angle = 360 / number_of_sides
#     random_color = colours[random.randint(0, len(colours) - 1)]
    
#     for _ in range(0, number_of_sides):
#         timmy.pencolor(random_color)
#         timmy.right(angle)
#         timmy.forward(50)


# for i in range(3, 10):
#     draw_shape(i)

# draw a random walk with random colors, thicker lines and faster walk
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# angles = [0, 90,180, 270]
# timmy.pendown()

# for _ in range(0, 100):
#     random_angle = random.choice(angles)
#     random_color = random.choice(colours)
#     timmy.speed(10)
#     timmy.width(10)
#     timmy.pencolor(random_color)
#     timmy.right(random_angle)
#     timmy.forward(20)


# draw a spirograph

# timmy.width(1)
# def get_random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color


# for _ in range(0, 50):
#     timmy.pencolor(get_random_color())
#     timmy.speed(10)
#     timmy.circle(50)
#     timmy.right(10)

# hirst painting project
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
timmy.penup()
timmy.goto(-400, -300)

def move_forward():
    x = -400
    y = -300
    
    for _ in range(10):
        timmy.goto(x, y)
        for _ in range(10):
            random_color = random.choice(color_list)
            timmy.dot(20, random_color)
            timmy.forward(40)
        
        y += 50

move_forward()

screen = t.Screen()
screen.exitonclick()