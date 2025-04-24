import math
from tkinter import *
calc=Tk()
calc.title("Calculator")         # Give name to the window displayed
calc.geometry("358x534")     
calc.resizable(0,0)
calc.configure(bg="light grey")  # Provide colour to the window except result_box
equation=""
equation1=""

# This function is called when button has been clicked by user 
def show(value):
    global equation            # value display in result_box
    global equation1           # actual evaluation of an equation
    if value=="factorial(":
        equation+="!("
    elif value=="⌫":
        equation=equation[0:len(equation)-1]        
    elif value=="sin(":
        equation+="sin("
    elif value=="cos(":
        equation+="cos("
    elif value=="tan(":
        equation+="tan("
    elif value=="log10(":
        equation+="log("
    elif value=="log(":
        equation+="ln("
    else:
        equation+=value
    if value=="sin(" or value=="cos(" or value=="tan(":
        equation1+="math."+value+"math.pi/180*"
    elif value=="log10(" or value=="factorial(" or value=="log(":
        equation1+="math."+value
    elif value=="e":
        equation1+="2.718281828459045"
    elif value=="π":
        equation1+="3.14159265359"
    elif value=="⌫":
        equation1=equation1[0:len(equation1)-1]
    else:
        equation1+=value
    result_box.config(text=equation)

# Clear all the text of result_box    
def clear():
    global equation
    global equation1
    equation=""
    equation1=""
    result_box.config(text=equation)

# Evaluate the expression and return the result
def calculate():
    global equation
    result=""
    if equation !="":
        try:
            result=eval(equation1)
        except:
            result="Error"
            equation=""
    result_box.config(text=result)
result_box=Label(calc,height=3,width=35,text="",font=("arial",23))
result_box.pack()

Button(calc,text="C",height=0,width=3,font=("arial",25),bd=2,fg="red",command=lambda:clear()).place(x=6,y=115)
Button(calc,text="sin",height=1,width=3,font=("arial",25),bd=2,fg="green",command=lambda:show("sin(")).place(x=76,y=115)
Button(calc,text="cos",height=1,width=3,font=("arial",25),bd=2,fg="green",command=lambda:show("cos(")).place(x=146,y=115)
Button(calc,text="tan",height=1,width=3,font=("arial",25),bd=2,fg="green",command=lambda:show("tan(")).place(x=216,y=115)
Button(calc,text="⌫",height=1,width=3,font=("arial",25),bd=2,fg="blue",command=lambda:show("⌫")).place(x=286,y=115)

Button(calc,text="ln",height=1,width=3,font=("arial",25),bd=2,fg="green",command=lambda:show(("log("))).place(x=6,y=185)
Button(calc,text="!x",height=1,width=3,font=("arial",25),bd=2,fg="green",command=lambda:show(("factorial("))).place(x=76,y=185)
Button(calc,text="exp",height=1,width=3,font=("arial",25),bd=2,fg="green",command=lambda:show("**")).place(x=146,y=185)
Button(calc,text="log",height=1,width=3,font=("arial",25),bd=2,fg="green",command=lambda:show("log10(")).place(x=216,y=185)
Button(calc,text="mod",height=1,width=3,font=("arial",25),bd=2,fg="green",command=lambda:show("%")).place(x=286,y=185)

Button(calc,text="7",height=1,width=3,font=("arial",25),bd=2,command=lambda:show(("7"))).place(x=6,y=255)
Button(calc,text="8",height=1,width=3,font=("arial",25),bd=2,command=lambda:show(("8"))).place(x=76,y=255)
Button(calc,text="9",height=1,width=3,font=("arial",25),bd=2,command=lambda:show("9")).place(x=146,y=255)
Button(calc,text="+",height=1,width=3,font=("arial",25),bd=2,fg="green",command=lambda:show("+")).place(x=216,y=255)
Button(calc,text="-",height=1,width=3,font=("arial",25),bd=2,fg="green",command=lambda:show("-")).place(x=286,y=255)

Button(calc,text="4",height=1,width=3,font=("arial",25),bd=2,command=lambda:show("4")).place(x=6,y=325)
Button(calc,text="5",height=1,width=3,font=("arial",25),bd=2,command=lambda:show("5")).place(x=76,y=325)
Button(calc,text="6",height=1,width=3,font=("arial",25),bd=2,command=lambda:show("6")).place(x=146,y=325)
Button(calc,text="*",height=1,width=3,font=("arial",25),bd=2,fg="green",command=lambda:show("*")).place(x=216,y=325)
Button(calc,text="/",height=1,width=3,font=("arial",25),bd=2,fg="green",command=lambda:show("/")).place(x=286,y=325)

Button(calc,text="1",height=1,width=3,font=("arial",25),bd=2,command=lambda:show("1")).place(x=6,y=395)
Button(calc,text="2",height=1,width=3,font=("arial",25),bd=2,command=lambda:show("2")).place(x=76,y=395)
Button(calc,text="3",height=1,width=3,font=("arial",25),bd=2,command=lambda:show("3")).place(x=146,y=395)
Button(calc,text="π",height=1,width=3,font=("arial",25),bd=2,fg="green",command=lambda:show("π")).place(x=216,y=395)
Button(calc,text="=",height=3,width=3,font=("arial",24),bd=2,fg="red",command=lambda:calculate()).place(x=286,y=395)

Button(calc,text="(",height=1,width=3,font=("arial",25),bd=2,fg="green",command=lambda:show("(")).place(x=6,y=465)
Button(calc,text="0",height=1,width=3,font=("arial",25),bd=2,command=lambda:show("0")).place(x=76,y=465)
Button(calc,text=")",height=1,width=3,font=("arial",25),bd=2,fg="green",command=lambda:show(")")).place(x=146,y=465)
Button(calc,text="e",height=1,width=3,font=("arial",25),bd=2,fg="green",command=lambda:show("e")).place(x=216,y=465)
calc.mainloop()
