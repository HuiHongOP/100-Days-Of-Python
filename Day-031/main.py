from tkinter import *
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

data = pd.read_csv("data/english_to_chinese.csv")

window = Tk()
window.title = "Flash Card"
window['bg'] = BACKGROUND_COLOR
window.config(pady=50, padx=50)

# Canvas allows overlapping objects
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
my_image = PhotoImage(file='images/card_front.png')
canvas.create_image(400, 260, image=my_image)
canvas.create_text(400, 150, text='English', font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text='Chinese', font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
wrong_image = PhotoImage(file='images/wrong.png')
wrong_button = Button(image=wrong_image, command='')
wrong_button.grid(column=0, row=1)

correct_image = PhotoImage(file='images/right.png')
correct_button = Button(image=correct_image, command='')
correct_button.grid(column=1, row=1)

window.mainloop()
