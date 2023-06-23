# This is a collection of widget examples for a Tkinter window

from tkinter import *

# Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)
window.config(padx=20, pady=20)  # adds a pad - a blank edge - to the window

# Labels
label = Label(text="This is old text")
label.config(text="This is new text")
label.grid(row=0, column=0)


# Buttons
def action():
    label.config(text=entry.get())
    print("Do something")


# calls action() when pressed
button = Button(text="Click Me", command=action)
button.grid(row=1, column=1)

button_2 = Button(text="new button")
button_2.grid(row=0, column=2)

# Entries
entry = Entry(width=30)
# Add some text to begin with
entry.insert(END, string="Click button to update")
# Gets text in entry
print(entry.get())
entry.grid(row=2, column=3)

# Text
text = Text(height=5, width=30)
# Puts cursor in textbox.
text.focus()
# Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
# Get current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.grid(row=2, column=1)


# Spinbox
def spinbox_used():
    # gets the current value in spinbox.
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.grid(row=3, column=1)


# Scale
# Called with current scale value.
def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.grid(row=4, column=1)


# Checkbutton
def checkbutton_used():
    # Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())


# variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.grid(row=5, column=1)


# Radiobutton
def radio_used():
    print(radio_state.get())


# Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.grid(row=6, column=1)
radiobutton2.grid(row=7, column=1)


# Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.grid(row=8, column=1)
window.mainloop()
