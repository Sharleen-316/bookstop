from tkinter import *
import sqlite3

win = Tk()
win.title("Passwords Database")
win.geometry("1100x600")

#Creating a database
password = sqlite3.connect('password.db')

#Create cursor
r = password.cursor()

#Create table
#r.execute("""CREATE TABLE passwords (
#    password text
#    )""")


#Delete Record Function
def delete():
    #Creating a database
    password = sqlite3.connect('password.db')

    #Create cursor
    r = password.cursor()

    
    #Delete a record
    r.execute("DELETE from passwords WHERE oid = "  + delete_box.get())
    
    #Commit Changes
    password.commit()

    #Close Connection
    password.close()

#Show Record Function
def show():
    #Creating a database
    password = sqlite3.connect('password.db')

    #Create cursor
    r = password.cursor()

    #Query the database
    r.execute("SELECT *, oid FROM passwords")
    records = r.fetchall()
    #print(records)
    
    #Loop through results
    print_records = ''
    for record in records:
        print_records += str(record) + '\n'
    
    show_label = Label(win, text=print_records)
    show_label.place(x=520, y=150)
    
    #Commit Changes
    password.commit()

    #Close Connection
    password.close()

#Delete Entry Field
delete_box = Entry(win, width=15)
delete_box.place(x=540, y=67)

delete_box_label = Label(win, text="Delete ID")
delete_box_label.place(x=480, y=67)


#Create Show Button
show_btn = Button(win, text="Show Passwords", command=show, width=30)
show_btn.place(x=450, y=25)

#Create Delete Button
delete_btn = Button(win, text="Delete Passwords", command=delete, width=30)
delete_btn.place(x=450, y=100)

win.mainloop()