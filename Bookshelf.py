#-- Bookshelf Test
#-- Levina Goenawan
#-- 18/05/2022

#---------------------#
#   Primary Imports
#---------------------#
from tkinter import *
from tkinter import ttk
from tkinter import messagebox #Shows message when error etc. When searching for book and not available states file not in directory.
from tkinter import filedialog
from PIL import ImageTk, Image
import os

#--------------------#
#  Global variables
#--------------------#
position_x = 50
position_y = 164
files = [] #creates list to replace your actual inputs for troubleshooting purposes
btn = [] #creates list to store the buttons ins
selected_button = None
last_bg = None

#---------------------#
#    Makes Interface
#---------------------#
win = Tk() #Win => to create a window
fram = Frame(win) #Win window is the parent window
win.title("Bookstop")
win.geometry("1100x600")
win.config(bg='#2E3550')
win.resizable(width=False, height=True)

ico = Image.open("images\other_images\small_logo.png")
bs_icon = ImageTk.PhotoImage(ico)
win.wm_iconphoto(False, bs_icon)

#-----------------------#
#   Open Review Page
#-----------------------#
def nextPage(rev_id):
    rev_id = str(rev_id)
    win.destroy()
    if rev_id == "Button0":
        import Button0
    elif rev_id == "Button1":
        import Button1
    elif rev_id == "Button2":
        import Button2
    elif rev_id == "Button3":
        import Button3
    elif rev_id == "Button4":
        import Button4
    elif rev_id == "Button5":
        import Button5
    elif rev_id == "Button6":
        import Button6
    elif rev_id == "Button7":
        import Button7
    elif rev_id == "Button8":
        import Button8
    elif rev_id == "Button9":
        import Button9
    elif rev_id == "Button10":
        import Button10
    elif rev_id == "Button11":
        import Button11
    elif rev_id == "Button12":
        import Button12
    elif rev_id == "Button13":
        import Button13
    elif rev_id == "Button14":
        import Button14
    elif rev_id == "Button15":
        import Button15
    elif rev_id == "Button16":
        import Button16 
    elif rev_id == "Button17":
        import Button17
    elif rev_id == "Button18":
        import Button18

def favPage():
    win.destroy()
    import Button1

def prevPage(): #Move back to login screen.
    win.destroy()
    import Login_screen

#---------------------#
#  Bookshelf border
#---------------------#
#-- Create a photoimage object of the image in the path
image1 = Image.open(r"images\other_images\Bookshelf_template.png")
bs = ImageTk.PhotoImage(image1)

label1 = Label(image=bs)
label1.image = Image

label1.place(x=0, y=145) #Position Image

#---------------------#
#    Book template
#---------------------#
#-- To change position of book button
def button_move():
    global position_x
    global position_y
    global x
    global y
    if int(position_x) > 830: #If position_x is over limit then position_x value returns to original 
        position_x = 50       #and position_y bookshelf value is added.
        position_y = position_y + 155
    else:
        position_x = position_x + 130
    x, y = position_x, position_y
    #coord()

#-- Obtaining coordinates per book. 
# Run once when more books come as quicker way to record book positions into txt file.

#f1 = open("coord_butt.txt") # Writing coordinates to text file
#def coord():
    #pos_id = str(pos_id)
    #with open("coord_butt.txt", "r") as c:
        #print(x,y)
        #c.write('{} {}\n'.format(x, y))

#-- Book template to insert for each book
f2 = open("book_id.txt")
ids = []
imgs = []
border = []

for line in f2: #Extracting number from txt file
    line = line.rstrip("\n")
    ids.append(line)
f2.close()

for i in range(19): #this just popultes a list as a replacement for your actual inputs for troubleshooting purposes
    files.append("Button"+str(i))

for i in range(len(files)): 
    bk = Image.open(f"images/book_files/{ids[i+1]}.png")
    resized_bk = bk.resize((100,120))
    imgs.append(ImageTk.PhotoImage(resized_bk))
    
    border.append(LabelFrame(win, bd = 0, background = "#D3D3D3"))
    btn.append(Button(border[i], text=files[i], image=imgs[-1], 
                    command=lambda c=i : [nextPage(btn[c].cget("text"))], 
                    relief=FLAT))
    btn[i].pack()
    border[i].place(x=position_x, y=position_y)
    button_move()

#---------------------#
#     Search bar
#---------------------#
#-- Book data
options = ["Story Title", "Author"]

