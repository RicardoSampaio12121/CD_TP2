from flask import Blueprint, render_template, request, redirect, url_for
from User import User
from flask_login import login_user
from models import UserModel


auth = Blueprint('auth', 'auth')


@auth.route('/Signup')
def signup():
    print("entra aqui caralho!")
    with open("WebPages/Register.html") as file:
        return file.read()


@auth.route('/signup', methods=['POST'])
def signup_post():
    username = request.form.get('username')
    password = request.form.get('password')

    user = User(username, password)

    # TODO: se já existir deve dar erro...corrigir
    user.create_user()
    return redirect(url_for('index'))


@auth.route('/Login')
def login():
    return render_template('WebPages/authentication.html')


@auth.route('/Login', methods=['POST'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')

    user = User(username, password)
    authenticated = user.authenticate_user()

    if not authenticated:
        return redirect(url_for('index'))

    user_model = UserModel(username, password)
    login_user(user_model)


