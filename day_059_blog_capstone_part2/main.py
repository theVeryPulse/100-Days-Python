# Builds a blog website with Flask and Jinja
# Blog has a main page where post previews are displayed
# Blog data is retrieved from npoint API
# Header and footer are shared through all pages with {% include 'header.html' %}

# SKILLS: Flask, Jinja, web development
# Difficulty: medium


from flask import Flask
from flask import render_template, url_for
import requests

app = Flask(__name__)
endpoint = 'https://api.npoint.io/771cea6b5d4b0d923b11'
response = requests.get(url=endpoint)
response.raise_for_status()
blog_data: list[dict] = response.json()


@app.route('/')
def index():
    return render_template('index.html', posts=blog_data)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/post/<int:post_id>')
def post(post_id: int):
    return render_template('post.html', post=blog_data[post_id - 1])


if __name__ == '__main__':
    app.run(debug=True)