books = ["History is all you left me", "Chinese Cinderella", "Heartstopper", 
         "Pride & Prejudice", "Red Pyramid", "The Book Thief", "Little Women", 
         "The Complete Sherlock Holmes", "The Cruel Prince", "The Wicked King", 
         "The Queen of Nothing", "Twisted Hate", "The Fine Print", "Red, White & Royal Blue",
         "Captive Prince", "Wolfsong", "The House in the Cerulean Sea", "Vital Science", "Star Wars Kenobi"]

authors = ["Adam Silvera", "Adeline Yen Mah", "Alice Oseman", "Jane Austen", 
           "Rick Riordan", "Markus Zusak", "Louisa M. Alcott", "Sir Arthur Conan Doyle",
           "Holly Black", "Ana Huang", "Lauren Asher", "Casey McQuiston", "C.S. Pacat",
           "TJ Klune", "Dr Karl Kruszelnicki", "John Jackson Miller"]

#-- Category to search options
def selected(event): # Be placed in the side to restrict user search options by category.
    my_list.delete(0,END)
    if my_combo.get() == "Story Title":
        for item in books:
            my_list.insert(END, item)
    if my_combo.get() == "Author":
        for item in authors:
            my_list.insert(END, item)

#-- Dropbox
my_combo = ttk.Combobox(win, value=options, width=9, font=("Helvetica", 9), state= "readonly")
my_combo.set('Story Title')
my_combo.bind('<<ComboboxSelected>>', selected)
my_combo.place(x=350, y=10)

#-- Find book function
def search_items():
    search_value = variable.get()
    if search_value == "" or search_value == " ":
        combo['values'] = item_names
    else:
        value_to_display = []
        for value in item_names:
            if search_value in value:
                value_to_display.append(value)
        combo['values'] = value_to_display

#-- Autofill search function
def update(data):
    #Clear the listbox
    my_list.delete(0, END)
    
    #Add toppings to listbox
    for item in data:
        my_list.insert(END, item)

# Update entry box with listbox clicked
def fillout(e):
    #Delete whatever is in the entry box
    my_entry.delete(0, END)
    
    #Add clicked list item to entry box
    my_entry.insert(0, my_list.get(ACTIVE))

#Creat function to check entry vs listbox
def check(e):
    #grab what was typed
    typed = my_entry.get()
    
    if typed == '':
        if my_combo.get() == "Story Title":
            data = books
        if my_combo.get() == "Author":
            data = authors
    else:
        data = []
        if my_combo.get() == "Story Title":
            for item in books:
                if typed.lower() in item.lower():
                    data.append(item)
        if my_combo.get() == "Author":
            for item in authors:
                if typed.lower() in item.lower():
                    data.append(item)
    
    #update out listbox with selected items
    update(data)

#-- Create an entry box
my_entry = Entry(win, font=("Helvetica", 11), width=34)
my_entry.place(x=439, y=10)

#-- Obtaining coordinates
file = open('coord_butt.txt')
content = file.readlines()

#-- Image appear function
global locate_img
img = Label(image = None)

def clear_label_image():
    img.config(image = '')

def find_image():
    locate_img = Image.open(r"Images\other_images\search.png")
    locate_img = locate_img.resize((30,30))
    locate = ImageTk.PhotoImage(locate_img)

    img.image = locate
    img.config(image = locate)
    img.place(x=coord_x, y=coord_y)

def printValue():
    global num
    pentry = my_entry.get()
    if my_combo.get() == "Story Title":
        datafile = open("book_list.txt")
    if my_combo.get() == "Author":
        datafile = open("author_list.txt")
    for num, line in enumerate(datafile,0):
        if pentry in line:
            return True
    return False
    findCoord()

def obt_coord():
    global pos_img
    global coord_x
    global coord_y
    with open('coord_butt.txt') as f1:
        var = content[num]
        x, y = var.split()
        coord_x = int(x)
        coord_y = int(y)
    find_image()

def click(event): #Click clear image function
    clear_label_image()

#When mouse click initiates function to clear icon
win.bind("<Button-1>", click) 
win.bind("<Button-2>", click)
win.bind("<Button-3>", click)

