import json
from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip


# ---------------------------- SEARCH WEBSITE ------------------------------- #

def search_website():
    web = website_text_input.get()
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
            user_detail = messagebox.showinfo(title=web,
                                              message=f"Website: {web}\nEmail : {data[web]['email']}\nPassword: {data[web]['password']}")
    except FileNotFoundError:
        error_msg = messagebox.showinfo(title="Oops", message=f"No Data file found")
    except KeyError:
        error_msg = messagebox.showinfo(title="Oops", message=f"No details for {web} exist")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generator():
    password_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    random_password = "".join(password_list)
    password_input.insert(0, random_password)
    pyperclip.copy(random_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def add():
    web = website_text_input.get()
    uid = email_username_input.get()
    password = password_input.get()
    new_data = {
        web: {
            "email": uid,
            "password": password
        }
    }
    if web == "" or password == "":
        web_empty = messagebox.showinfo(title="Oops", message="Please don't leave fields empty")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        except json.decoder.JSONDecodeError:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            website_text_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)
logo = PhotoImage(file="logo.png")
canvas = Canvas(window, width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_text_input = Entry(width=33)
website_text_input.grid(column=1, row=1)

search_button = Button(text="Search", width=15, command=search_website)
search_button.grid(column=2, row=1)

email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)
email_username_input = Entry(width=53)
email_username_input.insert(0, "jigar@gmail.com")
email_username_input.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_input = Entry(width=33)
password_input.grid(column=1, row=3)

password_generate_button = Button(text="Generate Password", command=password_generator)
password_generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=45, command=add)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
