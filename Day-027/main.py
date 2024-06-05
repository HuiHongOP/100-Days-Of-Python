from tkinter import *

window = Tk()
window.title("The First GUi Program")
window.minsize(width=500, height=300)
window['bg'] = 'light blue'

# Label
my_label = Label(text="I am a Label", font=("Arial", 14, "bold"))
my_label.pack()


# Button

def button_clicked():
    print("I got clicked")
    my_label.config(text=input.get())


button = Button(text="Click Me", command=button_clicked)
button.pack()

# Entry

input = Entry(width=10)
input.pack()
input.get()
# Keep the window on the screen and listening
window.mainloop()
