# Higher-lower game with Flask generated webpages
# Change address to /<num> to check guess result
# SKILLS: Flask, decorators, HTML,
# Difficulty: easy

import random

from flask import Flask

app = Flask(__name__)
correct_num = random.randint(1, 9)
print(f'Correct number: {correct_num}')


def centered_h1(text):
    return f'<h1 style="text-align: center;">{text}</h1>'


def centered_img(src):
    return f'<img style="display: block;margin-left: auto; margin-right: auto;" alt="Number of 1 to 9" src="{src}" />'


@app.route("/")
def hello():
    return f'{centered_h1("Guess a number between 1 and 9!")} ' \
           f'{centered_img("https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif")}'


@app.route('/<int:num>')
def guess(num):
    if correct_num == num:
        return f'{centered_h1("You are right!")} ' \
               f'{centered_img("https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif")}'
    elif correct_num > num:
        return f'{centered_h1("Too low, guess again")} ' \
               f'{centered_img("https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif")}'
    else:
        return f'{centered_h1("Too high, guess again")} ' \
               f'{centered_img("https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif")}'


@app.route('/bye')
def bye():
    return 'Bye bye'


if __name__ == '__main__':
    app.run()
