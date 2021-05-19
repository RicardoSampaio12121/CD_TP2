from flask import Blueprint, request, redirect, url_for, render_template
from auth import check_if_user_exists, create_user, change_user_password

admin = Blueprint('admin', 'admin')


@admin.route('/admin')
def load_admin():
    user_id = request.cookies.get('user_id')
    if user_id != 'root':
        return redirect(url_for('index'))
    return render_template('AdminPanel.html')


@admin.route('/admin', methods=["POST"])
def admin_post():
    if request.form.get('createUserBtn'):
        username = request.form.get('username')
        password = request.form.get('password')

        if check_if_user_exists(username):
            return redirect(url_for('admin.load_admin'))
        create_user(username, password)

        return redirect(url_for('admin.load_admin'))


@admin.route('/admin', methods=['PUT'])
def admin_put():
    print("entra antes")

    if request.form.get('changePassBtn'):
        print("entra aqui")

        username = request.form.get('username')
        password = request.form.get('password')

        if check_if_user_exists(username):
            change_user_password(username, password)



# TODO: criar utilizadores
# TODO: Permitir alterar a palavra-passe de um utilizador
# TODO: Remover um utilizador e tudo o que o envolve
# TODO: Definir grupos para utilizadores
# TODO: Definir canais
