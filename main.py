from flask import Flask, request, url_for, redirect
from UserManagement import UserManagement

app = Flask(__name__)


@app.route('/')
def index():
    with open("WebPages/index.html") as file:
        return file.read()


@app.route("/Register")
def register():
    with open("WebPages/register.html") as file:
        return file.read()


@app.route("/Register", methods=['POST'])
def get_register_data():
    username = request.form['username']
    password = request.form['password']

    um = UserManagement(username, password)
    um.create_user()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)


# TODO: Criar index
# TODO: Criação de utilizadores
# TODO: Autenticação de utilizadores
# TODO: Criar caixa de mensagens por utilizador
# TODO: Enviar mensagem persistente a utilizador
# TODO: Criação de grupos
# TODO: Enviar mensagem persistente a grupo
# TODO: Notificar ao aparecimento de uma nova mensagem
# TODO: Listar número de mensagens na caixa de mensagens
# TODO: Remover mensagem da caixa de mensagens
