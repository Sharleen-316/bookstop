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

img = (Image.open(r"Images/book_files/13.png"))
resized_image = img.resize((300,400), Image.ANTIALIAS)
new_image = ImageTk.PhotoImage(resized_image)
canvas.create_image(0,0, anchor='nw', image=new_image)

#Content Tags/Ratings/Language(s)
def message():
  messagebox.showinfo("Content Tags/Ratings/Language", "Content Tags: Romance, Adult Fiction, Sexual \nLanguage: English \nRating: E")
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
title_1 = Label(win, text='The Fine Print', font=('lucida bright', 20, 'bold'), bg='#B89B79', fg='#584A38')
title_1.place(x=680, y=50)

#Author
label_1 = Label(win, text='Author:', font=('arial', 10, 'bold'), bg='#FCEFD3')
label_1.place(x=580,y=100)

text_1 = Label(win, text="Lauren Asher", font=('arial', 10), bg='#FCEFD3')
text_1.place(x=655, y=100)

#Blurb
label_2 = Label(win, text="Blurb:", font=('arial', 10, 'bold'), bg='#FCEFD3')
label_2.place(x=580,y=125)

text_2 = Label(win, text="Rowan: I’m in the business of creating fairy tales. \nTheme parks. Production companies. Five-star hotels. \nEverything could be all mine if I renovated Dreamland. \nMy initial idea of hiring Zahra was good in theory, but \nthen I kissed her. Things spiraled out of control once \nI texted her using an alias. By the time I realized where \nI went wrong, it was too late. People like me don’t get \nhappy endings. Not when we’re destined to ruin them. \nZahra: After submitting a drunk proposal criticizing \nDreamland’s most expensive ride, I should have been \nfired. Instead, Rowan Kane offered me a dream job. \nThe catch? I had to work for the most difficult boss \nI’d ever met. Rowan was rude and completely off-limits, \nbut my heart didn’t care. At least not until I discovered \nhis secret. It was time to teach the billionaire that \nmoney couldn’t fix everything. Especially not us. ", font=('arial', 10), bg='#FCEFD3')
text_2.place(x=620,y=125)

#Rating Section
label_4 = Label(win, text="Your Rating: ", font=('arial', 10, 'bold'), bg='#FCEFD3')
label_4.place(x=580, y=400)

#1 Star
def rate_1():
  rating = "1"
  file = open("12_ratings.txt", "a")
  file.write(rating + '\n')
  file.close()
  messagebox.showinfo("Success!", "Thank you for your submission. You have rated 1 star.")
canvas = Canvas(win, width=35, height=35)
canvas.place(x=670, y=393)
star = Image.open(r"Images\other_images\star.png")
resized_star = star.resize((35,35), Image.ANTIALIAS)
new_star = ImageTk.PhotoImage(resized_star)
canvas.create_image(0,0, anchor='nw', image=new_star)
Button(win, image=new_star, command=rate_1).place(x=670, y=393)

#2 Star
def rate_2():
  rating = "2"
  file = open("12_ratings.txt", "a")
  file.write(rating + '\n')
  file.close()
  messagebox.showinfo("Success!", "Thank you for your submission. You have rated 2 stars.")
canvas = Canvas(win, width=35, height=35)
canvas.place(x=712, y=393)
new_star_2 = ImageTk.PhotoImage(resized_star)
canvas.create_image(0,0, anchor='nw', image=new_star_2)
Button(win, image=new_star_2, command=rate_2).place(x=712, y=393)

#3 Star
def rate_3():
  rating = "3"
  file = open("12_ratings.txt", "a")
  file.write(rating + '\n')
  file.close()
  messagebox.showinfo("Success!", "Thank you for your submission. You have rated 3 stars.")
canvas = Canvas(win, width=35, height=35)
canvas.place(x=754, y=393)
new_star_3 = ImageTk.PhotoImage(resized_star)
canvas.create_image(0,0, anchor='nw', image=new_star_3)
Button(win, image=new_star_3, command=rate_3).place(x=754, y=393)

#4 Star
def rate_4():
  rating = "4"
  file = open("12_ratings.txt", "a")
  file.write(rating + '\n')
  file.close()
  messagebox.showinfo("Success!", "Thank you for your submission. You have rated 4 stars.")
canvas = Canvas(win, width=35, height=35)
canvas.place(x=796, y=393)
new_star_4 = ImageTk.PhotoImage(resized_star)
canvas.create_image(0,0, anchor='nw', image=new_star_4)
Button(win, image=new_star_4, command=rate_4).place(x=796, y=393)

#5 Star
def rate_5():
  rating = "5"
  file = open("12_ratings.txt", "a")
  file.write(rating + '\n')
  file.close()
  messagebox.showinfo("Success!", "Thank you for your submission. You have rated 5 stars.")
canvas = Canvas(win, width=35, height=35)
canvas.place(x=838, y=393)
new_star_5 = ImageTk.PhotoImage(resized_star)
canvas.create_image(0,0, anchor='nw', image=new_star_5)
Button(win, image=new_star_5, command=rate_5).place(x=838, y=393)

#Average Rating Section
label_3 = Label(win, text="Rating:", font=('arial', 10, 'bold'), bg='#FCEFD3')
label_3.place(x=195, y=450)

rating = []
with open("12_ratings.txt") as file:
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
label_6.place(x=580, y=450)

def Restrict(e=None):
    string =  e.widget.get("1.0","end-1c")
    if 49 <= len(string):
        messagebox.showinfo("Character Limit Warning.", "You have used the maximum amount of characters allowed.")      

text_3 = Text(win, width=30, height=3, font=('arial', 10))
text_3.place(x=670, y=450)
text_3.bind('<Key>', Restrict)


def clear():
  text_3.delete(1.0, END)
clear_button = Button(win, text="Clear", relief = GROOVE, font=('arial', 10), background = '#B89B79', command=clear)
clear_button.place(x=708, y=505)

def post():
  review = text_3.get(1.0, 1.49)
  file = open("12_reviews.txt", "a")
  file.write(review + '\n')
  file.close()
  messagebox.showinfo("Posted!", "Thank you for your review!") 
  text_3.delete(1.0, END)
post_button = Button(win, text="Post", relief = GROOVE, font=('arial', 10), background = '#B89B79', command=post)
post_button.place(x=670, y=505)

reviews = []
with open("12_reviews.txt") as file:
   for line in file:
        reviews.append(line.strip())
        
for item in reviews:
    my_listbox.insert(END, item)

win.mainloop()