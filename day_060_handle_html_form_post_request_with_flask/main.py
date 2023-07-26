# This version enables Flask to receive the HTML form through post request
# The form submitted is then sent to website owner through email by STMP
# Skills: Flask, HTML, STMP,
# Difficulty: Medium

from flask import Flask, render_template, request
import requests
from notification_manager import NotificationManager

posts = requests.get("https://api.npoint.io/771cea6b5d4b0d923b11").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/contact")
def contact():
    return render_template("contact.html", header_text='Contact Me')


@app.route('/contact', methods=['POST'])
def receive_data():
    notification_manager = NotificationManager()
    notification_manager.send_emails(
        title='Some one leaves you a message on your website',
        text=f'{request.form.get("name")}\n'
             f'{request.form.get("email")}\n'
             f'{request.form.get("phone")}\n'
             f'{request.form.get("message")}\n',
        to=notification_manager.gmail_address
    )
    print('Message sent successfully')
    return render_template('contact.html', header_text='Successfully sent message')


if __name__ == "__main__":
    app.run(debug=True, port=5001)
