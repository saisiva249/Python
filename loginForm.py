from  tkinter import *
import os

def user_not_found():
    print("user not found")

def delete_loginScreen():
    loginsucess_Screen.destroy()

def login_success():
    global loginsucess_Screen
    loginsucess_Screen = Toplevel(parent_window)
    loginsucess_Screen.title("Sucess")
    loginsucess_Screen.geometry("150x100")
    Label(loginsucess_Screen, text = "Login Sucess").pack()
    Button(loginsucess_Screen, text="OK", command = delete_loginScreen).pack()


def login_verify():
    username = username_verify.get()
    password = password_verify.get()

    username_entry.delete(0,END)
    password_entry.delete(0,END)

    if((username != "") and (password != "")):
        login_success()
    else:
        user_not_found()


def login():
    global login_screen
    login_screen = Toplevel(parent_window)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen,text="Enter Details in below screen to login").pack()
    Label(login_screen,text="").pack()

    # these variables are used to bind to the entries for storing and retrieving the values.
    global username_verify
    global password_verify

    username_verify=StringVar()
    password_verify=StringVar()

    global username_entry
    global password_entry

    Label(login_screen,text="UserName *").pack()
    username_entry=Entry(login_screen,textvariable=username_verify)
    username_entry.pack()

    Label(login_screen,text="Password *").pack()
    password_entry=Entry(login_screen,textvariable=password_verify)
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
    parent_window.mainloop()

main_Screen()