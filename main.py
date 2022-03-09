#   a214_simple_window1.py
#   A program creates a window on your screen using Tkinter

import tkinter as tk

#buttons
# main window
root = tk.Tk()
root.wm_geometry("500x500")
root.title('authentrication')

frame_login = tk.Frame(root)
frame_login.grid(row=0, column=0, sticky="news")


frameAuth = tk.Frame(root)
frameAuth.grid(row=0, column=0, sticky="news")

frameGridTest = tk.Frame(root)
frameGridTest.grid(row=0,column=0,sticky="news")


def button():
    frameAuth.tkraise()
    lblPassword.config(text="password: " + ent_pass.get())


lbl_username = tk.Label(frame_login, text='userenanem:', font="Didot")
lbl_username.pack()
ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(pady=5)

password = tk.Label(frame_login,text="Password:",font="Didot")
password.pack()
ent_pass = tk.Entry(frame_login, bd=3)
ent_pass.pack()

button = tk.Button(frame_login, text='Enter', command=button)
button.pack()



#frameAuth
lblPassword = tk.Label(frameAuth, text='', font="Didot")
lblPassword.pack()


#grid tests



#setup

frame_login.tkraise()

root.mainloop()
