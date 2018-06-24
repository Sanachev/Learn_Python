from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
my_gif = PhotoImage(file='c:\\users\\user\\avatar.gif')
create_gif = canvas.create_image(0, 0, anchor=NW, image=my_gif)
def move_gif(event):
    if event.keysym == 'Up':
        canvas.move(create_gif, 0, -5)
    elif event.keysym == 'Down':
        canvas.move(create_gif, 0, 5)
    elif event.keysym == 'Left':
        canvas.move(create_gif, -5, 0)
    else:
        canvas.move(create_gif, 5, 0)
canvas.bind_all('<KeyPress-Up>', move_gif)
canvas.bind_all('<KeyPress-Down>', move_gif)
canvas.bind_all('<KeyPress-Left>', move_gif)
canvas.bind_all('<KeyPress-Right>', move_gif)
