import tkinter
from random import randrange, choice
import time


root = tkinter.Tk()
width_middle = root.winfo_screenwidth() // 2 - root.winfo_screenwidth() // 4
height_middle = root.winfo_screenheight() // 2 - root.winfo_screenheight() // 4
root.geometry('800x600+{}+{}'.format(width_middle, height_middle))

canv = tkinter.Canvas(root, bg='white')
canv.pack(fill=tkinter.BOTH, expand=1)

colors = ['red', 'yellow', 'green', 'blue', 'orange']


def new_balls():
    canv.delete(tkinter.ALL)
    x = randrange(100, 700)
    y = randrange(100, 500)
    r = randrange(30, 50)
    canv.create_oval(x - r, y - r, x + r, y + r, fill=choice(colors), width=0)
    root.after(1000, new_balls)


new_balls()
tkinter.mainloop()
