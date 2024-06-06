from tkinter import *

window = Tk()
window.title = "Mile to Km Converter"


def miles_to_km():
    user_miles = int(miles_input.get())
    km_output = user_miles * 1.609
    converter.config(text=km_output)


miles_input = Entry(width=15)
miles_input.grid(column=1, row=0)

miles_text = Label(text="Miles", font=("Courier", 12))
miles_text.grid(column=2, row=0)

is_equal = Label(text="is equal to", font=("Courier", 12))
is_equal.grid(column=0, row=1)

converter = Label(text="0", font=("Courier", 12))
converter.grid(column=1, row=1)

km = Label(text="Km", font=("Courier", 12))
km.grid(column=2, row=1)

calculate = Button(text='Calculate', font=("Courier", 12), command=miles_to_km)
calculate.grid(column=1, row=2)

window.mainloop()
