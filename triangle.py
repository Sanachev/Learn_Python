from tkinter import *
import random
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
color = ('green', 'red', 'blue', 'orange', 'yellow', 'pink', 'purple', 'violet', 'magenta', 'cyan')
clr = color[random.randint(0,9)]
def random_triangle(width, height, fillcolor):
    
    x1 = random.randrange(0,width)
    y1 = random.randrange(0,height)
    x2 = x1 + random.randrange(0,width)
    y2 = y1 + random.randrange(0,height)
    x3 = x1 + random.randrange(0,width)
    y3 = y1 + random.randrange(0,height)
    canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill = fillcolor)
def learn():
    for x in range (0,60):
        clr = color[random.randint(0,9)]
        random_triangle(400,400,clr)
learn()
