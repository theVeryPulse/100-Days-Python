# Goal: get data from WTForm on webpages built with Flask; form is rendered with Flask-Bootstrap

# Difficulty: hard. Many details among interactions between Flask, WTForm, HTML, and Flask-bootstrap
# SKILLS: Flask, WTForm, Flask-bootstrap

"""
Basic Steps of Building Website with Flask
- Build a base.html
- Inherit base.html to build other pages
- Use flask_bootstrap to add elements, such as
    {% from 'bootstrap4/form.html' import render_form %}
    {{ render_form(form) }} <!-- form is a FlaskForm instance-->
"""

# Useful links:
# Flask template inheritance: https://flask.palletsprojects.com/en/2.3.x/patterns/templateinheritance/
# Bootstrap-flask: https://bootstrap-flask.readthedocs.io/en/stable/basic/


from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap

'''
Open the Terminal in PyCharm (bottom left). 
- On Windows type:
python -m pip install -r requirements.txt

- On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


# Inherit from FlaskForm class, add required fields as class variables
class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label='Log in')


app = Flask(__name__)
bootstrap = Bootstrap(app)  # Link Flask app with Bootstrap
app.secret_key = 'seeecreeetkeeey'


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    login_form.validate_on_submit()
    if login_form.validate_on_submit():
        if login_form.email.data == 'admin@email.com' and login_form.password.data == '12345678':
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=login_form)


@app.route('/flask_bootstrap_test')
def flask_bootstrap_test():
    return render_template('flask_bootstrap_test.html')


if __name__ == '__main__':
    app.run(debug=True)
