from tkinter import *
import sqlite3

win = Tk()
win.title("Review Database")
win.geometry("1100x600")

#Creating a database
review = sqlite3.connect('review.db')

#Create cursor
i = review.cursor()

#Delete Record Function
def delete():
    #Create a database or connect to one
    review = sqlite3.connect('review.db')
    #Create cursor
    i = review.cursor()
    
    #Delete a record
    i.execute("DELETE from changes WHERE oid = "  + delete_box.get())
    
    #Commit Changes
    review.commit()

    #Close Connection
    review.close()

#Show Record Function
def show():
    #Create a database or connect to one
    review = sqlite3.connect('review.db')
    #Create cursor
    i = review.cursor()
    
    #Query the database
    i.execute("SELECT *, oid FROM changes")
    records = i.fetchall()
    #print(records)
    
    #Loop through results
    print_records = ''
    for record in records:
        print_records += str(record) + '\n'
    
    show_label = Label(win, text=print_records)
    show_label.place(x=330, y=150)
    
    #Commit Changes
    review.commit()

    #Close Connection
    review.close()

#Delete Entry Field
delete_box = Entry(win, width=15)
delete_box.place(x=540, y=67)

delete_box_label = Label(win, text="Delete ID")
delete_box_label.place(x=480, y=67)


#Create Show Button
show_btn = Button(win, text="Show Reviews", command=show, width=30)
show_btn.place(x=450, y=25)

#Create Delete Button
delete_btn = Button(win, text="Delete Reviews", command=delete, width=30)
delete_btn.place(x=450, y=100)

win.mainloop()