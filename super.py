from tkinter import*
class GUI:
    def __init__(self):
        self.root=Tk()
        self.root.mainloop()
class control(GUI):
    def __init__(self):
        super().__init__()#invokes the constructor of some other class by it's own object
        print("om")

obj=control()
