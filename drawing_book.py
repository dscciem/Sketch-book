from tkinter import *
from tkinter.colorchooser import askcolor
from PIL import ImageTk,Image

class Paint(object):
    DEFAULT_PEN_SIZE = 5.0
    DEFAULT_COLOR = 'black'
    def __init__(self):
        self.root = Tk()
        self.root.title('Drawing Book by Sagnik')
        self.root.geometry('800x450')
        self.root.maxsize(1600,900)
        self.root.minsize(500,300)

        self.paint_tools = Frame(self.root,width = 100,height = 100,relief = RIDGE,borderwidth = 3)
        self.paint_tools.place(x=0,y=0)


if __name__ == '__main__':
    Paint()