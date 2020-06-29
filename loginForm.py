from  tkinter import *

def login_verify():
    print("Login Verify")

def login():
    global login_screen
    login_screen = Toplevel(parent_window)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen,text="Enter Details in below screen to login").pack()
    Label(login_screen,text="").pack()

    global username
    global password

    username=StringVar()
    password=StringVar()

    Label(login_screen,text="UserName *").pack()
    username_entry=Entry(login_screen,textvariable=username)
    username_entry.pack()

    Label(login_screen,text="Password *").pack()
    password_entry=Entry(login_screen,textvariable=password)
    password_entry.pack()

    Label(login_screen, text = "").pack()
    Button(login_screen, text = "Login", width = 10, height = 1, command = login_verify).pack()

def register():
    print("Registeraton started")

def main_Screen():
    global parent_window
    parent_window = Tk()
    parent_window.geometry("300x250")
    parent_window.title("Welcome Screen")
    Label(text="Welcome Screen", bg="grey", width="300", height="2", font=("calibri",13)).pack()
    Label(text="").pack()
    Button(text="Login", width="30", height="2", command=login).pack()
    Label(text="").pack()
    Button(text="Register", width="30", height="2",command=register).pack()
    Label(text="").pack()
    parent_window.mainloop()

main_Screen()