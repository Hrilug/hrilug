import tkinter as tk  
import time

count=0
window=tk.Tk()

def second():
    print("Second")
    l2.place_forget()

def first():
    l1.place_forget()
    l2=tk.Label(window,text="让我们开始吧！",bg="green",font=("Arial",12),width=30, height=2)
    l2.place(x=100,y=50)
    b1=tk.Button(window, text='开始', font=('Arial', 12), width=10, height=1,command=second)
    b1.place(x=200,y=150)

window.title('问卷调查')
window.geometry('500x300')

l1=tk.Label(window, text='你好!欢迎来到Blue Boys的问卷调查！', bg='green', font=('Arial', 12), width=30, height=2)
l1.place(x=100,y=100)

window.after(2000,first)

window.mainloop()