#-- Bookstop -> Login Screen
#-- Levina Goenawan
#-- 09/06/2022

#---------------------#
#   Primary Imports
#---------------------#
from tkinter import *
import tkinter as tk
from tkinter import messagebox #Shows message when error etc. When searching for book and not available states file not in directory.
from PIL import ImageTk, Image
import os
import sqlite3

#---------------------#
#    Makes Interface
#---------------------#
main_screen = Tk()
def main_account_screen():
    main_screen.title("Bookstop")
    main_screen.geometry("1100x600")
    main_screen.config(bg='#84634B')
    main_screen.resizable(width=False, height=False)
    
    ico = Image.open("images\other_images\small_logo.png")
    bs_icon = ImageTk.PhotoImage(ico)
    main_screen.wm_iconphoto(False, bs_icon)

#-----------------------#
#     Register page
#-----------------------#
def register_user():
    if username_entry.get() == '':
        messagebox.showinfo("Warning!", "Invalid Username.")
    elif password_entry.get() == '':
        messagebox.showinfo("Warning!", "Invalid Password.")
    elif reenterpw_entry.get() == '':
        messagebox.showinfo("Warning!", "Verify Password needed.")
    elif password_entry.get() != reenterpw_entry.get():
        messagebox.showinfo("Warning!", "The password you entered is incorrect. Please try again.")
    elif password_entry.get() == reenterpw_entry.get():
        user_db = sqlite3.connect('user_name.db')

        r = user_db.cursor()

        #Insert into table
        r.execute("INSERT INTO user VALUES (:user_name)",
                {
                "user_name": username.get()
                })
        #Commit Changes
        user_db.commit()

        #Close Connection
        user_db.close()
        
        password_db = sqlite3.connect('password.db')

        r = password_db.cursor()

        #Insert into table
        r.execute("INSERT INTO passwords VALUES (:password)",
                {
                "password": password.get()
                })
        #Commit Changes
        password_db.commit()

        #Close Connection
        password_db.close()
 
        username_entry.delete(0, END)
        password_entry.delete(0, END)
        reenterpw_entry.delete(0, END)
        
        # set a label for showing success information on screen 
        register_success = Label(register_screen, text="Registration Success", fg="grey", font=("calibri", 13))
        register_success.place(x=80, y=200)

def register(): 
    global register_screen
    register_screen = Toplevel(main_screen) 
    register_screen.title("Register")
    register_screen.geometry("300x250")
    register_screen.config(bg='#84634B')
    register_screen.resizable(width=False, height=False) #Prevents user from adjusting screen
    
    ico = Image.open("images\other_images\small_logo.png")
    bs_icon = ImageTk.PhotoImage(ico)
    register_screen.wm_iconphoto(False, bs_icon)
    
    label1 = Label(register_screen, text="Please enter details below to register...", bg="#DDC7A0") # Set label for user's instruction
    label1.place(x=50, y=35)

    global username
    global password
    global reenter_password

    username = StringVar()
    password = StringVar()
    reenter_password = StringVar()

    global username_entry
    global password_entry
    global reenterpw_entry

    username_lable = Label(register_screen, text="Username * ", bg="#DDC7A0") # Set username label
    username_lable.place(x=25, y=75)
    
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.place(x=145, y=75)
    
    password_lable = Label(register_screen, text="Password * ", bg="#DDC7A0") # Set password label
    password_lable.place(x=25, y=104)
    
    password_entry = Entry(register_screen, textvariable=password, show='*') # Set password entry
    password_entry.place(x=145, y=104)

    password_reenter = Label(register_screen, text="Re-enter password * ", bg="#DDC7A0") # Set password label
    password_reenter.place(x=25, y=133)
    
    reenterpw_entry = Entry(register_screen, textvariable=reenter_password, show='*') # Set password entry
    reenterpw_entry.place(x=145, y=133)

    label2 = Button(register_screen, text="Register", width=10, height=1, bg="#DDC7A0", 
                    relief=FLAT, bd=1, command = register_user) # Set register button
    label2.place(x=112, y=172)

#-------------------------#
#    Login Verification
#-------------------------#
def user_not_found():
    messagebox.showinfo("Warning!", "User not found") 

def login_success():
    main_screen.destroy()
    import Gif

def password_not_recognised():
    messagebox.showinfo("Warning!", "Invalid Password")

#------------------------#
#       Login Page
#------------------------#
def login_verify():
    user_db = sqlite3.connect('user_name.db')

    r = user_db.cursor()
    global password_login_entry
    
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
    
    r.execute("SELECT *, oid FROM user")
    records = r.fetchall()
    #print(records)
    
    #Loop through results
    print_records = ''
    for record in records:
        print_records += str(record) + '\n'
    
    
    if username1 in record:
        password_db = sqlite3.connect('password.db')

        r = password_db.cursor()
        r.execute("SELECT *, oid FROM passwords")
        records = r.fetchall()
        #print(records)
        
        print_records = ''
        for record in records:
            print_records += str(record) + '\n'
        
        if password1 in record:
            login_success()
        else:
            password_not_recognised()
        #Commit Changes
        password_db.commit()
        #Close Connection
        password_db.close()
    else:
        user_not_found()
    
    #Commit Changes
    user_db.commit()

    #Close Connection
    user_db.close()

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    login_screen.config(bg='#84634B')
    login_screen.resizable(width=False, height=False)
    label3 = Label(login_screen, text="Please enter details below to login...", bg="#DDC7A0")
    label3.place(x=53, y=35)
    
    ico = Image.open("images\other_images\small_logo.png")
    bs_icon = ImageTk.PhotoImage(ico)
    login_screen.wm_iconphoto(False, bs_icon)
    
    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    username_lable2 = Label(login_screen, text="Username *", bg="#DDC7A0")
    username_lable2.place(x=43, y=85)
    
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.place(x=130, y=85)
    
    password_lable2 = Label(login_screen, text="Password * ", bg="#DDC7A0")
    password_lable2.place(x=43, y=114)
    
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.place(x=130, y=114)
    
    label4 = Button(login_screen, text="Login", width=10, height=1, bg="#DDC7A0", relief=FLAT, 
                    bd=1, command=login_verify)
    label4.place(x=112, y=162)

#----------------------#
#       Sign up
#----------------------#
#-- Create a photoimage object of the image in the path
box_img = Image.open(r"images\other_images\bg_brown.png")
box_img = box_img.resize((1100,600))
resize_box_img = ImageTk.PhotoImage(box_img)

box_img = tk.Label(image=resize_box_img)
box_img.image = Image
box_img.pack()

#-- Create Login Button 
login_butt = Button(text="Login", height="3", width="30", background="#E3E4E2", 
                    highlightbackground = "#84634B", bd=1, relief=SOLID, command=login)
login_butt.place(x=430, y=330)
 
#-- Create a register button
register_butt = Button(text="Register", height="3", width="30", background="#E3E4E2", 
                       highlightbackground = "#84634B", bd=1, relief=SOLID, command=register)
register_butt.place(x=430, y=395)

#------------------------#
#       Logo Image
#------------------------#
#-- Create a photoimage object of the image in the path
logo = Image.open(r"images\other_images\logo.png")
logo = logo.resize((205,200))
img1 = ImageTk.PhotoImage(logo)
label1 = tk.Label(image=img1, background="black", bd=1)
label1.image = Image

label1.place(x=436, y=110) #Position Image

#----------------#
#    Run code
#----------------#
main_account_screen()
main_screen.mainloop() 

