from datetime import datetime
from tkinter import *
root=Tk()
root.geometry("400x200")
root.title("\u231B Stopwatch") 
root.resizable(0,0)
root.wm_attributes("-toolwindow","True")

def start_timer():
    global hr1, min1, sec1
    start=datetime.now().strftime("%H:%M:%S")
    hr1=int(start[0]+start[1])
    min1=int(start[3]+start[4])
    sec1=int(start[6]+start[7])
    
def stop_timer():
    global hr2,min2,sec2
    stop=datetime.now().strftime("%H:%M:%S")
    hr2=int(stop[0]+stop[1])
    min2=int(stop[3]+stop[4])
    sec2=int(stop[6]+stop[7])
    a=(hr2-hr1)*60*60+(min2-min1)*60+(sec2-sec1)
    s=a%60
    m=int(((a-s)/60)%60)
    h=int(((a-s-m*60)/60)/60)

    result_box.config(text=f"⏱ {h:02d}:{m:02d}:{s:02d}")

Button(root,text="START",font=("Arial",15),height=1,width=10,command=lambda:start_timer(),bg="green").place(x=80,y=120)
Button(root,text="STOP",font=("Arial",15),height=1,width=10,command=lambda:stop_timer(),bg="red").place(x=200,y=120)

result_box=Label(root,height=1,width=15,text="⏱ 00:00:00",font=("arial",30))
result_box.pack()
root.mainloop()