def findCoord():
    if my_entry.get() == '':
        messagebox.showinfo("Warning!", "Search bar empty. Please enter book/author.")
    elif my_entry.get() != '' and printValue():
        obt_coord()
    else:
        if my_combo.get() == "Story Title":
            messagebox.showinfo("Not available", "Sorry the book you searched is not available..." +
                            "\n\n Want other bookstoppers to know? Add into the forum - located in the top right")
        if my_combo.get() == "Author":
            messagebox.showinfo("Not available", "Sorry the author you searched is not available..." +
                            "\n\n Want other bookstoppers to know? Add into the forum - located in the top right")
        
def enter_func(event):
    if my_entry.get() == '':
        messagebox.showinfo("Warning!", "Search bar empty. Please enter book/author.")
    elif my_entry.get() != '' and printValue():
        obt_coord()
    else:
        if my_combo.get() == "Story Title":
            messagebox.showinfo("Warning!", "Sorry the book you searched is not available..." +
                            "\n\n Want other bookstoppers to know? \n\n Add to forum - located in the top right")
        if my_combo.get() == "Author":
            messagebox.showinfo("Warning!", "Sorry the author you searched is not available..." +
                            "\n\n Want other bookstoppers to know? \n\n Add to the forum - located in the top right")

#-- Create a listbox
my_frame = Frame(win, bg='#FCEFD3')
my_list = Listbox(my_frame, width=60, height=6)

#-- Add scroll bar on listbox
scrollbar = Scrollbar(my_frame, orient="vertical")
scrollbar.config(command=my_list.yview)
scrollbar.pack(side = RIGHT, fill = Y)

my_list.pack()

my_frame.place(x=360, y=35)

my_list.config(yscrollcommand = scrollbar.set) #Attaching Listbox to Scrollbar

#-- Create Find button
butt1 = Button(win, text='Find', command=findCoord, relief=SOLID, font=("Helvetica", 9), borderwidth=0) 
butt1.place(x=719, y=10)

update(books) # Add the books to out list

my_entry.bind('<Return>', enter_func) #When press enter can search novel without clicking find button
my_list.bind("<<ListboxSelect>>", fillout) # Creat a binding on the listbox onclick
my_entry.bind("<KeyRelease>", check) #Create a binding on the entry box

#----------------------#
#       Icons
#----------------------#
#Themes
ab = Image.open(r"images\other_images\add_b.png")
resized_ab = ab.resize((27,27))
new_ab = ImageTk.PhotoImage(resized_ab)
ag = Image.open(r"images\other_images\add_g.png")
resized_ag = ag.resize((27,27))
new_ag = ImageTk.PhotoImage(resized_ag)
ar = Image.open(r"images\other_images\add_r.png")
resized_ar = ar.resize((27,27))
new_ar = ImageTk.PhotoImage(resized_ar)
ay = Image.open(r"images\other_images\add_y.png")
resized_ay = ay.resize((27,27))
new_ay = ImageTk.PhotoImage(resized_ay)

sfb = Image.open(r"images\other_images\saved_b.png")
resized_sfb = sfb.resize((27,27))
new_sfb = ImageTk.PhotoImage(resized_sfb)
sfg = Image.open(r"images\other_images\saved_g.png")
resized_sfg = sfg.resize((27,27))
new_sfg = ImageTk.PhotoImage(resized_sfg)
sfr = Image.open(r"images\other_images\saved_r.png")
resized_sfr = sfr.resize((27,27))
new_sfr = ImageTk.PhotoImage(resized_sfr)
sfy = Image.open(r"images\other_images\saved_y.png")
resized_sfy = sfy.resize((27,27))
new_sfy = ImageTk.PhotoImage(resized_sfy)

sb = Image.open(r"images\other_images\settings_b.png")
resized_sb = sb.resize((27,27))
new_sb = ImageTk.PhotoImage(resized_sb)
sg = Image.open(r"images\other_images\settings_g.png")
resized_sg = sg.resize((27,27))
new_sg = ImageTk.PhotoImage(resized_sg)
sr = Image.open(r"images\other_images\settings_r.png")
resized_sr = sr.resize((27,27))
new_sr = ImageTk.PhotoImage(resized_sr)
sy = Image.open(r"images\other_images\settings_y.png")
resized_sy = sy.resize((27,27))
new_sy = ImageTk.PhotoImage(resized_sy)

