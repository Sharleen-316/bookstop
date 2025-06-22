from tkinter import *
import time
import os

#---------------------#
#   Primary Imports
#---------------------#
from tkinter import *
import tkinter as ttk
from tkinter import messagebox #Shows message when error etc. When searching for book and not available states file not in directory.
from PIL import ImageTk, Image
import os

#-------------------------#
#    Screen Interface
#-------------------------#
win = Tk()
win.title("Waiting on Bookshelf...")
win.geometry("720x480")
win.resizable(width=False, height=False) #Restrict users from maximising screen

ico = Image.open("images\other_images\small_logo.png")
bs_icon = ImageTk.PhotoImage(ico)
win.wm_iconphoto(False, bs_icon)

#------------------#
#      Gif
#------------------#
frameCnt = 96
frames = [PhotoImage(file=r'images\other_images\train.gif', format = 'gif -index %i' %(i)) for i in range(frameCnt)]

def update(ind):
    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    win.after(60, update, ind)

label = Label(win)
label.pack()
win.after(0, update, 0)

#-- Create a heading
img = Image.open(r"images\other_images\cloud_heading.png")
heading_img = ImageTk.PhotoImage(img)

label1 = Label(image=heading_img)
label1.image = Image

label1.place(x=0, y=20) #Position image

#-------------#
#    Timer
#-------------#
def countdown(time):
    global label
    if time == -1:
        win.destroy()
        import Bookshelf
    else:
        win.after(1000, countdown, time-1)

countdown(3)
win.mainloop()