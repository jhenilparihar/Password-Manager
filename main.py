from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['H', 'E', 'N', 'I', 'L', 'h', 'e', 'n', 'i', 'l', 'P', 'A', 'R', 'p', 'a', 'r']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '@']

    password_list = []

    password_list += [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)

    generated_password = "J" + ''.join(password_list)
    password_input.delete(0, END)
    password_input.insert(0, generated_password)
    pyperclip.copy(generated_password)

# ---------------------------- FIND PASSWORD ------------------------------- #


def search():
    website = website_input.get()
    try:
        with open('../data.json', mode='r') as file:
            data = json.load(file)
            password = data[website]["Password"]
    except FileNotFoundError:
        messagebox.showinfo(title='File Not Found', message='No Data File Found')
    except KeyError:
        messagebox.showinfo(title='Key Error', message='No Details for the website exists')
    else:
        messagebox.showinfo(title='Website Found', message=f'Website : {website}\nPassword : {password}')
        pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "Email": email,
            "Password": password
        }
                }
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title='Oops', message="Please Don't leave any field empty")
    else:
        try:
            with open('data.json', mode='r') as file:
                # reading old data
                data = json.load(file)
                # updating old data with new data
                data.update(new_data)
        except FileNotFoundError:
            with open('data.json', mode='w') as file:
                json.dump(new_data, file, indent=4)
        else:
            # saving updated data
            with open('data.json', mode='w') as file:
                json.dump(data, file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas()
canvas.config(width=200, height=200)
image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

website_label = Label(text='Website : ')
website_label.grid(column=0, row=1)

email_label = Label(text='Email/Username : ')
email_label.grid(column=0, row=2)

password_label = Label(text='Password : ')
password_label.grid(column=0, row=3)

website_input = Entry(width=32)
website_input.grid(column=1, row=1, columnspan=1, padx=(0, 5))
website_input.focus()

email_input = Entry(width=51)
email_input.grid(column=1, row=2, columnspan=2, pady=(5, 5))
email_input.insert(0, 'example@gmail.com')

password_input = Entry(width=32)
password_input.grid(column=1, row=3, padx=(0, 5))

search_button = Button(text='Search', bg='white', width=14, command=search, border=0)
search_button.grid(column=2, row=1)

generate_button = Button(text='Generate Password', bg='white', command=generate_password, border=0)
generate_button.grid(column=2, row=3)

add_button = Button(text='ADD', width=44, bg='white', command=save, border=0)
add_button.grid(column=1, row=4, columnspan=3, pady=(5, 0))

window.mainloop()
