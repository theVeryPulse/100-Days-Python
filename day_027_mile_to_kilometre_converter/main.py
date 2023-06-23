# This program with GUI converts miles to kilometres
# SKILLS: Tkinter, GUI
# Difficulty: easy

import tkinter

# window
window = tkinter.Tk()
window.title("Miles to kilometres")
window.minsize(width=400, height=200)
window.config(padx=50, pady=10)

# initial text
mile_unit = tkinter.Label(text="Miles", font=("Cambria", 20))
mile_unit.grid(row=0, column=2)
is_equal_to_str = tkinter.Label(text="=", font=("Cambria", 20))
is_equal_to_str.grid(row=1, column=0)

km_unit = tkinter.Label(text="km", font=("Cambria", 20))
km_unit.grid(row=1, column=2)
km_num = tkinter.Label(text="1.6093", font=("Cambria", 20))
km_num.grid(row=1, column=1)


def mile_to_km():
    """Convert the mile number to kilometres"""
    try:
        miles = float(miles_input.get())
    except Exception:
        pass
    else:
        kilometres = round((miles * 1.60934), 4)
        km_num.config(text=f'{kilometres}')


# button
button = tkinter.Button(text="click me", command=mile_to_km)
button.grid(row=2, column=1)

# entry
miles_input = tkinter.Entry(width=10)
miles_input.grid(row=0, column=1)
miles_input.insert(index=tkinter.END, string="1")


window.mainloop()



