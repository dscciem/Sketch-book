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

        self.paint_tools = Frame(self.root,width = 100,height = 300,relief = RIDGE,borderwidth = 3)
        self.paint_tools.place(x=0,y=0)

        self.pen_logo = ImageTk.PhotoImage(Image.open('logos/pen.png'))
        self.p = Label(self.paint_tools , text = 'Pen' , borderwidth = 0, font = ('verdana',10,'bold'))
        self.p.place(x=5,y=10)
        self.pen_button = Button(self.paint_tools,padx=6,image = self.pen_logo,borderwidth=2,command = self.use_pen)
        self.pen_button.place(x=60,y=10)



if __name__ == '__main__':
    Paint()