# This is a simple password manager program with a GUI
# It generates random passwords and save log in information in a text file
# I personally love this program, it has beautiful and well-organised codes
# SKILLS: Tkinter, GUI, Tkinter
# Difficulty: medium
import random
import string
from tkinter import *
from tkinter import messagebox
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    """Generate a random password from using safe characters"""
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '-']
    char_set = [*list(string.ascii_letters), *list(string.digits), *symbols]
    # print(char_set)  # test code
    rd_password = ''.join(random.choices(char_set, k=14))
    password_et.delete(0, 'end')
    password_et.insert(index=0, string=rd_password)
    pyperclip.copy(rd_password)
    messagebox.showinfo(title='Info', message='password copied to clipboard')


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    """Save the website, email/username, password to 'passwords.txt'"""
    website = website_et.get()
    email_username = email_username_et.get()
    password = password_et.get()

    for char in ILLEGAL_CHARS:
        if char in f'{website}{email_username}{password_et}':
            messagebox.showwarning(title='Warning', message=f'email or password cannot contain {char}')
            return
        elif website == '' or email_username == '' or password == '':
            messagebox.showwarning(title='Warning', message='Missing information')
            return
    # ask user to check information
    is_okay = messagebox.askokcancel(title='confirm information', message=f'Website: {website}\n'
                                                                          f'Email/Username: {email_username}\n'
                                                                          f'Password: {password}\n'
                                                                          f'Do you wish to save these information?')
    if is_okay:
        with open('passwords.txt', 'a') as file:
            file.write(f'{website} | {email_username} | {password}\n')
        website_et.delete(0, 'end')
        password_et.delete(0, 'end')
        messagebox.showinfo(title='Success!', message='Password successfully saved!')


# ---------------------------- UI SETUP ------------------------------- #
LONG_ENTRY_WIDTH = 50
SHORT_ENTRY_WIDTH = 31
DEFAULT_EMAIL = 'philip@email.com'
ILLEGAL_CHARS = ['|', '¥', ' ']


window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)
window.minsize(260, 260)
# logo
logo = PhotoImage(file='logo.png')
canvas = Canvas(width=200, height=200)
canvas.create_image((100, 100), image=logo)
canvas.grid(row=0, column=1)
# Website
website_dp = Label(text='Website:')
website_dp.grid(row=1, column=0)
website_et = Entry(width=LONG_ENTRY_WIDTH)
website_et.grid(row=1, column=1, columnspan=2)
website_et.focus()
# Email/Username
email_username_dp = Label(text="Email/Username:")
email_username_dp.grid(row=2, column=0)
email_username_et = Entry(width=LONG_ENTRY_WIDTH)
email_username_et.grid(row=2, column=1, columnspan=2)
email_username_et.insert(0, DEFAULT_EMAIL)
# Password
password_dp = Label(text='Password:')
password_dp.grid(row=3, column=0)
password_et = Entry(width=SHORT_ENTRY_WIDTH)
password_et.grid(row=3, column=1)
# Generate password button
generate_password_bt = Button(text='Generate Password', command=generate_password)
generate_password_bt.grid(row=3, column=2)
# 'Add' button
add_bt = Button(text='Add', width=LONG_ENTRY_WIDTH, command=save_password)
add_bt.grid(row=4, column=1, columnspan=2)

window.mainloop()