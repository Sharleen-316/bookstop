#Forum Screen Program
#Author: S Hossain
#Purpose: To be able to reccommend new books to be added to the Bookstop database
#Verison: 1.0

#Importing required libraries
from tkinter import *
from tkinter import filedialog
import os
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import messagebox
import sqlite3

#Window settings
win = Tk()
win.geometry("1110x600")
win.resizable(width=False, height=True)
win.title("Bookstop")

ico = Image.open("images\other_images\small_logo.png")
bs_icon = ImageTk.PhotoImage(ico)
win.wm_iconphoto(False, bs_icon)

#Creating a database
conn = sqlite3.connect('books.db')
improvements = sqlite3.connect('improvements.db')

#Create cursor
c = conn.cursor()
i = improvements.cursor()

#Create table
#c.execute("""CREATE TABLE books (
#    book_name null, 
#    author_name null,
#    language null,
#    other null,
#    rating null,
#    tags null,
#    lbl blob
#    )""")

#i.execute("""CREATE TABLE changes (
#    change text 
#    )""")

#Background
back_img = Image.open(r"Images\other_images\forumbg.png")
back_img = back_img.resize((1100,800))
back = ImageTk.PhotoImage(back_img)

back_img = tk.Label(image=back)
back_img.image = Image
back_img.pack()

#Back Button
def back_butt():
  win.destroy()
  import Bookshelf
back_button = Button(win, text="Back", relief = GROOVE, font=('arial', 10), background = '#B89B79', command=back_butt)
back_button.place(x=0, y=0)


#Title of Window
title_1 = Label(win, text="Recommendations", font=('lucida bright', 28, 'bold'), background = '#B89B79', foreground = '#584A38')
title_1.place(x=380, y=60)

#Book Name
label_1 = Label(win, text="*Name of book:", font=('arial', 10, 'bold'), background = '#FCEFD3')
label_1.place(x=370, y=122)

book_name = Entry(win, width=27)
book_name.place(x=565, y=125)

#Author
label_2 = Label(win, text="*Author:", font=('arial', 10, 'bold'), background = '#FCEFD3')
label_2.place(x=370, y=152)

author_name= Entry(win, width=27)
author_name.place(x=565, y=155)

#Language
label_5 = Label(win, text="*Language (or field below):", font=('arial', 10, 'bold'), background = '#FCEFD3')
label_5.place(x=370, y=182)
 
language = StringVar()
languages = ["English", "Spanish", "Mandarin", "Hindi", "French", "Other"]
drop_down = OptionMenu(win, language, *languages)
language.set("Select a language")
drop_down.config(width=21, bg = '#B89B79')
drop_down["menu"].config(bg = '#B89B79')
drop_down.place(x=562, y=180)

label_6 = Label(win, text='Other languages:', font=('arial', 10, 'bold'), background = '#FCEFD3')
label_6.place(x=370, y=212)

other = Entry(win, width=27)
other.place(x=565, y=215)

#Suggested rating
label_3 = Label(win, text="*Age Group", font=('arial', 10, 'bold'), background = '#FCEFD3')
label_3.place(x=370, y=242)

rating = StringVar()
groups = ["G", "T", "M", "E"]
drop_down = OptionMenu(win, rating, *groups)
rating.set("Select a rating")
drop_down.config(width=21, bg = '#B89B79')
drop_down["menu"].config(bg = '#B89B79')
drop_down.place(x=562, y=240)

def message():
    messagebox.showinfo("Key", "G - General Audiences \n T - Teen and Up Audiences \n M - Mature \n E - Explicit: only suitable for adults")  
canvas = Canvas(win, width=10, height=10)
question = Image.open(r"Images\other_images\question_mark.png")
resized_question = question.resize((10,10), Image.ANTIALIAS)
new_question = ImageTk.PhotoImage(resized_question)
canvas.create_image(0,0, anchor='nw', image=new_question)
Button(win, image=new_question, command=message, background= '#FCEFD3', relief=GROOVE).place(x=427, y=247)

