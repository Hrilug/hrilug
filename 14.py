from tkinter import messagebox
import tkinter as tk

top = tk.Tk()
#这里四个参数分别为：宽、高、左、上
top.geometry("500x300+750+200")

top.title("www.tianqiweiqi.com")

def okCallBack():
    tk.messagebox.askokcancel("title","info")

btnOk = tk.Button(top,
                  width=10,
                  height=1,
                  text='ok',
                  padx=1,
                  pady=1,
                  anchor='w',
                  command = okCallBack)
btnOk.place(x=50,y=10,anchor='w')
btnOk.pack()

top.mainloop()