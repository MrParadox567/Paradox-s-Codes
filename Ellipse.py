import tkinter
import turtle
import math

class Ellipse:
    def __init__(self):
        self.__main_window = tkinter.Tk()

        #Creating Frames
        self.__top_frame = tkinter.Frame(self.__main_window)
        self.__mid_frame = tkinter.Frame(self.__main_window)
        self.__bottom_frame = tkinter.Frame(self.__main_window)

        ##Creating Entry Widgets in the top Frame
        self.Label1 = tkinter.Label(self.__top_frame,text="This program will draw an Ellipse of your choice.")
        self.Label2=tkinter.Label(self.__top_frame,
                                  text="Enter the value of the semi-major axis of the Ellipse: ")
        self.major_axis = tkinter.Entry(self.__top_frame,width = 10)

        self.Label1.pack(side="left")
        self.Label2.pack(side="left")
        self.major_axis.pack(side="left")

        self.Label3 = tkinter.Label(self.__mid_frame,
                                    text = "Enter the value of the semi-minor axis of the Ellipse: ")
        self.minor_axis = tkinter.Entry(self.__mid_frame,width = 10)

        ##Packing the top_frame widgets
        
        self.Label3.pack(side="left")
        self.minor_axis.pack(side="left")

        #Creating Buttons
        self.__do_button = tkinter.Button(self.__bottom_frame,text="Draw",
                                          command = self.draw_ellipse)
        self.__quit_button = tkinter.Button(self.__bottom_frame,text="Quit",
                                            command = self.__main_window.destroy)
        
        ##Packing the buttons
        self.__do_button.pack(side="left")
        self.__quit_button.pack(side="left")

        ##Packing the frames
        self.__top_frame.pack()
        self.__mid_frame.pack()
        self.__bottom_frame.pack()

        tkinter.mainloop()
    
    def draw_ellipse(self):
        a = float(self.major_axis.get())
        b = float(self.minor_axis.get())
        turtle.penup()
        turtle.goto(a,0)
        turtle.pendown()

        for theta in range(361):
            turtle.goto(a*math.cos(math.radians(theta)),b*math.sin(math.radians(theta)))
        
turtle.bgcolor("cyan")
turtle.pencolor("purple")
ellipse = Ellipse()
            


        