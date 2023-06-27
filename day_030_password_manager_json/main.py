import json
# This is the updated version of day 29's password manager program
# Feature: save all information in json files
# User can change the default email address now
# SKILLS: .json and Python，Tkinter, GUI,
# Difficulty: medium

# NOTES
# write: json.dump()
# read: json.load()
# update: json.update()


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

    for illegal_char in ILLEGAL_CHARS:
        if illegal_char in f'{website}{email_username}{password_et}':
            messagebox.showwarning(title='Warning', message=f'email or password cannot contain {illegal_char}')
            return
        elif website == '' or email_username == '' or password == '':
            messagebox.showwarning(title='Warning', message='Missing information')
            return
    # ask user to check information
    message = f'Website: {website}\n' \
              f'Email/Username: {email_username}\n' \
              f'Password: {password}\n' \
              f'Do you wish to save these information?'
    is_okay = messagebox.askokcancel(title='confirm information', message=message)
    if is_okay:
        new_data = {website: {"email": email_username, "password": password}}
        try:
            # check if there is already json data
            with open('data.json', 'r') as data_file:
                data = json.load(data_file)  # load already existing json data into json
                data.update(new_data)  # add new data into the dict
        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open('data.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)  # write dict back into json
                # NOTE: read, process, and then write
        finally:
            website_et.delete(0, 'end')
            password_et.delete(0, 'end')
            messagebox.showinfo(title='Success!', message='Password successfully saved!')


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    q_website = website_et.get()

    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
        username_password = data[q_website]
    except Exception as E:
        print(E)
        messagebox.showinfo(title='info', message='No data found')
    else:
        email_username_et.delete(0, 'end')
        email_username_et.insert(0, username_password['email'])
        password_et.insert(0, username_password['password'])


# ---------------------------- UI SETUP ------------------------------- #
LONG_ENTRY_WIDTH = 50
SHORT_ENTRY_WIDTH = 31
default_email = 'philip@email.com'
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
website_et = Entry(width=SHORT_ENTRY_WIDTH)
website_et.grid(row=1, column=1, columnspan=1)
website_et.focus()
# Email/Username title and entry
email_username_dp = Label(text="Email/Username:")
email_username_dp.grid(row=2, column=0)
email_username_et = Entry(width=LONG_ENTRY_WIDTH)
email_username_et.grid(row=2, column=1, columnspan=2)
email_username_et.insert(0, default_email)
# Password
password_dp = Label(text='Password:')
password_dp.grid(row=3, column=0)
password_et = Entry(width=SHORT_ENTRY_WIDTH)
password_et.grid(row=3, column=1)
# Generate password button
generate_password_bt = Button(text='Generate Password', command=generate_password, width=16)
generate_password_bt.grid(row=3, column=2)
# 'Add' button
add_bt = Button(text='Add', width=LONG_ENTRY_WIDTH, command=save_password)
add_bt.grid(row=4, column=1, columnspan=2)
# 'Search' button
search_bt = Button(text='Search', command=search_password, width=16)
search_bt.grid(row=1, column=2)
window.mainloop()