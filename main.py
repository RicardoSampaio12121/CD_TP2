from flask import Flask, request, url_for, redirect, render_template
from User import User
import users
import auth
from auth import auth


app = Flask(__name__)

app.register_blueprint(auth)


@app.route('/')
def index():
    with open("WebPages/index.html") as file:
        return file.read()


if __name__ == '__main__':
    app.run(debug=True)


# TODO: Criar caixa de mensagens por utilizador
# TODO: Enviar mensagem persistente a utilizador
# TODO: Criação de grupos
# TODO: Enviar mensagem persistente a grupo
# TODO: Notificar ao aparecimento de uma nova mensagem
# TODO: Listar número de mensagens na caixa de mensagens
# TODO: Remover mensagem da caixa de mensagens
