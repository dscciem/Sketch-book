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

        self.brush_logo = ImageTk.PhotoImage(Image.open('logos/brush.png'))
        self.b = Label(self.paint_tools,text = 'Brush',borderwidth = 0,font= ('verdana',10,'bold'))
        self.b.place(x=5,y=40)
        self.brush_button = Button(self.paint_tools,image = self.brush_logo,borderwidth = 2,command=self.use_brush)
        self.brush_button.place(x=60,y=40)

        self.color_logo = ImageTk.PhotoImage(Image.open('logos/color.png'))
        self.cl = Label(self.paint_tools,text = 'Color',borderwidth = 0,font= ('verdana',10,'bold'))
        self.cl.place(x=5,y=70)
        self.color_button = Button(self.paint_tools,image = self.color_logo,borderwidth = 2,command=self.choose_color)
        self.color_button.place(x=60,y=70)

        self.eraser_logo = ImageTk.PhotoImage(Image.open('logos/eraser.png'))
        self.e = Label(self.paint_tools,text = 'Eraser',borderwidth = 0,font= ('verdana',10,'bold'))
        self.e.place(x=5,y=100)
        self.eraser_button = Button(self.paint_tools,image = self.eraser_logo,borderwidth = 2,command=self.use_eraser)
        self.eraser_button.place(x=60,y=100)

        self.pen_size = Label(self.paint_tools,text= "Pen Size",font= ('verdana',10,'bold'))
        self.pen_size.place(x=15,y=250)
        self.choose_size_button = Scale(self.paint_tools, from_= 0, to = 10,orient = VERTICAL)
        self.choose_size_button.place(x=20,y=150)
        self.c = Canvas(self.root,bg = 'white',width = 1600, height = 1600,relief = RIDGE,borderwidth = 0)
        self.c.place(x=100,y=0)

        self.setup()
        self.root.mainloop()
    
    def setup(self):
        self.old_x = None
        self.old_y = None
        self.line_width = self.choose_size_button.get()
        self.color = self.DEFAULT_COLOR
        self.eraser_on = False
        self.active_button = self.pen_button
        self.c.bind('<B1-Motion>',self.paint)
        self.c.bind('<ButtonRelease-1>',self.reset)
    
    def use_pen(self):
        self.activate_button(self.pen_button)
    
    def use_brush(self):
        self.activate_button(self.brush_button)

    def use_eraser(self):
        self.activate_button(self.eraser_button,eraser_mode=True)

    def choose_color(self):
        self.eraser_on = False
        self.color = askcolor(color=self.color)[1]

    def activate_button(self,button,eraser_mode=False):
        self.eraser_on = eraser_mode
        self.active_button.config(relief = RAISED)
        button.config(relief = SUNKEN)
        self.activate_button = button
    
    def reset(self,event):
        self.old_x,self.old_y = None,None

    def paint(self,event):
        self.line_width = self.choose_size_button.get()
        paint_color = 'white' if self.eraser_on else self.color
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x,self.old_y,event.x,event.y,width =self.line_width,fill = paint_color,capstyle = ROUND,smooth = True,splinesteps=36)
        self.old_y=event.y
        self.old_x=event.x

if __name__ == '__main__':
    Paint()