#Content Tags
label_4 = Label(win, text="*Content Tags:", font=('arial', 10, 'bold'), background = '#FCEFD3')
label_4.place(x=370, y=272)

tags = Entry(win, width=27)
tags.place(x=565, y=275)

def message():
    messagebox.showinfo('Note', 'Please separate each tag with a comma, e.g. "Sexual, LGBTQ+, Violence"')  
canvas = Canvas(win, width=10, height=10)
question_2 = Image.open(r"Images\other_images\question_mark.png")
resized_question_2 = question_2.resize((10,10), Image.ANTIALIAS)
new_question_2 = ImageTk.PhotoImage(resized_question_2)
canvas.create_image(0,0, anchor='nw', image=new_question_2)
Button(win, image=new_question, command=message, background= '#FCEFD3', relief=GROOVE).place(x=467, y=277)

#Image:
label_8 = Label(win, text="Book Cover Image:", font=('arial', 10, 'bold'), background = '#FCEFD3')
label_8.place(x=370, y=302)


def showImage():
    fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image File", filetypes=(("All Files", "*.*"), ("JPG File", "*.jpg"), ("PNG file", "*.png")))
    img = Image.open(fln)
    img.thumbnail((80,70))
    img = ImageTk.PhotoImage(img)
    lbl.configure(image=img)
    lbl.image = img

lbl = Label(win, bg='white')
lbl.place(x=658, y=302)

btn= Button(win, text="Browse Image", command=showImage, bg='#B89B79')
btn.place(x=565, y=302)

#Improvements:
label_7 = Label(win, text="Add Review for your book:", font=('arial', 10, 'bold'), background = '#FCEFD3')
label_7.place(x=370, y=377)

text_1 = Text(win, width=23, height=5, font=('arial', 10))
text_1.place(x=565, y=382)


#Submission Button
def submit():
    global languages
    if book_name.get() == '':
        messagebox.showinfo("Warning!", "Please put in a book name")
    elif author_name.get() == '':
        messagebox.showinfo("Warning!", "Please put in a author name")
    elif language.get() == 'Select a language' and other.get() == '':
        messagebox.showinfo("Warning!", "Please put in a language")
    elif language.get() == 'Other' and other.get() == '':
        messagebox.showinfo("Warning!", "You have selected Other. \n\n Please put in language/s in field below")
    elif rating.get() == 'Select a rating':
        messagebox.showinfo("Warning!", "Please put in a rating")
    elif tags.get() == '':
        messagebox.showinfo("Warning!", "Please put in content tags")
    else:
        #Create a database or connect to one
        conn = sqlite3.connect('books.db')
        #Create cursor
        c = conn.cursor()
    
        #Insert into table
        c.execute("INSERT INTO books VALUES (:book_name, :author_name, :language, :other, :rating, :tags, :lbl)",
                {
                "book_name": book_name.get(), 
                "author_name": author_name.get(),
                "language": language.get(),
                "other": other.get(), 
                "rating": rating.get(),
                "tags": tags.get(),
                "lbl": lbl.cget('image')
                })
        book_name.delete(0,END)
        author_name.delete(0,END)
        other.delete(0,END)
        tags.delete(0,END)
        language.set("Select a language")
        rating.set("Select a rating")
        messagebox.showinfo("Yay!", "Thank you for your recommendation!")
        #Commit Changes
        conn.commit()

        #Close Connection
        conn.close()
    
    review = sqlite3.connect('review.db')
    i = review.cursor()
    
    i.execute("INSERT INTO changes VALUES (:change)",
            {
            "change": text_1.get(1.0, END)
            })
    
    text_1.delete(1.0, END)
    
    #Commit Changes
    review.commit()

    #Close Connection
    review.close()

submit_button = Button(win, text="Submit", relief=GROOVE, foreground='white', background='green', font=('arial', 20, "bold"), command=submit)
submit_button.place(x=485, y=485)

win.mainloop()