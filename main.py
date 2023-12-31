from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_list = [random.choice(letters) for char in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for char in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for char in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.delete(0, 'end')
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SEARCH WEBSITE ------------------------------ #
def search():
    with open('data.json', 'r') as f:
        data = json.load(f)
        website = website_input.get()
        try:
            dados = data[website]
        except KeyError:
            messagebox.showwarning(title="Erro", message='Site invalido ou não cadastrado!')
        else:
            email = dados['email']
            password = dados['password']
            messagebox.showinfo(title='Credenciais', message= f"Seu email é: {email} \nSua senha é: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
            }
        }

    if len(website) < 1 or len(password) <4 or len(email) <1:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                            f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            try:
                with open('data.json', "r") as f:
                    data = json.load(f)
            except FileNotFoundError:
                with open('data.json', "w") as f:
                    json.dump(new_data, f, indent=4)
            else:
                data.update(new_data)
                with open('data.json', "w") as f:
                    json.dump(data, f, indent=4)
            finally:
                website_input.delete(0, 'end')
                password_input.delete(0, 'end')


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels

Label(text="Website:").grid(column=0, row=1)
Label(text="Email/Username:").grid(column=0, row=2)
Label(text="Password:").grid(column=0, row=3)

# Inputs

website_input = Entry(width=35)
website_input.grid(column=1, row=1, padx=20, pady=5)

email_input = Entry(width=35)
email_input.grid(column=1, row=2, padx=5, pady=5)
email_input.insert(0, 'andre25531@gmail.com')

password_input = Entry(width=35)
password_input.grid(column=1, row=3, padx=5, pady=5)

#Buttons
search_button = Button(text="Search", border=1, width=10, command=search)
search_button.grid(column=2, row=1, padx=5, pady=5)

generate_password_button = Button(text="Generate", border=1, width=10, command=generate_password)
generate_password_button.grid(column=2, row=3, padx=5, pady=5)

add_button = Button(text="Add", width=30, border=1, command=save)
add_button.grid(row=4, column=1)

window.mainloop()