# Render an HTML page as name card
# SKILLS: Flask, HTML render
# Difficulty: easy

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)