ub = Image.open(r"images\other_images\user_b.png")
resized_ub = ub.resize((27,27))
new_ub = ImageTk.PhotoImage(resized_ub)
ug = Image.open(r"images\other_images\user_g.png")
resized_ug = ug.resize((27,27))
new_ug = ImageTk.PhotoImage(resized_ug)
ur = Image.open(r"images\other_images\user_r.png")
resized_ur = ur.resize((27,27))
new_ur = ImageTk.PhotoImage(resized_ur)
uy = Image.open(r"images\other_images\user_y.png")
resized_uy = uy.resize((27,27))
new_uy = ImageTk.PhotoImage(resized_uy)

#-- Add Icon
def forum_page():
    win.destroy()
    import Forum_Page

icon_c = Canvas(win, width=200, height=200)
icon_c.place(x=961, y=9)
add = Image.open(r"images\other_images\add.png")
resized_add = add.resize((27,27))
new_add = ImageTk.PhotoImage(resized_add)
add_b = Button(icon_c, image=new_add, command=forum_page, relief=SOLID, borderwidth=0, background='#D1BFAA') #Connect to forum page when user clicks.
add_b.grid()

#-- Saved Files Icon
icon_c = Canvas(win, width=200, height=200)
icon_c.place(x=994, y=9)
saved = Image.open(r"images\other_images\saved_files.png")
resized_saved = saved.resize((27,27))
new_saved = ImageTk.PhotoImage(resized_saved)
saved_b = Menubutton(icon_c, image=new_saved, background='#D1BFAA') #Extends to a list of the saved images
saved_b.grid()

saved_b.menu = Menu(saved_b, tearoff=False) # Creating menubutton when user clicks opens options
saved_b["menu"] = saved_b.menu

blaVar = IntVar()

saved_b.menu.add_checkbutton(label="Saved Book 1", variable=blaVar) #Whenever user saves book will add to list
saved_b.menu.add_checkbutton(label="Saved Book 2", variable=blaVar)
saved_b.menu.add_checkbutton(label="Saved Book 3", variable=blaVar)

#-- Settings Icon
icon_c = Canvas(win, width=200, height=200)
icon_c.place(x=1027, y=9)
settings = Image.open(r"images\other_images\settings.png")
resized_settings = settings.resize((27,27))
new_settings = ImageTk.PhotoImage(resized_settings)
settings_b = Menubutton(icon_c, image=new_settings, background='#D1BFAA') #Extends to other information (quick settings)
settings_b.grid()

settings_options = Menu(settings_b, tearoff=False)
sub_settings = Menu(settings_options, tearoff=False) #Add new menubar

settings_b.config(menu=settings_options)
settings_options.add_cascade(label='Change Theme', menu=sub_settings)
settings_b.pack()

bg = 0
def bg_num(): # Writing coordinates into text file
    global bg
    bg = str(bg)
    with open("bg_value.txt", "a+") as f3:
        f3.write(bg + "\n")
        f3.close()

def og_bg():
    global bg
    if bg == '0':
        messagebox.showinfo("Warning!", "Theme has not been changed. Please first change theme.")
    else:
        win.config(bg='#2E3550')
        add_b.config(image=new_add, background='#D1BFAA') #Changes image
        saved_b.config(image=new_saved, background='#D1BFAA')
        settings_b.config(image=new_settings, background='#D1BFAA')
        if user_b.image == new_user:
            user_b.config(image=new_user, background='#D1BFAA')
        elif user_b.image == new_ug:
            user_b.config(image=new_user, background='#D1BFAA')
        elif user_b.image == new_ur:
            user_b.config(image=new_user, background='#D1BFAA')
        elif user_b.image == new_uy:
            user_b.config(image=new_user, background='#D1BFAA')
        elif user_b.image == new_ub:
            user_b.config(image=new_user, background='#D1BFAA')
        bg = 0
        bg_num()

def darkgreen_bg():
    global bg
    win.config(bg='#003C39')
    add_b.config(image=new_ag, background='#D1BFAA') #Changes image
    saved_b.config(image=new_sfg, background='#D1BFAA')
    settings_b.config(image=new_sg, background='#D1BFAA')
    if user_b.image == new_user:
        user_b.config(image=new_ug, background='#D1BFAA')
    elif user_b.image == new_ug:
        user_b.config(image=new_ug, background='#D1BFAA')
    elif user_b.image == new_ur:
        user_b.config(image=new_ug, background='#D1BFAA')
    elif user_b.image == new_uy:
        user_b.config(image=new_ug, background='#D1BFAA')
    elif user_b.image == new_ub:
        user_b.config(image=new_ug, background='#D1BFAA')
    bg = 1
    bg_num()

