# Decorator practice
from flask import Flask

app = Flask(__name__)
print(app, type(app))


def make_bold(func):
    def wrapper():
        return f'<b>{func()}</b>'

    return wrapper


def make_emphasized(func):
    def wrapper():
        return f'<em>{func()}</em>'

    return wrapper
    pass


def make_underlined(func):
    def wrapper():
        return f'<u>{func()}</u>'

    return wrapper
    pass


@app.route("/")
@make_bold
@make_underlined
@make_emphasized
def hello():
    return "Hello, World!"


@app.route('/bye')
def bye():
    return 'Bye bye'


@app.route('/<username>')
def greet(username):
    return f'Hello, {username}!'


@app.route('/<username>/<int:age>')
def greet_age(username, age):
    return f'Hello, {username.capitalize()}! You are {age} years old'


if __name__ == '__main__':
    app.run(debug=True)
