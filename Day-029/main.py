import tkinter.messagebox
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- Search Website ------------------------------- #
def search_website():
    if len(web_entry.get()) == 0:
        messagebox.showinfo(title="Error", message='Please enter the website you would like to search for')
    else:
        try:
            with open('password.json', 'r') as file:
                data = json.load(file)
                web_info = data[web_entry.get()]
        except IndexError:
            messagebox.showinfo(title='Error', message='No Website information is found')
        else:
            messagebox.showinfo(title=f'{web_entry.get()}', message=f"Email: {web_info['email']} \n"
                                                                    f"Password: {web_info['password']}")


# ---------------------------- FILE INFORMATION JSON ------------------------------- #
def file_info(new_data):
    try:
        with open("password.json", 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        with open('password.json', 'w') as file:
            json.dump(new_data, file, indent=4)
    else:
        data.update(new_data)
        with open('password.json', 'w') as file:
            json.dump(data, file, indent=4)
    finally:
        web_entry.delete(0, END)
        email_entry.delete(0, END)
        password_entry.delete(0, END)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    pass_letters = [random.choice(letters) for x in range(nr_letters)]
    pass_symbols = [random.choice(letters) for x in range(nr_symbols)]
    pass_numbers = [random.choice(letters) for x in range(nr_numbers)]

    password_list = pass_letters + pass_symbols + pass_numbers

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    if len(web_entry.get()) == 0 or len(email_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showinfo(title="Error", message="Please make sure you haven't left any fields empty.")
    else:
        is_okay = messagebox.askokcancel(title=web_entry.get(),
                                         message=f"These are the details entered: \nEmail: {email_entry.get()}"
                                                 f"\nPassword: {password_entry.get()} \nIt is okay to save?")
        if is_okay:
            new_data = {
                web_entry.get(): {
                    'email': email_entry.get(),
                    'password': password_entry.get()
                }
            }
            file_info(new_data)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title = "Password Management"
window['bg'] = 'light blue'
window.config(pady=20, padx=50)

canvas = Canvas(width=200, height=200, highlightthickness=2)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

web_label = Label(text='Website: ')
web_label.grid(column=0, row=1)

web_entry = Entry(width=35)
web_entry.grid(column=1, row=1, columnspan=2)
web_entry.focus()

search_button = Button(text='Search', command=search_website)
search_button.grid(column=2, row=1, columnspan=2)

email_label = Label(text='Email/Username: ')
email_label.grid(column=0, row=2)

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)

password_label = Label(text='Password: ')
password_label.grid(column=0, row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

add_info = Button(text="Add", width=35, command=save_password)
add_info.grid(column=1, row=4, columnspan=2)

window.mainloop()