def burgundy_bg():
    global bg
    win.config(bg='#822828')
    add_b.config(image=new_ar, background='#D1BFAA') #Changes image
    saved_b.config(image=new_sfr, background='#D1BFAA')
    settings_b.config(image=new_sr, background='#D1BFAA')
    if user_b.image == new_user:
        user_b.config(image=new_ur, background='#D1BFAA')
    elif user_b.image == new_ug:
        user_b.config(image=new_ur, background='#D1BFAA')
    elif user_b.image == new_ur:
        user_b.config(image=new_ur, background='#D1BFAA')
    elif user_b.image == new_uy:
        user_b.config(image=new_ur, background='#D1BFAA')
    elif user_b.image == new_ub:
        user_b.config(image=new_ur, background='#D1BFAA')
    bg = 2
    bg_num()

def yellow_bg():
    global bg
    win.config(bg="#DAD135")
    add_b.config(image=new_ay, background='#705F4D') #Changes image
    saved_b.config(image=new_sfy, background='#705F4D')
    settings_b.config(image=new_sy, background='#705F4D')
    if user_b.image == new_user:
        user_b.config(image=new_uy, background='#705F4D')
    elif user_b.image == new_ug:
        user_b.config(image=new_uy, background='#D1BFAA')
    elif user_b.image == new_ur:
        user_b.config(image=new_uy, background='#D1BFAA')
    elif user_b.image == new_uy:
        user_b.config(image=new_uy, background='#D1BFAA')
    elif user_b.image == new_ub:
        user_b.config(image=new_uy, background='#D1BFAA')
    bg = 3
    bg_num()
    
def blue_bg():
    global bg
    win.config(bg="#0E3D71")
    add_b.config(image=new_ab, background='#D1BFAA') #Changes image
    saved_b.config(image=new_sfb, background='#D1BFAA')
    settings_b.config(image=new_sb, background='#D1BFAA')
    if user_b.image == new_user:
        user_b.config(image=new_ub, background='#D1BFAA')
    elif user_b.image == new_ug:
        user_b.config(image=new_ub, background='#D1BFAA')
    elif user_b.image == new_ur:
        user_b.config(image=new_ub, background='#D1BFAA')
    elif user_b.image == new_uy:
        user_b.config(image=new_ub, background='#D1BFAA')
    elif user_b.image == new_ub:
        user_b.config(image=new_ub, background='#D1BFAA')
    bg = 4
    bg_num()

darkgreen = Image.open(r"images\other_images\darkgreen.png")
resized_darkgreen = darkgreen.resize((60,27))
new_darkgreen = ImageTk.PhotoImage(resized_darkgreen)
burgundy = Image.open(r"images\other_images\burgundy.png")
resized_burgundy = burgundy.resize((60,27))
new_burgundy = ImageTk.PhotoImage(resized_burgundy)
blue = Image.open(r"images\other_images\blue.png")
resized_blue = blue.resize((60,27))
new_blue = ImageTk.PhotoImage(resized_blue)
yellow = Image.open(r"images\other_images\yellow.png")
resized_yellow = yellow.resize((60,27))
new_yellow = ImageTk.PhotoImage(resized_yellow)

#Menu button for themes
sub_settings.add_command(image=new_burgundy, command=burgundy_bg)
sub_settings.add_command(image=new_yellow, command=yellow_bg)
sub_settings.add_command(image=new_blue, command=blue_bg)
sub_settings.add_command(image=new_darkgreen, command=darkgreen_bg)

sub_settings.add_separator() # Adds line to seperate buttons
sub_settings.add_command(label='Reset theme', command=og_bg)

#-- User Icon
global user_b
icon_c = Canvas(win, width=200, height=200, background='#2E3550')
icon_c.place(x=1060, y=9)
user = Image.open(r"images\other_images\user_img.png")
resized_user = user.resize((27,27))
new_user = ImageTk.PhotoImage(resized_user)
user_b = Menubutton(icon_c, image=new_user, background='#D1BFAA') #May add function where user can change image
user_b.image = new_user
user_b.grid()

user_options = Menu(user_b, tearoff=False)
sub_user = Menu(user_options, tearoff=False)

user_b.config(menu=user_options)
user_options.add_cascade(label='Customize Profile', menu=sub_user)

def change_profile():
    fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image File", filetypes=(("JPG File", "*.jpg"), ("PNG file", "*.png")))
    profile = Image.open(fln)
    resized_profile = profile.resize((27,27))
    new_profile = ImageTk.PhotoImage(resized_profile)
    user_b.config(image=new_profile)
    user_b.image = new_profile

