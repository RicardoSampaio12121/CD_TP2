from flask import Blueprint, request, redirect, url_for, session, make_response, render_template
from User import User

auth = Blueprint('auth', 'auth')


@auth.route('/Signup')
def signup():
    user_id = request.cookies.get('user_id')
    if not user_id:
        return render_template("RegisterForm.html")
    else:
        return redirect(url_for('index'))


@auth.route('/Signup', methods=['POST'])
def signup_post():
    username = request.form.get('username')
    password = request.form.get('password')

    user = User(username, password)

    # TODO: se já existir deve dar erro...corrigir
    user.create_user()
    return redirect(url_for('index'))


@auth.route('/Login')
def login():
    user_id = request.cookies.get('user_id')
    if not user_id:
        return render_template("LoginForm.html")
    else:
        return redirect(url_for('index'))


@auth.route('/Login', methods=['POST'])
def login_post():
    # TODO: check if user is already logged in
    username = request.form.get('username')
    password = request.form.get('password')

    user = User(username, password)
    authenticated = user.authenticate_user()

    if not authenticated:
        return redirect(url_for('index'))
    session[username] = True

    response = redirect(url_for('index'))
    response.set_cookie('user_id', username)
    return response


