from tkinter import*
w_width = 700
w_height = 500

bg_color = ""

window = Tk()
window.geometry(str(w_width) + "x" + str(w_height)) 
window.title("My App")

top_frame = Frame(background='red', width=w_width, height=100)
top_frame.pack()

main_frame = Frame(background="red", width=100, height=1200)
main_frame.pack()

home_button = Button(bottom_frame, txt="home", height=5, width=5, bg='green'
home_button.place(x=0,y=0)

# adding widgets to the root window

# Creating a photoimage object to use image



window.mainloop()