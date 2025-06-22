from tkinter import *
import sqlite3

win = Tk()
win.title("Books Database")
win.geometry("1100x600")

#Creating a database
conn = sqlite3.connect('books.db')

#Create cursor
c = conn.cursor()

#Delete Record Function
def delete():
    #Create a database or connect to one
    conn = sqlite3.connect('books.db')
    #Create cursor
    c = conn.cursor()
    
    #Delete a record
    c.execute("DELETE from books WHERE oid = "  + delete_box.get())
    
    #Commit Changes
    conn.commit()

    #Close Connection
    conn.close()

#Show Record Function
def show():
    #Create a database or connect to one
    conn = sqlite3.connect('books.db')
    #Create cursor
    c = conn.cursor()
    
    #Query the database
    c.execute("SELECT *, oid FROM books")
    records = c.fetchall()
    #print(records)
    
    #Loop through results
    print_records = ''
    for record in records:
        print_records += str(record) + '\n'
    
    show_label = Label(win, text=print_records)
    show_label.place(x=280, y=150)
    
    #Commit Changes
    conn.commit()

    #Close Connection
    conn.close()

#Delete Entry Field
delete_box = Entry(win, width=15)
delete_box.place(x=540, y=67)

delete_box_label = Label(win, text="Delete ID")
delete_box_label.place(x=480, y=67)


#Create Show Button
show_btn = Button(win, text="Show Books", command=show, width=30)
show_btn.place(x=450, y=25)

#Create Delete Button
delete_btn = Button(win, text="Delete Book", command=delete, width=30)
delete_btn.place(x=450, y=100)

win.mainloop()