from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        return f"Name: {request.form.get('name')}    Password: {request.form.get('password')}"
    else:
        return 'login'


if __name__ == '__main__':
    app.run(debug=True)
