# This is a flash car application
# Users can load their own words list
# Words marked as remembered will be removed from the list
# Words still need learning is saved in a new file
# When opened again, program first tries finding this new list and load its data
# SKILLS: tkinter, pandas, file i/o
# Difficulty: medium
from tkinter import *
import pandas as pd
import random

seconds_left = 3
timer = 'timer tracking ID, used for cancelling count down'
curr_card_data = {'French word': 'English word'}


def switch_next_card(word_is_remembered):
    """Display the next pair of words; reset count down; reset language; reset text color; reset card side"""
    global seconds_left, timer, curr_card_data
    seconds_left = 3
    curr_card_data = random.choice(word_data)
    card_canvas.itemconfig(card_bg, image=card_front_img)
    card_canvas.itemconfig(lang, text='French', fill='black')
    card_canvas.itemconfig(word, text=curr_card_data['French'], fill='black')
    window.after_cancel(timer)
    count_down_1s()
    # remove the word if marked as remembered
    if word_is_remembered:
        word_data.remove(curr_card_data)
        print('word removed from learning list')
        file = open('./data/words_to_learn.csv', 'w')
        word_data_df = pd.DataFrame.from_dict(word_data)
        word_data_df.to_csv('./data/words_to_learn.csv', index=False)
        print('new learning list file generated')
        file.close()


def renew_count_down_display():
    """Call count_down if there is time left, else display answer"""
    global seconds_left
    print(f'renew count down, {seconds_left} left')
    if seconds_left > 0:
        count_down_1s()
    else:
        show_answer()


def count_down_1s():
    """Count down one second, call the answer displaying function when there is no time left"""
    global seconds_left, timer
    if seconds_left == 0:
        show_answer()
    timer = window.after(1000, renew_count_down_display)
    seconds_left -= 1


def show_answer():
    """Show the answer, reset timer"""
    global seconds_left, curr_card_data
    seconds_left = 3
    print('time is up, show answer')
    card_canvas.itemconfig(lang, text='English', fill='white')
    card_canvas.itemconfig(word, text=f'{curr_card_data["English"]}', fill='white')
    card_canvas.itemconfig(card_bg, image=card_back_img)


# Load word data
try:
    word_data = pd.read_csv('./data/words_to_learn.csv')
except FileNotFoundError:
    print('words to learn list not found, loading all words')
    word_data = pd.read_csv('./data/french_words.csv')
else:
    print('words to learn list found, loading words')
finally:
    word_data = word_data.to_dict(orient="records")
print(word_data)

BACKGROUND_COLOR = "#B1DDC6"

# ====UI init====
window = Tk()
window.title('Flash Card')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
# ===Buttons===
# ---correct---
correct_img = PhotoImage(file="./images/right.png")
correct_bt = Button(image=correct_img, highlightthickness=0, command=lambda: switch_next_card(True))
correct_bt.grid(row=1, column=1)
# ---wrong---
wrong_img = PhotoImage(file="./images/wrong.png")
wrong_bt = Button(image=wrong_img, highlightthickness=0, command=lambda: switch_next_card(False))
wrong_bt.grid(row=1, column=0)
# ===Flashcard===
# ---card---
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
card_canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_bg = card_canvas.create_image(400, 263, image=card_front_img)
card_canvas.grid(row=0, column=0, columnspan=2)
# ---language---
LANG_FONT = ("Calibri", 40, 'italic')
lang = card_canvas.create_text(390, 150, text='French', font=LANG_FONT)
# ---word---
WORD_FONT = ("Calibri", 60, 'bold')
word = card_canvas.create_text(400, 280, text='click button to begin', font=WORD_FONT)

window.mainloop()