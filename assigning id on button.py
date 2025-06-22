#Website obtained from https://stackoverflow.com/questions/45728548/how-can-i-get-the-button-id-when-it-is-clicked

#---------------------#
#   Primary Imports
#---------------------#
from tkinter import *
from tkinter import ttk
from tkinter import messagebox 
from PIL import ImageTk, Image
#import cv2 
import os

#--------------------#
#  Global variables
#--------------------#
position_x = 50
position_y = 169
files = [] #creates list to replace your actual inputs for troubleshooting purposes
btn = [] #creates list to store the buttons ins

#---------------------#
#    Makes Interface
#---------------------#
win = Tk() #Win => to create a window
fram = Frame(win) #Win window is the parent window
win.title("Bookstop")
win.geometry("1100x600")
win.config(bg='#2E3550')
win.resizable(width=False, height=True)

#-------------------#
#    Book Button
#-------------------#
#ef nextPage():
    #win.destroy()
    #import Review Page 
    
def func(rev_id):
    rev_id = str(rev_id)
    win.destroy()
    if rev_id == "Button0":
        import Button0
    elif rev_id == "Button1":
        import Button1
    

#-- To change position of book button
def button_move():
    global position_x
    global position_y
    if int(position_x) > 830: #If position_x is over limit then position_x value returns to original 
        position_x = 50       #and position_y bookshelf value is added.
        position_y = position_y + 155
    else:
        position_x = position_x + 130

#-- Assigning id to buttons
f = open("book_id.txt")
ids = []
imgs = []
for line in f: #Extracting number from txt file
    line = line.rstrip("\n")
    ids.append(line)
f.close()

for i in range(11): #this just popultes a list as a replacement for your actual inputs for troubleshooting purposes
    files.append("Button"+str(i))

for i in range(len(files)): 
    bk = Image.open(f"images/book_files/{ids[i]}.png")
    resized_bk = bk.resize((100,120))
    imgs.append(ImageTk.PhotoImage(resized_bk))
    
    border = LabelFrame(win, bd = 0, background = "#D3D3D3")
    btn.append(Button(border, text=files[i], image=imgs[-1], command=lambda c=i : func(btn[c].cget("text")), relief=SOLID))
    btn[i].pack()
    border.place(x=position_x, y=position_y)
    
    button_move()

win.mainloop()
