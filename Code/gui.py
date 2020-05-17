# tkinter : is inbuilt module

from tkinter import Tk, Label, Button,Text


class MyFirstGUI:
    def __init__(self, master):
         
        self.master = master
        master.title("GUI Form")

        self.head1 = Label(master, text="This is our first GUI! ")        
        self.head1.pack()

        
        self.head2 = Label(master, text="This is our first GUI! 2")        
        self.head2.pack()



        self.head3 = Label(master, text="This is our first GUI! 3")        
        self.head3.pack()

        
        self.b1 = Button(master, text="Greet",command=self.hi)
        self.b1.pack()

        self.b2 = Button(master, text="Close", command=master.quit)
        self.b2.pack()

        
        self.t1 = Text(master)
        self.t1.pack()

        

        
        
    def hi(self):
          print('you have clicked on button ')
          



root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
