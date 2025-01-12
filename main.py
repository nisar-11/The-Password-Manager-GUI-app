from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

GREEN = "#9bdeac"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_used():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, string=password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_clicked():
    website_data = website_entry.get()
    password_data = password_entry.get()
    email_data = email_entry.get()

    if len(website_data) == 0 or len(password_data) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website_data, message=f"These are the details entered:\nwebsite: {website_data}\nemail: {email_data}\npassword: {password_data}\nIs it ok to save?")
        if is_ok:
            with open("data.txt", mode="a") as file:
                file.write(f"{website_data} | {email_data} | {password_data}\n")
            website_entry.delete(0, 'end')
            password_entry.delete(0, 'end')
            website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50, bg=GREEN)

canvas = Canvas(width=200, height=200, bg=GREEN, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", bg=GREEN)
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:", bg=GREEN)
email_label.grid(column=0, row=2)
password_label = Label(text="Password:", bg=GREEN)
password_label.grid(column=0, row=3)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()


email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(END, string="abc@gmail.com")

password_entry = Entry(width=17)
password_entry.grid(column=1, row=3)

generate_button = Button(text="Generate Password", command=generate_used, highlightthickness=0)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=30, command=add_clicked, highlightthickness=0)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()