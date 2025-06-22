from tkinter import *
import sqlite3

win = Tk()
win.title("User Names Database")
win.geometry("1100x600")

#Creating a database
user = sqlite3.connect('user_name.db')

#Create cursor
r = user.cursor()

#Create table
#r.execute("""CREATE TABLE user (
#    user_name text
#    )""")


#Delete Record Function
def delete():
    #Creating a database
    user = sqlite3.connect('user_name.db')

    #Create cursor
    r = user.cursor()

    
    #Delete a record
    r.execute("DELETE from user WHERE oid = "  + delete_box.get())
    
    #Commit Changes
    user.commit()

    #Close Connection
    user.close()

#Show Record Function
def show():
    #Creating a database
    user = sqlite3.connect('user_name.db')

    #Create cursor
    r = user.cursor()

    #Query the database
    r.execute("SELECT *, oid FROM user")
    records = r.fetchall()
    #print(records)
    
    #Loop through results
    print_records = ''
    for record in records:
        print_records += str(record) + '\n'
    
    show_label = Label(win, text=print_records)
    show_label.place(x=460, y=150)
    
    #Commit Changes
    user.commit()

    #Close Connection
    user.close()

#Delete Entry Field
delete_box = Entry(win, width=15)
delete_box.place(x=540, y=67)

delete_box_label = Label(win, text="Delete ID")
delete_box_label.place(x=480, y=67)


#Create Show Button
show_btn = Button(win, text="Show Usernames", command=show, width=30)
show_btn.place(x=450, y=25)

#Create Delete Button
delete_btn = Button(win, text="Delete Usernames", command=delete, width=30)
delete_btn.place(x=450, y=100)

win.mainloop()