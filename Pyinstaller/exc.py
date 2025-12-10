import sys, os
from tkinter import *

def resource_path(path):
    try:
        base_path = sys._MEIPASS
    except:
        base_path = os.path.abspath("./")
    return os.path.join(base_path,path)

window = Tk()
img = PhotoImage(file=resource_path("resources/image/ms19.png"))
label = Label(window, image=img)
label.pack()
window.mainloop()