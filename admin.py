from flask import Blueprint, request, redirect, url_for, render_template, jsonify
from auth import check_if_user_exists, create_user, change_user_password

admin = Blueprint('admin', 'admin')


@admin.route('/admin')
def load_admin():
    user_id = request.cookies.get('user_id')
    if user_id != 'root':
        return redirect(url_for('index'))
    return render_template('AdminPanel.html')


@admin.route('/admin/create_user', methods=['POST'])
def admin_create_user():
    username = request.form['usernameC']
    password = request.form['passwordC']

    if check_if_user_exists(username):
        return jsonify({'error': 'Username already exists!'})

    create_user(username, password)

    return jsonify({'success': 'Username registered successfully!'})


@admin.route('/admin/change_password', methods=['PUT'])
def admin_change_password():
    username = request.form['usernameCP']
    password = request.form['passwordCP']

    if check_if_user_exists(username):
        change_user_password(username, password)
        return jsonify({'success': 'Password changed successfully!'})

    return jsonify({'error': 'Username does not exists'})


# TODO: Remover um utilizador e tudo o que o envolve
# TODO: Definir grupos para utilizadores
# TODO: Definir canais


