from tkinter import *
from tkinter import messagebox

def login():
    username=entry1.get()
    password=entry2.get()

    if (username==""and password==""):
        messagebox.showinfo("","BLANK NOT ALLOWED")

    elif (username=="PACMAN" and password=="0190"):
        messagebox.showinfo("","login success")

    else:
        messagebox.showinfo("","incorrects username and password")
        entry1.delete(0, END)
        entry2.delete(0, END)
        print("cleared")

def register():
    username = entry1.get()
    password = entry2.get()

    if (username == "" or password == ""):
        messagebox.showwarning("Warning", "BLANK NOT ALLOWED")

    elif (username=="PACMAN" and password=="0190"):
        messagebox.showerror("Error", "User already exists")

    else:
        messagebox.showinfo("Success", "New user added successfully")
        entry1.delete(0, END)
        entry2.delete(0, END)
        print("cleared") 

def toggle_password():
       if entry2.cget("show") == "":
           entry2.config(show="*")    
           show_btn.config(text="Show")
       else:
           entry2.config(show="")     
           show_btn.config(text="Hide") 

def check_fields(event=None):
    if entry1.get() != "" and entry2.get() != "":
        btn_register.config(state=NORMAL)
    else:
        btn_register.config(state=DISABLED)

     

root=Tk()
root.title("login")
root.geometry("350x230")

global entry1
global entry2

Label(root,text ="username").place(x=20,y=30)
Label(root,text="password").place(x=20,y=80)

entry1=Entry(root,bd=5)
entry1.place(x=140,y=30)

entry2=Entry(root,bd=5, show="*")
entry2.place(x=140,y=80)

show_btn = Button(root, text="Show", width=6, command=toggle_password)
show_btn.place(x=270, y=80)

Button(root,text="login",command=login,height=2,width=12).place(x=40,y=150)
btn_register = Button(root, text="Register",
                      command=register,
                      height=2, width=12,
                      state=DISABLED)
btn_register.place(x=170, y=150)

root.bind('<Return>', lambda e: login())
entry1.bind("<KeyRelease>", check_fields)
entry2.bind("<KeyRelease>", check_fields)
root.mainloop()

