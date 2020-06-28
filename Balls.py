import tkinter
from random import randrange, choice


def new_balls():
    global x, y, r, x2, y2, r2, ball, ball2, velocity_moment, vector_moment_x, \
        vector_moment_y, vector_moment_x2, vector_moment_y2
    canv.delete(tkinter.ALL)
    x = randrange(100, 700)
    y = randrange(100, 500)
    r = randrange(30, 50)
    x2 = randrange(100, 700)
    y2 = randrange(100, 500)
    r2 = randrange(30, 50)
    if (x2 - r2 <= x + r and x2 >= x) or (x2 + r >= x - r and x2 <= x):
        x2 = x + r + r2
    if (y2 - r2 <= y + r and y2 >= y) or (y2 + r >= y - r and y2 <= y):
        y2 = y + r + r2
    ball = canv.create_oval(x - r, y - r, x + r, y + r, fill=choice(colors), width=0)
    ball2 = canv.create_oval(x2 - r2, y2 - r2, x2 + r2, y2 + r2, fill=choice(colors), width=0)
    velocity_array = [5, 10]
    vector = [-1, 1]
    velocity_moment = choice(velocity_array)
    vector_moment_x = choice(vector)
    vector_moment_y = choice(vector)
    vector_moment_x2 = choice(vector)
    vector_moment_y2 = choice(vector)
    root.after(5000, new_balls)


def motion():
    global vector_moment_x, vector_moment_y, vector_moment_x2, vector_moment_y2
    canv.move(ball, vector_moment_x, vector_moment_y)
    canv.move(ball2, vector_moment_x2, vector_moment_y2)
    root.after(velocity_moment, motion)
    if canv.coords(ball) == [] or canv.coords(ball2) == []:
        pass
    else:
        if canv.coords(ball)[0] <= 0 or canv.coords(ball)[2] >= 800:
           vector_moment_x = - vector_moment_x
        if canv.coords(ball)[1] <= 0 or canv.coords(ball)[3] >= 600:
            vector_moment_y = - vector_moment_y
        if canv.coords(ball2)[0] <= 0 or canv.coords(ball2)[2] >= 800:
            vector_moment_x2 = - vector_moment_x2
        if canv.coords(ball2)[1] <= 0 or canv.coords(ball2)[3] >= 600:
            vector_moment_y2 = - vector_moment_y2


def click(event):
    global count
    ccx = canv.coords(ball)[2] - r
    ccy = canv.coords(ball)[3] - r
    ccx2 = canv.coords(ball2)[2] - r2
    ccy2 = canv.coords(ball2)[3] - r2
    if r ** 2 >= (event.x - ccx) ** 2 + (event.y - ccy) ** 2:
        canv.delete(tkinter.ALL)
        count = count + 1
        label_count['text'] = count
    if r2 ** 2 >= (event.x - ccx2) ** 2 + (event.y - ccy2) ** 2:
        canv.delete(tkinter.ALL)
        count = count + 10
        label_count['text'] = count


def main():
    global root, canv, colors, label_count, count
    root = tkinter.Tk()
    width_middle = root.winfo_screenwidth() // 2 - root.winfo_screenwidth() // 4
    height_middle = root.winfo_screenheight() // 2 - root.winfo_screenheight() // 4
    root.geometry('800x600+{}+{}'.format(width_middle, height_middle))
    canv = tkinter.Canvas(root, bg='white')
    canv.pack(fill=tkinter.BOTH, expand=1)
    colors = ['red', 'yellow', 'green', 'blue', 'orange']
    count = 0
    new_balls()
    motion()
    canv.bind('<Button-1>', click)
    label_count = tkinter.Label(text=count, bg='white', fg='black', width=20)
    label_count.pack()
    tkinter.mainloop()


if __name__ == "__main__":
    main()
