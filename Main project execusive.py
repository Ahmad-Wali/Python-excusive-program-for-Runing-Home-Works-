import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.configure(bg='lightblue')

def new():
    nw= tk.Toplevel(root)
    nw.title("Home Work1")
    
    file= open("C:/Users/DELL-PC/Desktop/factorial",mode="r")
    data = file.readlines()
    

    for user in data:
        user = user.rstrip("\n")
        tk.Label(nw, text=user,font=isinstance).pack(side="top")

def new2():
    nw= tk.Toplevel(root)
    nw.title("Home Work2")
    
    file= open("C:/Users/DELL-PC/Desktop/fiboacci",mode="r")
    data = file.readlines()
    

    for user in data:
        user = user.rstrip("\n")
        tk.Label(nw, text=user,font=isinstance).pack(side="top")

def new3():
    nw= tk.Toplevel(root)
    nw.title("Cooised Home Work")
    types=[("all files","*.*")]
    filepath= filedialog.askopenfilename(filetypes=types, title="choose file")

    file= open(filepath, mode="r")
    data = file.readlines()
    
    for user in data:
        user = user.rstrip("\n")
        tk.Label(nw, text=user,font=isinstance).pack()

def load_file():
    types=[("all files","*.*")]
    
    
        
def home_work2():
    types=[("all files","*.*")]
    file= open("C:/Users/DELL-PC/Desktop/fiboacci",mode="r")
    data = file.readlines()

    for user in data:
        user = user.rstrip("\n")
        tk.Label(root, text=user,font=isinstance).pack(side="bottom")

def add_other():
    types=[("all files","*.*")]
    filepath= filedialog.askopenfilename(filetypes=types, title="choose file")

    file= open(filepath, mode="r")
    data = file.readlines()
    
    for user in data:
        user = user.rstrip("\n")
        tk.Label(root, text=user,font=isinstance).pack()



root.title("A basic program for displaying Home Works")
f_button= tk.Button(root, text= "Home work 1 ",font=isinstance, command = new,border=5)
f_button.pack(side= "left",padx=10)
s_button = tk.Button(root,text= "Home work 2 ",font=isinstance, command = new2,border=5)
s_button.pack(side="right",padx=10)
t_button = tk.Button(root, text="add H.W",font=isinstance,command = new3,border=5)
t_button.pack(side= "left",padx=380)




root.geometry("1200x1300")
root.mainloop()


    