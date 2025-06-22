from tkinter import *
from PIL import Image, ImageTk

win = Tk()
win.geometry("1100x600")
win.title("Testing")

position_x = 50
position_y = 68

def nextPage():
    win.destroy()

def button_move():

    global position_x

    global position_y

    if int(position_x) > 830: #If position_x is over limit then position_x value returns to original

        position_x = 50       #and position_y bookshelf value is added.

        position_y = position_y + 155

    else:

        position_x = position_x + 130



#-- Book template to insert for each book

f = open("book_id.txt")

ids = []

for line in f: #Extracting number from txt file

    line = line.rstrip("\n")

    ids.append(line)

f.close()



imgs = []

for i in range(11):

    canvas = Canvas(win, width=200, height=200)

    canvas.place(x=position_x, y=position_y)



    bk = Image.open(f"images/book_files/{ids[i]}.png")

    resized_bk = bk.resize((100,120))

    imgs.append(ImageTk.PhotoImage(resized_bk))

   

    butt = Button(canvas, image=imgs[-1], command=nextPage).pack()

    button_move()
    
win.mainloop()