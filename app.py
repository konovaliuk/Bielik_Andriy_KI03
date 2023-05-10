from flask import Flask, render_template, url_for, request
from command.register_command import Register

app = Flask(__name__)


@app.route('/')  # головна сторінка
def home():
    return render_template("home.html")


@app.route('/register', methods=['GET', 'POST'])  # реєстрація
def register():
    if request.method == 'POST':
        return Register(request).execute()
    else:
        return render_template("register.html")


@app.route('/authorization')  # авторизація
def authorization():
    return render_template("authorization.html")


app.run(debug=True)
