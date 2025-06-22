from tkinter import *
import sqlite3

win = Tk()
win.title("Bookstop Database")
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
    show_label.grid(row=4, column=0, columnspan=2)
    
    #Commit Changes
    conn.commit()

    #Close Connection
    conn.close()

#Delete Entry Field
delete_box = Entry(win, width=30)
delete_box.grid(row=2, column=1, pady=5)

delete_box_label = Label(win, text="Delete ID")
delete_box_label.grid(row=2, column=0, pady=5)


#Create Show Button
show_btn = Button(win, text="Show Books", command=show)
show_btn.grid(row=1, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

#Create Delete Button
delete_btn = Button(win, text="Delete Record", command=delete)
delete_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=136)

win.mainloop()