def reset_user():
    global bg
    if user_b.image == new_user:
        messagebox.showinfo("Warning!", "Profile has not been changed. Please first change image.")
    elif bg == '0':
        user_b.config(image=new_user, background='#D1BFAA')
        user_b.image = new_user
    elif bg == '1':
        user_b.config(image=new_ug, background='#D1BFAA')
        user_b.image = new_ug
    elif bg == '2':
        user_b.config(image=new_ur, background='#D1BFAA')
        user_b.image = new_ur
    elif bg == '3':
        user_b.config(image=new_uy, background='#705F4D')
        user_b.image = new_uy
    elif bg == '4':
        user_b.config(image=new_ub, background='#D1BFAA')
        user_b.image = new_ub

sub_user.add_command(label='Select images', command=change_profile)
sub_user.add_separator()
sub_user.add_command(label='Reset profile', command=reset_user)

def help_screen():
    messagebox.showinfo("Help", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur facilisis ligula quam, non maximus eros ultrices eget. Maecenas in orci dictum, blandit ipsum ut, mattis urna. Vestibulum sed arcu sed odio tincidunt hendrerit vestibulum ac tortor. Proin et suscipit ex, at blandit odio. Pellentesque vestibulum laoreet ipsum, ac rhoncus lectus euismod et. Curabitur posuere iaculis nibh, a dictum nisi sagittis sit amet. Vivamus posuere nunc nibh, eget varius lorem fringilla vel. Maecenas luctus, erat sed tempus imperdiet, dui augue malesuada neque, at lobortis mi felis et risus. Pellentesque eu porttitor tellus. Donec a scelerisque nisl, id mattis tellus. Phasellus sed ligula sollicitudin, auctor mi ut, varius nibh. Aliquam elementum id est sit amet porta. Donec odio nisl, aliquam id fermentum et, varius a quam.\n\nSed pulvinar mauris vel erat lacinia, nec condimentum diam rutrum. Aenean consequat quam vel turpis gravida feugiat. Suspendisse et tristique quam. Duis ut ante tincidunt, dapibus ipsum et, cursus neque. Sed luctus tincidunt justo eget tristique. Nunc gravida lacus at lectus accumsan, a mattis urna tempus. Ut pharetra, lorem in semper euismod, sapien nulla maximus est, ac rhoncus elit tortor ut nibh. In auctor, ipsum eget mollis rhoncus, magna libero pretium ligula, vitae dignissim dolor arcu in quam. Curabitur dolor dui, placerat sed diam pretium, varius convallis libero. Pellentesque mattis lorem a porta blandit. Aliquam eget rutrum odio, vestibulum rutrum sapien. Nunc id leo ex. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Morbi faucibus sem sem, id egestas massa molestie eu. Suspendisse laoreet ante quis nisl molestie, eget tempor tellus maximus. Cras ultrices laoreet nibh, eget varius odio tincidunt a.") 

user_options.add_command(label='Help', command=help_screen) #Create pop up screen with loral esem
user_options.add_separator() # Adds line to seperate buttons
user_options.add_command(label='Logout', command=prevPage) #Exit screen and return to home screen
user_b.pack()

#------------------------#
#    Book of the month
#------------------------#
#-- Create a photoimage object of the image in the path
bm = Image.open(r"images\other_images\book_month.png")
bm_img = ImageTk.PhotoImage(bm)
bm_final = Label(image=bm_img, background="grey", bd=1)
bm_final.place(x=12, y=9) #Position Image

#-- Book of the month button
# Literally create a new book file for the favourite book as we cannot reuse the same image apparently.
logo = Image.open(r"images\other_images\fav_book.png") 
logo = logo.resize((100,120))
img1 = ImageTk.PhotoImage(logo)

label1 = Button(image=img1, command=favPage, relief=SOLID, bd=0)
label1.place(x=85, y=12)

#----------------#
#-   Run code
#----------------#
with open("bg_value.txt", "r") as f4:
    last_line = f4.readlines()[-1]
print(last_line)
last_line = int(last_line)
if last_line == int(0):
    og_bg()
elif last_line == int(1):
    darkgreen_bg()
elif last_line == int(2):
    burgundy_bg()
elif last_line == int(3):
    yellow_bg()
elif last_line == int(4):
    blue_bg()
win.mainloop()