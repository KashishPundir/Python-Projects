
from tkinter import Label
from tkinter import Tk
import time

master=Tk()
master.title("Digital Clock")
master.wm_attributes("-toolwindow","True")
master.resizable(0,0)

def current_time():
    timeVar=time.strftime("%I:%M:%S %p")
    clock.config(text=timeVar)
    clock.after(200,current_time)

clock=Label(master,font=("Arial",60),bg="black",fg="light grey")     
clock.pack()
current_time()    
master.mainloop()