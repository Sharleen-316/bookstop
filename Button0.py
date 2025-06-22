#Review Screen Program
#Author: S Hossain
#Purpose: To view a selected book, see reviews and rate it
#Verison: 1.1 (Backup)

#Importing required libraries
from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import Image,ImageTk
import statistics
from tkinter import messagebox

#Window settings
win = Tk()
win.geometry("1100x600")
win.resizable(width=False, height=True) 
win.title("Bookstop")

ico = Image.open("images\other_images\small_logo.png")
bs_icon = ImageTk.PhotoImage(ico)
win.wm_iconphoto(False, bs_icon)

style = ttk.Style()
style.theme_use('clam')
style.configure("Vertical.TScrollbar", background='#FCEFD3', bordercolour="red", arrowcolor="light grey")

#Background
back_img = Image.open(r"Images\other_images\reviewbg.png")
back_img = back_img.resize((1100,800))
back = ImageTk.PhotoImage(back_img)

back_img = tk.Label(image=back)
back_img.image = Image
back_img.pack()

#Back button
def back_butt():
  win.destroy()
  import Bookshelf
back_button = Button(win, text="Back", relief = GROOVE, font=('arial', 10), background = '#B89B79', command=back_butt)
back_button.place(x=0, y=0)

#Image of book
canvas = Canvas(win, width=300, height=400, bg='#FCEFD3')
canvas.place(x=195, y=50)

img = (Image.open(r"Images/book_files/1.png"))
resized_image = img.resize((300,400), Image.ANTIALIAS)
new_image = ImageTk.PhotoImage(resized_image)
canvas.create_image(0,0, anchor='nw', image=new_image)


#Content Tags/Ratings/Language(s)
def message():
  messagebox.showinfo("Content Tags/Ratings/Language", "Content Tags: LGBT, Mental Health, Romance \nLanguage: English \nRating: T")
canvas = Canvas(win, width=20, height=20)
canvas.place(x=171, y=52)
question = Image.open(r"Images\other_images\question_mark.png")
resized_question = question.resize((20,20), Image.ANTIALIAS)
new_question = ImageTk.PhotoImage(resized_question)
canvas.create_image(0,0, anchor='nw', image=new_question)
Button(win, image=new_question, command=message, background= '#FCEFD3', relief=GROOVE).place(x=171, y=52)

#Save Book
canvas = Canvas(win, width=20, height=20)
canvas.place(x=171, y=77)
save = Image.open(r"Images\other_images\save_tag.png")
resized_save = save.resize((20,20), Image.ANTIALIAS)
new_save = ImageTk.PhotoImage(resized_save)
canvas.create_image(0,0, anchor='nw', image=new_save)
Button(win, image=new_save, command=None, background= '#FCEFD3', relief=GROOVE).place(x=171, y=77)

#Title of Book
title_1 = Label(win, text='History Is All You Left Me', font=('lucida bright', 20, 'bold'), bg='#B89B79', fg='#584A38')
title_1.place(x=580, y=50)

#Author
label_1 = Label(win, text='Author:', font=('arial', 10, 'bold'), bg='#FCEFD3')
label_1.place(x=580,y=100)

text_1 = Label(win, text="Adam Silvera", font=('arial', 10), bg='#FCEFD3')
text_1.place(x=655, y=100)

#Blurb
label_2 = Label(win, text="Blurb:", font=('arial', 10, 'bold'), bg='#FCEFD3')
label_2.place(x=580,y=125)

text_2 = Label(win, text="When Griffin's first love and ex-boyfriend,\n Theo, dies in a drowning accident, his\n universe implodes. Even though Theo had\n moved to California for college and \nstarted seeing Jackson, Griffin never \ndoubted Theo would come back to him \nwhen the time was right. But now, the \nfuture he's been imagining for himself has \ngone far off course. To make things worse, \nthe only person who truly understands his \nheartache is Jackson. But no \nmatter how much they open up to each \nother, Griffin's downward spiral continues. \nHe's losing himself in his obsessive \ncompulsions and destructive choices, and \nthe secrets he's been keeping are tearing \nhim apart. If Griffin is ever to rebuild his \nfuture, he must first confront his history, every last \nheartbreaking piece in the puzzle of his life.", font=('arial', 10), bg='#FCEFD3')
text_2.place(x=625,y=125)

#Rating Section
label_4 = Label(win, text="Your Rating: ", font=('arial', 10, 'bold'), bg='#FCEFD3')
label_4.place(x=580, y=450)

#1 Star
def rate_1():
  rating = "1"
  file = open("0_ratings.txt", "a")
  file.write(rating + '\n')
  file.close()
  messagebox.showinfo("Success!", "Thank you for your submission. You have rated 1 star.")
