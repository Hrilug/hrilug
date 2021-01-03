
import tkinter as tk
 
master = tk.Tk()
 
def my_mainloop():
    print ("Hello World!")
    master.after(1000, my_mainloop)    
 
master.after(1000, my_mainloop)
 
master.mainloop()