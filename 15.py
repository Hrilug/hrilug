from tkinter import *

class A:
    def __init__(self, master=None):
        self.root = master
        self.root.geometry('800x600+200+200')
        self.root.title('测试')
        # self.root.bind("<Motion>", self.call_back)
        self.frm1 = Frame(self.root)
        self.frm2 = Frame(self.root)
        self.frm3 = Frame(self.root)
        self.createpage()
    def call_back(self, event):
        print('现在的位置是：', event.x_root, event.y_root)
    def createpage(self):
        menu = Menu(self.root)
        self.root.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label='测试1', menu=filemenu)
        filemenu.add_command(label='1')
        filemenu.add_command(label='2')
        filemenu.add_command(label='3')
        onemenu = Menu(menu)
        menu.add_cascade(label='测试2', menu=onemenu)
        onemenu.add_command(label='1')
        onemenu.add_command(label='2')
        onemenu.add_command(label='3')
        self.frm1.config(bg='blue', height=500, width=600)
        Label(self.frm1, text='frm1').place(in_=self.frm1, anchor=NW)
        self.frm1.place(x=180, y=50)
        self.frm2.config(bg='red', height=500, width=150)
        Label(self.frm2, text='frm2').place(anchor=NW)
        self.frm2.place(x=20, y=50)
        self.frm3.config(bg='yellow', height=40, width=760)
        Label(self.frm3, text='frm3').place(in_=self.frm3, anchor=NW)
        self.frm3.place(x=20, y=5)
        # frm3下的Label
        Label(self.frm3, text='Label Test Test',
              fg='red', font='Verdana 10 bold').place(x=300, y=10)
        # frm2下的Button
        for i in range(9):
            Button(self.frm2, text='Button%d' % i).place(x=20, y=20+i*50, width=100)
        # frm1下的控件
        Label(self.frm1, text='项目资源管理平台',
              fg='red', font='Verdana 10 bold').place(x=100, y=50, height=80, width=400)
        Button(self.frm1, text='1', height=1, width=1).place(x=450, y=450)
        Button(self.frm1, text='2', height=1, width=1).place(x=490, y=450)
        Button(self.frm1, text='3', height=1, width=1).place(x=530, y=450)
if __name__ == '__main__':
    root = Tk()
    A(root)
    mainloop()
