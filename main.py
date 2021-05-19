from flask import Flask, session, make_response, render_template, redirect, url_for, request
from auth import auth
from admin import admin
from messenger import messenger

app = Flask(__name__)

app.register_blueprint(auth)
app.register_blueprint(messenger)
app.register_blueprint(admin)


@app.route('/')
def index():
    user_id = request.cookies.get('user_id')
    if user_id:
        print(request.cookies.get('session'))
        print(session)
        return render_template("index.html")
    else:
        return redirect(url_for("auth.login"))


if __name__ == '__main__':
    app.secret_key = "2862"
    app.run(debug=True)

# TODO: Criação de grupos
# TODO: Enviar mensagem persistente a grupo
# TODO: Notificar ao aparecimento de uma nova mensagem
# TODO: Listar número de mensagens na caixa de mensagens
# TODO: Remover mensagem da caixa de mensagens
