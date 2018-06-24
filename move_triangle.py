import time
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=400, height=250)
canvas.pack()
canvas.create_polygon(10, 10, 10, 60, 50, 35)
def upd():
    tk.update()
    time.sleep(0.05)
def triangle_move():
    for x in range (0, 60):
        canvas.move(1, 5, 0)
        upd()
    for x in range (0, 30):
        canvas.move(1, 0, 5)
        upd()
    for x in range (0, 60):
        canvas.move(1, -5, 0)
        upd()
    for x in range (0, 30):
        canvas.move(1,0, -5)
        upd()
triangle_move()
    