canvas = Canvas(win, width=35, height=35)
canvas.place(x=670, y=443)
star = Image.open(r"Images\other_images\star.png")
resized_star = star.resize((35,35), Image.ANTIALIAS)
new_star = ImageTk.PhotoImage(resized_star)
canvas.create_image(0,0, anchor='nw', image=new_star)
Button(win, image=new_star, command=rate_1).place(x=670, y=443)

#2 Star
def rate_2():
  rating = "2"
  file = open("0_ratings.txt", "a")
  file.write(rating + '\n')
  file.close()
  messagebox.showinfo("Success!", "Thank you for your submission. You have rated 2 stars.")
canvas = Canvas(win, width=35, height=35)
canvas.place(x=712, y=443)
new_star_2 = ImageTk.PhotoImage(resized_star)
canvas.create_image(0,0, anchor='nw', image=new_star_2)
Button(win, image=new_star_2, command=rate_2).place(x=712, y=443)

#3 Star
def rate_3():
  rating = "3"
  file = open("0_ratings.txt", "a")
  file.write(rating + '\n')
  file.close()
  messagebox.showinfo("Success!", "Thank you for your submission. You have rated 3 stars.")
canvas = Canvas(win, width=35, height=35)
canvas.place(x=754, y=443)
new_star_3 = ImageTk.PhotoImage(resized_star)
canvas.create_image(0,0, anchor='nw', image=new_star_3)
Button(win, image=new_star_3, command=rate_3).place(x=754, y=443)

#4 Star
def rate_4():
  rating = "4"
  file = open("0_ratings.txt", "a")
  file.write(rating + '\n')
  file.close()
  messagebox.showinfo("Success!", "Thank you for your submission. You have rated 4 stars.")
canvas = Canvas(win, width=35, height=35)
canvas.place(x=796, y=443)
new_star_4 = ImageTk.PhotoImage(resized_star)
canvas.create_image(0,0, anchor='nw', image=new_star_4)
Button(win, image=new_star_4, command=rate_4).place(x=796, y=443)

#5 Star
def rate_5():
  rating = "5"
  file = open("0_ratings.txt", "a")
  file.write(rating + '\n')
  file.close()
  messagebox.showinfo("Success!", "Thank you for your submission. You have rated 5 stars.")
canvas = Canvas(win, width=35, height=35)
canvas.place(x=838, y=443)
new_star_5 = ImageTk.PhotoImage(resized_star)
canvas.create_image(0,0, anchor='nw', image=new_star_5)
Button(win, image=new_star_5, command=rate_5).place(x=838, y=443)

#Average Rating Section
label_3 = Label(win, text="Rating:", font=('arial', 10, 'bold'), bg='#FCEFD3')
label_3.place(x=195, y=450)

rating = []
with open("0_ratings.txt") as file:
   for line in file:
        rating.append(int(line.strip()))

average = statistics.mean(rating)

Label(win, text=f'{round(average, 2)} stars, voted on by {len(rating)} bookstoppers', font=('arial', 10), bg='#FCEFD3').place(x=245, y=450)

#Reviews from other people
label_5 = Label(win, text="Reviews from fellow bookstoppers:", font=('arial', 10, 'bold'), bg='#FCEFD3')
label_5.place(x=195, y=485)


my_frame = Frame(win, bg='#FCEFD3') 
my_scrollbar = ttk.Scrollbar(my_frame, orient="vertical")
my_listbox = Listbox(my_frame, width=50, height=5, yscrollcommand=my_scrollbar.set, selectmode=SINGLE)

my_scrollbar.config(command=my_listbox.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)
my_frame.place(x=197,y=503)

my_listbox.pack()

#Reviews Section
label_6 = Label(win, text="Your Review:", font=('arial', 10, 'bold'), bg='#FCEFD3')
label_6.place(x=580, y=500)

def Restrict(e=None):
    string =  e.widget.get("1.0","end-1c")
    if 49 <= len(string):
        messagebox.showinfo("Character Limit Warning.", "You have used the maximum amount of characters allowed.")      

text_3 = Text(win, width=30, height=3, font=('arial', 10))
text_3.place(x=670, y=500)
text_3.bind('<Key>', Restrict)


def clear():
  text_3.delete(1.0, END)
clear_button = Button(win, text="Clear", relief = GROOVE, font=('arial', 10), background = '#B89B79', command=clear)
clear_button.place(x=708, y=555)

def post():
  review = text_3.get(1.0, 1.49)
  file = open("0_reviews.txt", "a")
  file.write(review + '\n')
  file.close()
  messagebox.showinfo("Posted!", "Thank you for your review!")
  text_3.delete(1.0, END) 
post_button = Button(win, text="Post", relief = GROOVE, font=('arial', 10), background = '#B89B79', command=post)
post_button.place(x=670, y=555)

reviews = []
with open("0_reviews.txt") as file:
   for line in file:
        reviews.append(line.strip())
        
for item in reviews:
    my_listbox.insert(END, item)

win.mainloop()