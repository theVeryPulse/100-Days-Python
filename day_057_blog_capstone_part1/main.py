# Build a simple blog website with Flask
# The website has a main page where users can click on posts
# Posts are rendered on-site using the same template
# SKILLS: Flask, Jinja, API
# Difficulty: easy-medium

from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)
data_endpoint = 'https://api.npoint.io/4b8d83307c8c643636fd'
response = requests.get(url=data_endpoint)
blog_data = response.json()
blog_post_list: list[Post] = [
    Post(
        post_id=post['id'],
        title=post['title'],
        subtitle=post['subtitle'],
        body=post['body']
        )
    for post in blog_data
]


@app.route('/')
def home():
    return render_template(
        "index.html",
        blog_data=blog_post_list
    )


@app.route('/post/<int:blog_id>')
def blog_post(blog_id):
    for post in blog_post_list:
        if post.id == blog_id:
            requested_post = post
    if requested_post:
        return render_template(
            'post.html',
            post=requested_post
        )


if __name__ == "__main__":
    app.run(debug=True)
