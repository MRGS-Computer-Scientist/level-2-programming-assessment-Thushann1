from tkinter import*
from app_settings import *

class App():

    def __init__(self):
        window = Tk()
        window.geometry(str(w_width) + "x" + str(w_height)) 
        window.title("My App")

        top_frame = Frame(background='red', width=w_width, height=100)
        top_frame.pack()

        main_frame = Frame(background="red", width=100, height=1200)
        main_frame.pack()

        home_button = Button(top_frame, text="Home", height=5, width=5, bg='green')
        home_button.place(x=0,y=0)

        window.mainloop()

        def print_name(self):
            print("micheal")