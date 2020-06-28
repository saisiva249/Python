#no need to install tkinter, as it is a standard python interface to the GUI toolkit
# for seeing a simple TK interface python -m tkinter
# Steps: importing tkinter
# Creating the GUi application main window
# adding widjets to GUI application
# adding main event loop to take action against each event triggered by user
#--import tkinter
#--top = tkinter.Tk()

from tkinter import *
from tkinter import ttk

parent_Window = Tk()
parent_Window.title("Sample Tkinter Controls")
parent_Window.geometry('500x250')
#frames are used to pack/ organise widgets like a container 
name_Frame = Frame(parent_Window)
name_Frame.pack()
buttons_Frame = Frame(parent_Window)
buttons_Frame.pack(side= BOTTOM)

#menu Bar
menubar = Menu(parent_Window)#main menu bar
#creating file menu items
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New")
filemenu.add_command(label = "Open")
filemenu.add_command(label = "Save")
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = parent_Window.quit)
#cascading first item created
menubar.add_cascade(label = "File", menu = filemenu)#placing the file inside the main menu bar

editmenu= Menu(menubar,tearoff=0)
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
#cascading item to menubar
menubar.add_cascade(label="Edit", menu= editmenu)
#adding menu bar to the parent window
parent_Window.config(menu=menubar)

#label
name_label = Label(name_Frame,text = "Hello", fg="green")
name_label.pack(side= LEFT)
#text box entry
name_entry = Entry(name_Frame, bd =5)
name_entry.pack(side=RIGHT)
#buttons
button1 = Button(buttons_Frame, text="Button1",fg="red", bg="orange")
button1.pack(side = LEFT)
button2 = Button(buttons_Frame, text="Button2", fg="black")
button2.pack(side = LEFT)
#numeric updown control, Spin Box
spin = Spinbox(buttons_Frame, from_=10, to=50, bd= 3)
spin.pack(side= LEFT)
#combobox
combo = ttk.Combobox(buttons_Frame, value=["C#","Python","JS"])
combo.pack(side= LEFT)
#checkBox
checkbox_control = Checkbutton(buttons_Frame,text="Agree to license")
checkbox_control.pack(side = RIGHT)

parent_Window.mainloop()