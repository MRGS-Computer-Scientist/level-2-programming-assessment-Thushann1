from tkinter import*
w_width = 700
w_height = 500


window = Tk()
window.geometry(str(w_width) + "x" + str(w_height)) 
window.title("My App")

main_frame = Frame(background="red", width=100, height=100)
main_frame.pack()

hello_label = Label(text="hello, World!")
hello_label.place(x=90, y=20 )

window.mainloop()