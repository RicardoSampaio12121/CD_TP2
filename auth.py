from flask import Blueprint, request, redirect, url_for, session, make_response, render_template
import os

auth = Blueprint('auth', 'auth')


def check_if_user_exists(username):
    file = open("Users/users.txt", "r")
    for line in file:
        _ = line.split(' ', 1)
        if _[0] == username:
            file.close()
            return True
    file.close()
    return False


def create_user(username, password):
    file = open("Users/users.txt", "a")
    file.write(f'{username} {password}\n')
    file.close()

    os.mkdir(f'Messenger_records/{username}')


def change_user_password(username, password):
    file = open("User/users.txt", 'r')
    lines = file.readlines()
    for line in lines:
        _ = line.split(' ', 1)
        _[1] = _[1][:-1]
        if _[0] == username and _[1] == password:
            line = f'{username} {password} \n'

    file = open('User/users.txt', 'w')
    file.writelines(lines)
    file.close()

def authenticate_user(username, password):
    file = open("Users/users.txt", "r")
    for line in file:
        _ = line.split(' ', 1)
        _[1] = _[1][:-1]
        if _[0] == username and _[1] == password:
            file.close()
            return True
    file.close()
    return False


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

    if check_if_user_exists(username):
        # Utilizador já existe
        redirect(url_for('signup'))

    create_user(username, password)
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

    if authenticate_user(username, password):
        session[username] = True
        response = redirect(url_for('index'))
        response.set_cookie('user_id', username)
        return response

    return redirect(url_for('index'))



